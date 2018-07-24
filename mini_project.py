import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Python\mini_project")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\Python\mini_project")
    
    #(2) for each file, rename filename
    table = str.maketrans("","","0123456789")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(table))
    os.chdir(saved_path)
    
rename_files()
