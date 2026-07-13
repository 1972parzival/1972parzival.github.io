import os
import trimesh
from tqdm import tqdm  # Import tqdm for progress bar

def convert_stl_to_obj(stl_path, obj_path):
    """Converts an STL file to an OBJ file with detailed status updates."""
    try:
        print(f"Starting conversion for: {stl_path}")
        
        # Load the STL file using trimesh
        print(f"Loading STL file: {stl_path}")
        mesh = trimesh.load_mesh(stl_path)
        
        # Check if the mesh is loaded successfully
        if mesh.is_empty:
            print(f"Warning: The mesh in {stl_path} is empty. Skipping conversion.")
            return
        
        # Export the mesh as an OBJ file
        print(f"Exporting to OBJ: {obj_path}")
        mesh.export(obj_path)
        print(f"Successfully converted {stl_path} to {obj_path}")
        
    except Exception as e:
        print(f"Error occurred while converting {stl_path}: {e}")

def convert_all_stls_in_stls_folder():
    """Converts all STL files in the 'stls' folder located where the script is, with detailed status updates and progress bar."""
    
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Script directory: {script_dir}")
    
    # Set the path to the 'stls' folder inside the script's directory
    stls_folder = os.path.join(script_dir, 'stls')
    
    # Check if the 'stls' folder exists
    if not os.path.exists(stls_folder):
        print(f"The directory '{stls_folder}' does not exist!")
        return
    
    print(f"Looking for STL files in: {stls_folder}")
    
    # Flag to check if we found any STL files
    found_stls = False
    stl_files = [f for f in os.listdir(stls_folder) if f.endswith(".stl")]
    total_files = len(stl_files)
    print(f"Found {total_files} STL files in the 'stls' folder.")

    if total_files == 0:
        print("No STL files found in the 'stls' folder.")
        return
    
    # Use tqdm for progress bar
    for i, filename in enumerate(tqdm(stl_files, desc="Converting files", unit="file")):
        stl_file_path = os.path.join(stls_folder, filename)
        obj_file_path = os.path.splitext(stl_file_path)[0] + ".obj"
        
        # Conversion process for each STL file
        print(f"Found STL file: {filename}. Starting conversion...")
        convert_stl_to_obj(stl_file_path, obj_file_path)

    print(f"Conversion completed for all {total_files} STL files in '{stls_folder}'.")

if __name__ == "__main__":
    print("Starting STL to OBJ conversion process...")
    # Call the function to convert all STL files in the 'stls' folder
    convert_all_stls_in_stls_folder()
    print("Conversion process finished.")
