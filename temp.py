import os

def delete_temp_and_recycle_bin():
    # Delete all the files in the temp folder
    temp_folder = os.environ['temp']
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            try:
                os.unlink(os.path.join(root, file))
            except OSError:
                continue

    # Delete all the files in the recycle bin
    path = 'C:\\$Recycle.Bin'
    for root, dirs, files in os.walk(path):
        for f in files:
            os.unlink(os.path.join(root, f))

    # Delete all the directories in the recycle bin
    for root, dirs, files in os.walk(path):
        for d in dirs:
            os.rmdir(os.path.join(root, d))
