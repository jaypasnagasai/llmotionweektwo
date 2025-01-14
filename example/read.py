import h5py

# Path to the .h5 file
h5_file_path = '007538.h5'

# Open the file in read mode
with h5py.File(h5_file_path, 'r') as h5_file:
    # List all datasets in the file
    print("Datasets in the file:", list(h5_file.keys()))
    
    # Access the text data
    text_data = h5_file['text_data'][:]
    print("Text Data:", [text.decode('utf-8') for text in text_data])
    
    # Access the pose data
    pose_data = h5_file['pose_data'][:]
    print("Pose Data Shape:", pose_data.shape)
