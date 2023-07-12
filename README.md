
# File Organizer

A brief description of what this project does and who it's for
A script that help organize a directory

it is a function that accept a full path of the directory you want to organize as an argument gets a list of all the files and folders in the directory and asign the to a variable loops over each element in the list and checks if it is file if it is, it split the element's name into two with one item being the element path and the othe being the extension it grabs the part with the extension it then checks if the extension is can be found in a list containing different extensions for documents, images or videos use os.path.join() to join the path of the directory given as argument with the name of the folder you want to place the file it then creates a directory by using the path generated above finally, it calls the shutil.move() function passing the file name as an argument and the concatenated directory as the destination



## Running this script

To run this script input the below on the terminal

```bash
  python3 file_organizer '/Users/ajakayejoseph/Desktop/<name of the folder you want to organize>'
```
