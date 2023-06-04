import deeplabcut, os

cwd = os.getcwd()
print(f'Successfully imported DeepLabCut version: {deeplabcut. __version__}')

videolist = ['Videos\HeartBaseline.mp4']
for i in enumerate(videolist):
    videolist[i[0]] = cwd + '\\' + videolist[i[0]]
print(videolist)

config_path = deeplabcut.create_new_project('DLC Test', 'BMERIT - Ahmed Almousawi', videolist, working_directory=cwd, copy_videos=False, multianimal=False)
