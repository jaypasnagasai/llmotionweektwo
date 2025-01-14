import numpy as np
import h5py

# Load the text file
with open('007538.txt', 'r') as txt_file:
    text_data = txt_file.readlines()

# Load the .npy file
npy_data = np.load('007538.npy')

# Create the HDF5 file
output_h5_path = '007538.h5'
with h5py.File(output_h5_path, 'w') as h5_file:
    # Save text data
    text_dataset = h5_file.create_dataset('text_data', data=np.string_(text_data))
    
    # Save npy data
    npy_dataset = h5_file.create_dataset('pose_data', data=npy_data)

print(f"Combined data saved to {output_h5_path}")
