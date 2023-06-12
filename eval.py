import deeplabcut, os
from init import config_path, videolist


deeplabcut.evaluate_network(config_path, plotting=True)

