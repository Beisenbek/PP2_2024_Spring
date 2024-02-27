import os 
   
# Get the path of current working directory 
path = os.getcwd() 
   
# Get the list of all files and directories 
dir_list = os.listdir(path) 
   
print("Files and directories in '", path, "' :")  
# print the list 
print(dir_list)