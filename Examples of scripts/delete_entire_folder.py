import os

def delete_all(path):
    new_path = os.chdir(path)
    for sth in os.listdir(path):
        if os.path.isfile(sth):
            print("file")
            #os.unlink("./"+sth,dir_fd= None)
        if os.path.isdir(sth):
            dir_contains = os.listdir("./"+sth)
            print(os.getcwd())
            if len(dir_contains) != 0:
                print(type(sth))
                print(type(new_path))
                delete_all(new_path + "/" + sth)
            #os.rmdir("./"+sth)
            print("dir")


delete_all("/home/andreea/Desktop/ceva")