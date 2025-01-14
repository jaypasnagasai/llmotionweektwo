# LLMotion: Week 2

## AGENDA
To find the `pose_data` and `text_data` for a motion in the AMASS DATASET

## MASTER DATASET
The dataset the motion data has been extracted from 

- Dataset: [ACCAD](https://accad.osu.edu/research/motion-lab/mocap-system-and-data)
- Subjects: 20
- Motions: 252
- Video: 26.74 min

## EXAMPLE MOTION
The motion used to extract the left knee

- File Name: [Run1_poses.npz](example.npz)
- Folder: s008
  
- Poses_Data: [poses.npy](poses.npy)
- `text_data`: [example.npz](text.txt)
- HumanML3D: 007568
  
- Gender: Male
- Frame Rate: 120 fps
- Video Duration: 1.8 s
- Total # of Frames: 217
- Type: SMPL-H

## SMPL-H LEGEND

According to the [Meshcapade Wiki](https://github.com/Meshcapade/wiki/blob/main/wiki/SMPL.md), here is the legend of the SMPL-H skeleton dataset,
```
     0: 'pelvis',
     1: 'left_hip',
     2: 'right_hip',
     3: 'spine1',
     4: 'left_knee',
     5: 'right_knee',
     6: 'spine2',
     7: 'left_ankle',
     8: 'right_ankle',
     9: 'spine3',
    10: 'left_foot',
    11: 'right_foot',
    12: 'neck',
    13: 'left_collar',
    14: 'right_collar',
    15: 'head',
    16: 'left_shoulder',
    17: 'right_shoulder',
    18: 'left_elbow',
    19: 'right_elbow',
    20: 'left_wrist',
    21: 'right_wrist',
    22: 'left_index1',
    23: 'left_index2',
    24: 'left_index3',
    25: 'left_middle1',
    26: 'left_middle2',
    27: 'left_middle3',
    28: 'left_pinky1',
    29: 'left_pinky2',
    30: 'left_pinky3',
    31: 'left_ring1',
    32: 'left_ring2',
    33: 'left_ring3',
    34: 'left_thumb1',
    35: 'left_thumb2',
    36: 'left_thumb3',
    37: 'right_index1',
    38: 'right_index2',
    39: 'right_index3',
    40: 'right_middle1',
    41: 'right_middle2',
    42: 'right_middle3',
    43: 'right_pinky1',
    44: 'right_pinky2',
    45: 'right_pinky3',
    46: 'right_ring1',
    47: 'right_ring2',
    48: 'right_ring3',
    49: 'right_thumb1',
    50: 'right_thumb2',
    51: 'right_thumb3'
```

## NOTE

- The text descriptions are is form the [HumanML3D](https://github.com/EricGuo5513/HumanML3D/tree/main/HumanML3D) dataset
- The mapping of the `pose_data` to the `text_data` is through using the [index](https://github.com/EricGuo5513/HumanML3D/blob/main/index.csv) of the dataset

## IMPLEMENTATION

1. Install NumPy to load arrays
2. Run [extract.py](extract.py) to load [example.npz](example.npz) and create [poses.npy](poses.npy) for pose data

## IMPLEMENTATION [OPTIONAL]

1. Install NumPy to load arrays
2. Run [main.py](main.py) to combine [poses.npy](poses.npy) & [text.txt](text.txt) to a `.h5` file
3. Run [read.py](read.py) to load [motion.h5](motion.h5)

## PROGRESS

- Since it is possible to map `pose_data` and `text_data` to one file, it is replicable to the dataset.
- While I have used a more rudimentary approach to extract `pose_data`, the [HumanML3D](https://github.com/EricGuo5513/HumanML3D/tree/main/HumanML3D) repo has a Jupyter Notebook which can do this more efficiently.
- The next step is to able to set up the `pose_data` from all the datasets

## CHALLENGES

1. The data is in 3D Arrays. Finetuning array files directly could be ineffective since LLMs are inclined to deal with structured data (CSV/JSON). Hence, the most basic approach would be to flatten the data. But, I am unsure of how effective it will be.
2. Some motions have multiple text descriptions, hence it is important to be cognizant of them. Luckily, the Jupyter notebook should help us in the files processing. So, replicating the notebook should be ideal.
3. The HumanML3D dataset does not have text descriptions for the more recent AMASS datasets. So, if we are certain that the existent data is suffient, we can go ahead.

## CONCLUSION

A major part of this week was about mapping the `pose_data` to the `text_data`. I started out to do for the entire ACCAD dataset, but due to the repetition of certain motions, I have decided to demonstrate the mapping with one example motion. The key aspect is to focus on the [challenges](#challenges) and work on them. Any feedback would be appreciated. Thank You!
