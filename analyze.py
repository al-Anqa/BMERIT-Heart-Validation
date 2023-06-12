import deeplabcut, os
from init import config_path, videolist


deeplabcut.analyze_videos(config_path, videolist, save_as_csv=True)

