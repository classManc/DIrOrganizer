import argparse
import os
import shutil

# Takes the full path of the directory you want to organize as an argument
def dir_organizer(dir_path):
    
    # gets a list of all the files and folders in the directory and asign the to a variable
    dir_content = os.listdir(dir_path)

    # loop over each element in the list
    for content in dir_content:
    
        # check if it is a file, 
        if os.path.isfile((os.path.join(dir_path,content))): # it needs the full path of the file you want to check, if you are not in the directory where the file is located
            file_extension = os.path.splitext(content)[1].lower() # split it if it is a file and get the second element
            
            if file_extension in ['.txt', '.csv', '.log', ',py']: # check if the element extension gotten from above is in the list
                document_folder = os.path.join(dir_path, 'document') # if it is, join the path of the directory with the string "document"
                os.makedirs(document_folder, exist_ok=True) # create a new folder called document with the path from above
                # move the file to the document folder
                shutil.move((os.path.join(dir_path,content)), os.path.join(dir_path, document_folder)) #it needs the full path of the file you want to check, if you are not in the directory where the file is located
                                                       
            
            elif file_extension in ['.mp4', '.avi', '.mkv']:
                video_folder = os.path.join(dir_path, 'videos')
                os.makedirs(video_folder, exist_ok=True)
                shutil.move((os.path.join(dir_path,content)), os.path.join(dir_path, video_folder))

            elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                image_folder = os.path.join(dir_path, 'image')
                os.makedirs(image_folder, exist_ok=True)
                shutil.move((os.path.join(dir_path,content)), os.path.join(dir_path, image_folder))
                
            else:
                pass
        else:
            pass

if __name__ == '__main__':
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='File Organizer Script')

    # Add an argument for the directory path
    parser.add_argument('dir_path', type=str, help='Path to the directory')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the file organizer function with the provided directory path
    dir_organizer(args.dir_path)

                