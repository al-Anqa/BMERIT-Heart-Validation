import deeplabcut, os
from init import config_path, videolist


deeplabcut.create_labeled_video(config_path, videolist, save_frames = True, draw_skeleton = True, videotype='.mp4')
