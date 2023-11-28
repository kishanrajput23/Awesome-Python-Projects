import os;

def main():

    # getting the path
    path = input("Enter the path : ");

    if(path.endswith("/")):
        print();
    else:
        print();
        path += '/';

    # getting the files from the path
    files = os.listdir(path)   

    # interating through the files
    for index, file in enumerate(files):

        # changing the  path 
        renamePath  = path + file;

        # changing the file
        renameFile  = path +'lens image' + str(index)+ '.jpg';
        
        # renaming the file and path
        os.rename(renamePath, renameFile);
        
        # opening the file explorer
        os.system(r'xdg-open '+  path);

        
if __name__ == '__main__':
    main();
    print("Changed the file names");