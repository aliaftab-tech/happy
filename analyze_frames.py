import os
from PIL import Image
import numpy as np

frames_dir = r"d:\happy birthday\video_frames"

def analyze_frame(frame_num):
    img_path = os.path.join(frames_dir, f"frame_{frame_num:03d}.jpg")
    img = Image.open(img_path)
    arr = np.array(img)
    # Background color is roughly arr[100, 100]
    bg = arr[100, 100].astype(int)
    print(f"Frame {frame_num} bg color approx: {bg}")

analyze_frame(3)
analyze_frame(6)
analyze_frame(9)
analyze_frame(16)
analyze_frame(18)
analyze_frame(22)
analyze_frame(24)
analyze_frame(30)
analyze_frame(38)
analyze_frame(47)
