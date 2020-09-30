import os

def delete_all(path):
    new_path = os.chdir(path)
    for sth in os.listdir(path):
        if os.path.isfile(sth):
            print("file")
            os.unlink(path + "/"+sth,dir_fd= None)
        if os.path.isdir(sth):
            dir_contains = os.listdir("./"+sth)
            print(os.getcwd())
            if len(dir_contains) != 0:
                delete_all(path + "/" + sth)
            print("dir")
    os.rmdir(path)




delete_all("/home/andreea/Desktop/ceva")