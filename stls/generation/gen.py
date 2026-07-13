#!/usr/bin/env python3
"""
text_to_stl.py — turn a line of text into a simple extruded 3D STL model.

This version avoids shapely/trimesh (which can be finicky to install on some
Macs because of the GEOS C library). It only needs matplotlib, numpy, and
triangle.

Edit the TEXT / SIZE / DEPTH / FONT_PATH constants below, then run:
    python3 text_to_stl.py

The output .stl is saved in the same folder as this script, named after
the text (e.g. TEXT = "Hi" -> Hi.stl).

Dependencies:
    pip3 install matplotlib numpy triangle
"""

import os
import struct
import numpy as np
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path as MplPath
import triangle as tr

# ─── EDIT THESE ────────────────────────────────────────────────────────────
TEXT = "dc motor control"       # the text to convert
SIZE = 50            # font size (roughly the height in mm)
DEPTH = 5            # extrusion depth/thickness
FONT_PATH = None     # optional path to a .ttf/.otf font file, or None for default
# ────────────────────────────────────────────────────────────────────────────


def signed_area(pts):
    x, y = pts[:, 0], pts[:, 1]
    return 0.5 * np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)


def get_loops(text, size, font_path):
    fp = FontProperties(fname=font_path) if font_path else FontProperties()
    path = TextPath((0, 0), text, size=size, prop=fp)
    loops = []
    for p in path.to_polygons():
        p = np.asarray(p)
        if len(p) > 2:
            # drop duplicate closing point if present
            if np.allclose(p[0], p[-1]):
                p = p[:-1]
            if len(p) > 2:
                loops.append(p)
    return loops


def classify_loops(loops):
    """Return list of (points, is_hole) sorted largest-first,
    using point-in-polygon containment to detect nested (hole) loops."""
    order = sorted(range(len(loops)), key=lambda i: abs(signed_area(loops[i])), reverse=True)
    paths = [MplPath(loops[i]) for i in order]
    is_hole = [False] * len(order)

    for a in range(len(order)):
        centroid_a = loops[order[a]].mean(axis=0)
        contained_in = [b for b in range(a) if paths[b].contains_point(centroid_a)]
        # nested inside an odd number of larger loops => this loop is a hole
        is_hole[a] = (len(contained_in) % 2 == 1)

    return [(loops[order[i]], is_hole[i]) for i in range(len(order))]


def build_pslg(classified):
    """Build the vertices/segments/holes structure the `triangle` library expects."""
    vertices = []
    segments = []
    holes = []
    normalized = []

    for pts, hole in classified:
        # enforce consistent winding: outer loops CCW, hole loops CW
        area = signed_area(pts)
        if hole and area > 0:
            pts = pts[::-1]
        elif not hole and area < 0:
            pts = pts[::-1]
        normalized.append((pts, hole))

        start = len(vertices)
        n = len(pts)
        vertices.extend(pts.tolist())
        for i in range(n):
            segments.append((start + i, start + (i + 1) % n))

        if hole:
            holes.append(pts.mean(axis=0).tolist())

    return np.array(vertices), np.array(segments), (np.array(holes) if holes else None), normalized


def triangulate(vertices, segments, holes):
    A = dict(vertices=vertices, segments=segments)
    if holes is not None:
        A["holes"] = holes
    result = tr.triangulate(A, "p")
    return result["vertices"], result["triangles"]


def extrude(tri_verts, tri_faces, normalized, depth):
    n = len(tri_verts)
    bottom = np.hstack([tri_verts, np.zeros((n, 1))])
    top = np.hstack([tri_verts, np.full((n, 1), depth)])
    all_verts = np.vstack([bottom, top])

    faces = []
    # bottom cap (normal -z): reverse winding
    for a, b, c in tri_faces:
        faces.append((a, c, b))
    # top cap (normal +z): offset indices into the "top" block
    for a, b, c in tri_faces:
        faces.append((a + n, b + n, c + n))

    # side walls, built straight from the (already normalized) boundary loops
    for pts, hole in normalized:
        idx = [np.argmin(np.sum((tri_verts - p) ** 2, axis=1)) for p in pts]
        m = len(idx)
        for i in range(m):
            b1, b2 = idx[i], idx[(i + 1) % m]
            t1, t2 = b1 + n, b2 + n
            faces.append((b1, b2, t2))
            faces.append((b1, t2, t1))

    return all_verts, np.array(faces)


def write_binary_stl(path, verts, faces):
    with open(path, "wb") as f:
        f.write(b"\0" * 80)
        f.write(struct.pack("<I", len(faces)))
        for a, b, c in faces:
            v0, v1, v2 = verts[a], verts[b], verts[c]
            normal = np.cross(v1 - v0, v2 - v0)
            norm_len = np.linalg.norm(normal)
            if norm_len > 0:
                normal = normal / norm_len
            f.write(struct.pack("<3f", *normal))
            for v in (v0, v1, v2):
                f.write(struct.pack("<3f", *v))
            f.write(struct.pack("<H", 0))


def build_stl(text, out_path, size=50, depth=5, font_path=None):
    loops = get_loops(text, size, font_path)
    if not loops:
        raise ValueError("No renderable glyphs found in the given text.")

    classified = classify_loops(loops)
    vertices, segments, holes, normalized = build_pslg(classified)
    tri_verts, tri_faces = triangulate(vertices, segments, holes)
    all_verts, faces = extrude(tri_verts, tri_faces, normalized, depth)

    # center the model at the origin
    center = all_verts.mean(axis=0)
    all_verts = all_verts - center

    write_binary_stl(out_path, all_verts, faces)

    extents = all_verts.max(axis=0) - all_verts.min(axis=0)
    print(f"Saved: {out_path}")
    print(f"Bounding box (mm): {np.round(extents, 2)}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    safe_name = "".join(c if c.isalnum() else "_" for c in TEXT).strip("_") or "output"
    out_path = os.path.join(script_dir, f"{safe_name}.stl")
    build_stl(TEXT, out_path, size=SIZE, depth=DEPTH, font_path=FONT_PATH)


if __name__ == "__main__":
    main()