import deeplabcut, os

cwd = os.getcwd()
print(f'Successfully imported DeepLabCut version: {deeplabcut. __version__}')

videolist = ['Videos\HeartUltrasound.mp4']
for i in enumerate(videolist):
    videolist[i[0]] = cwd + '\\' + videolist[i[0]]
print(videolist)

config_path = 'C:\\Users\\Ahmed\\Desktop\\HeartValidation--DeepLabCut\\Ultrasound1-Ahmed-2023-08-09\\config.yaml'
if os.path.exists('DLC Test-BMERIT - Ahmed Almousawi-2023-06-11') == False:
    config_path = deeplabcut.create_new_project('DLC Test', 'BMERIT - Ahmed Almousawi', videolist, working_directory=cwd, copy_videos=False, multianimal=False)

# This extracts useful frames from the videos automatically
# deeplabcut.extract_frames(config_path, mode='automatic', algo='kmeans', userfeedback=False)

# This lets you check the points before doing anything major
# deeplabcut.check_labels(config_path, visualizeindividuals=True)
