import React, { useState, useEffect, useRef, useCallback} from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader';
import * as THREE from 'three';
import './App.css';

// Custom hook to manage model caching
const useModelCache = () => {
  const [modelCache, setModelCache] = useState({});
  const [loadingModels, setLoadingModels] = useState({});

  const loadModel = useCallback((modelPath) => {
    return new Promise((resolve, reject) => {
      // Check if model is already cached
      if (modelCache[modelPath]) {
        resolve(modelCache[modelPath]);
        return;
      }

      // Check if model is currently loading
      if (loadingModels[modelPath]) {
        loadingModels[modelPath].then(resolve);
        return;
      }

      const loader = new OBJLoader();
      const modelLoading = new Promise((innerResolve, innerReject) => {
        loader.load(
          modelPath,
          (obj) => {
            const newModelRef = new THREE.Group();

            const box = new THREE.Box3().setFromObject(obj);
            const size = box.getSize(new THREE.Vector3());
            const maxDimension = Math.max(size.x, size.y, size.z);
            obj.rotation.x = -Math.PI / 2;
            const scaleFactor = 2.5 / maxDimension;
            obj.scale.set(scaleFactor, scaleFactor, scaleFactor);

            box.setFromObject(obj);
            const center = box.getCenter(new THREE.Vector3());
            obj.position.sub(center);

            obj.traverse((child) => {
              if (child.isMesh) {
                const edges = new THREE.EdgesGeometry(child.geometry, 45);
                const lineMaterial = new THREE.LineBasicMaterial({
                  color: 0xffffff,
                  opacity: 0.5,
                  transparent: true,
                });
                const edgeLines = new THREE.LineSegments(edges, lineMaterial);
                edgeLines.position.copy(child.position);
                edgeLines.rotation.copy(child.rotation);
                edgeLines.scale.copy(child.scale);
                child.parent.add(edgeLines);
                child.parent.remove(child);
              }
            });

            newModelRef.add(obj);

            // Update cache
            setModelCache(prev => ({
              ...prev,
              [modelPath]: newModelRef
            }));

            // Remove from loading models
            setLoadingModels(prev => {
              const updated = { ...prev };
              delete updated[modelPath];
              return updated;
            });

            innerResolve(newModelRef);
            resolve(newModelRef);
          },
          undefined,
          (error) => {
            innerReject(error);
            reject(error);
          }
        );
      });

      // Track loading models
      setLoadingModels(prev => ({
        ...prev,
        [modelPath]: modelLoading
      }));

      return modelLoading;
    });
  }, [modelCache,loadingModels]);

  return { modelCache, loadModel };
};


const ModelLoader = ({ modelPath }) => {
  const [model, setModel] = useState(null);
  const { loadModel } = useModelCache();
  const groupRef = useRef(null);

  useEffect(() => {
    loadModel(modelPath)
      .then(setModel)
      .catch(error => console.error('Error loading OBJ:', error));
  }, [modelPath, loadModel]);

  // Apply rotations to the model group
  useFrame(() => {
    if (groupRef.current) {
      groupRef.current.rotation.y += 0.003;
    }
  });

  return (
    <group ref={groupRef}>
      {!model && (
        <mesh>
          <boxGeometry args={[1, 1, 1]} />
          <meshBasicMaterial color="white" wireframe={true} />
        </mesh>
      )}
      {model && <primitive object={model} />}
    </group>
  );
};

const App = () => {
  const [models, setModels] = useState([]);
  // Track selection by INDEX, not by `file`. Multiple entries can share the
  // same .obj file (e.g. every blog post defaults to logo.obj), so `file`
  // is not a safe unique identifier.
  const [selectedIndex, setSelectedIndex] = useState(0);
  const [highlightedIndex, setHighlightedIndex] = useState(null);
  const [asciiArt, setAsciiArt] = useState('');
  const [asciiIndex, setAsciiIndex] = useState(0);
  const [asciiComplete, setAsciiComplete] = useState(false);
  const {loadModel } = useModelCache();
  const [isMobile, setIsMobile] = useState(window.innerWidth <= 800);

  const selectedModelData = models[selectedIndex];

  const navigateToSelected = useCallback(() => {
    if (selectedModelData && selectedModelData.site) {
      window.location.href = selectedModelData.site;
    }
  }, [selectedModelData]);

  const handleCanvasClick = () => {
    navigateToSelected();
  };

  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth <= 800);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  useEffect(() => {
    fetch('./models.json')
      .then((response) => response.json())
      .then((data) => {
        setModels(data);
        setSelectedIndex(0);

        // Preload all models in the background
        data.forEach(model => {
          loadModel(`./stls/${model.file}`);
        });
      })
      .catch((error) => console.error('Error loading models:', error));
  }, [loadModel]);

  const asciiArtString = `
......................................................................................................
..............@@@@......................@@@....................@@@@...................................
.............@@..@@...................@@@@@@@.................@@@@@@@..........@@@@@@@@@@@@@@@@@@@@...
............@@....@@.................@@@@@@@@@..............@@@@@@@@@@.........@@@@@@@@@@@@@@@@@@@....
............@......@...............@@@@@@@@@@@@@...........@@@@@@@@@@@@........@@@@@@@@@@@@@@@@@......
...........@@......@@.............@@@@@@@@@@@@@@@.........@@@@@@@@@@@@@@@......@@@@@@@@@@@@@@@@.......
..........@@........@@.............@@@@@@@@@@@@@..........@@@@@@@@@@@@@@.................@@@@.........
.........@@..........@@.............@@@@@@@@@@@.............@@@@@@@@@@@..................@@@..........
........@@...........@@..............@@@@@@@@................@@@@@@@@....................@@...........
.......@@.............@@.............@@@@@@@@................@@@@@@@@....................@............
.......@@.....@@@@.....@@...........@@@.@@..@@..............@@@.@@.@@@.........@@@@@..................
......@@......@..@......@@.........@@@......@@@...........@@@@......@@@........@@@@@..................
.....@@......@....@@@@@@@@........@@@...@@@..@@@@.........@@@..@@@...@@@........@@@@@.................
....@@......@.@@@@@@@@@@@@@......@@@...@@@@@..@@@........@@@...@@@@...@@@.......@@@@@@@...............
....@......@@.@@@.........@@....@@@....@@@@@...@@@......@@@...@@@@@@...@@@.......@@@@@@@@@@@@@@@@.....
..@@@.....@@....@@@........@@..@@@@@@@@@@@@@@@@@@@@....@@@@@@@@@@@@@@@@@@@@........@@@@@@@@@@@@@@.....
..@@@@@@@@@........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@.........@@@@@@@@@@@@.....
......................................................................................................
  `;

  useEffect(() => {
    if (asciiIndex < asciiArtString.length) {
      const interval = setInterval(() => {
        setAsciiArt((prev) => prev + asciiArtString[asciiIndex]);
        setAsciiIndex((prev) => prev + 1);
      }, 5);

      return () => clearInterval(interval);
    } else {
      setAsciiComplete(true);
    }
  }, [asciiIndex, asciiArtString]);

  const handleKeyPress = useCallback((event) => {
    if (models.length === 0) return;
    if (event.key === 'ArrowDown') {
      setSelectedIndex((prev) => (prev + 1) % models.length);
    } else if (event.key === 'ArrowUp') {
      setSelectedIndex((prev) => (prev - 1 + models.length) % models.length);
    } else if (event.key === 'Enter') {
      navigateToSelected();
    }
  }, [models, navigateToSelected]);

  useEffect(() => {
    window.addEventListener('keydown', handleKeyPress);
    return () => {
      window.removeEventListener('keydown', handleKeyPress);
    };
  }, [handleKeyPress]);

  return (
    <div className="container">
      {isMobile ? (
        <div className="dropdown-container">
          <select
            value={selectedIndex}
            onChange={(e) => setSelectedIndex(Number(e.target.value))}
          >
            {models.map((model, index) => (
              <option key={`${model.file}-${index}`} value={index}>
                {model.name}
              </option>
            ))}
          </select>
        </div>
      ) : (
        <div className="sidebar">
          <h3>Select a Project</h3>
          <ul>
            {models.map((model, index) => (
              <li
                key={`${model.file}-${index}`}
                className={`${selectedIndex === index ? 'selected' : ''} ${highlightedIndex === index ? 'highlighted' : ''}`}
                onClick={() => setSelectedIndex(index)}
                onMouseEnter={() => setHighlightedIndex(index)}
                onMouseLeave={() => setHighlightedIndex(null)}
              >
                {selectedIndex === index ? `> ${model.name}` : model.name}
              </li>
            ))}
          </ul>
        </div>
      )}


      <div className="right-container">
        {!asciiComplete && (
          <div className="ascii-art">
            {asciiArt}
          </div>
        )}

        {asciiComplete && (
          <Canvas
            style={{ backgroundColor: 'black' }}
            camera={{
              position: [2.5, 2.5, 2.5],
              fov: 45,
            }}
            onClick={handleCanvasClick}
          >

            <ambientLight intensity={0.5} />
            <spotLight position={[10, 10, 10]} intensity={1} />
            <directionalLight position={[5, 5, 5]} intensity={1} />
            {selectedModelData &&
              <ModelLoader modelPath={`./stls/${selectedModelData.file}`} />
            }

            <OrbitControls
              enableZoom={false}
              minPolarAngle={Math.PI / 4}
              maxPolarAngle={Math.PI / 4}
              minAzimuthAngle={-Math.PI / 4}
              maxAzimuthAngle={Math.PI / 4}
            />
          </Canvas>
        )}
      </div>
    </div>
  );
};

export default App;