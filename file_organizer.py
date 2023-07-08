import os
import shutil

# Takes the full path of the directory you want to organize as an argument
def dir_organizer(dir_path):
    
    # gets a list of all the files and folders in the directory and asign the to a variable
    dir_content = os.listdir(dir_path)

    # loop over each element in the list
    for content in dir_content:
        
        # check if it is a file
        if os.path.isfile(content):
            file_extension = os.path.splitext(content)[1].lower() # split it if it is a file and get the second element
            
            if file_extension in ['.txt', '.csv', '.log', ',py']: # check if the element extension gotten from above is in the list
                document_folder = os.path.join(dir_path, 'document') # if it is, join the path of the directory with the string "document"
                os.makedirs(document_folder, exist_ok=True) # create a new folder called document with the path from above
                destination_file = os.path.join(document_folder, content) # join the path of the ddocumment folder to the name of the current file in the loop
                shutil.move(content, destination_file) # move the file to the document folder
            
            elif file_extension in ['.mp4', '.avi', '.mkv']:
                video_folder = os.path.join(dir_path, 'videos')
                os.makedirs(video_folder, exist_ok=True)
                destination_file = os.path.join(video_folder, content)
                shutil.move(content, destination_file)

            elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                image_folder = os.path.join(dir_path, 'image')
                os.makedirs(image_folder, exist_ok=True)
                destination_file = os.path.join(image_folder, content)
                shutil.move(content, destination_file)
            else:
                pass
        else:
            pass

                