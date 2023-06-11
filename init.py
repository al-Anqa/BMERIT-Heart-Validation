import deeplabcut, os

cwd = os.getcwd()
print(f'Successfully imported DeepLabCut version: {deeplabcut. __version__}')

videolist = ['Videos\HeartBaseline.mp4']
for i in enumerate(videolist):
    videolist[i[0]] = cwd + '\\' + videolist[i[0]]
print(videolist)

config_path = 'C:\\Users\\ahmed\\Desktop\\HeartValidation--DeepLabCut\\DLC Test-BMERIT - Ahmed Almousawi-2023-06-11\\config.yaml'
if os.path.exists('DLC Test-BMERIT - Ahmed Almousawi-2023-06-11') == False:
    config_path = deeplabcut.create_new_project('DLC Test', 'BMERIT - Ahmed Almousawi', videolist, working_directory=cwd, copy_videos=False, multianimal=False)

# deeplabcut.extract_frames(config_path, mode='automatic', algo='kmeans', userfeedback=False)

# deeplabcut.check_labels(config_path, visualizeindividuals=True)

deeplabcut.SkeletonBuilder(config_path)

