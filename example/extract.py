import os
import numpy as np

# Directory containing the script and .npz files
directory = os.getcwd()  # Use the current working directory

# Output directory for new .npy files
output_directory = os.path.join(directory, "processed")
os.makedirs(output_directory, exist_ok=True)

# Function to process each .npz file
def process_npz_file(filepath, output_directory, index):
    try:
        # Load the .npz file
        data = np.load(filepath, allow_pickle=True)

        # Ensure the 'poses' key exists in the file
        if "poses" in data.keys():
            poses = data["poses"]

            # Create output filepath with numbered filename
            output_filename = f"{index:04d}.npy"
            output_filepath = os.path.join(output_directory, output_filename)

            # Save the poses data to a new .npy file
            np.save(output_filepath, poses)
            print(f"Processed and saved: {output_filepath}")
        else:
            print(f"Key 'poses' not found in {filepath}. Skipping.")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# Debug: Print the output directory
print(f"Output directory: {output_directory}")

# Iterate through all .npz files in the directory
index = 1
for filename in sorted(os.listdir(directory)):
    if filename.endswith(".npz"):
        filepath = os.path.join(directory, filename)
        print(f"Processing {filename} -> Saving as {index:04d}.npy")  # Debug: Log the processing
        process_npz_file(filepath, output_directory, index)
        index += 1

print("Processing complete.")




# Desktop/ACAAD/pose_data/ACCAD/Female1General_c3d