import os

def delete_all(path):
    os.chdir(path)
    for sth in os.listdir(path):
        if os.path.isfile(sth):
            #print("file " + sth + " in " + path)
            os.unlink(path + "/" + sth,dir_fd= None)
        elif os.path.isdir(sth):
            dir_contains = os.listdir("./"+sth)
            if len(dir_contains) != 0:
                os.chdir(path + "/" + sth)
                #print("dir found in " + path + " named " + sth)
                delete_all(path + "/" + sth)
    #print(path)
            os.chdir(path)
            os.rmdir(path + "/" + sth)



delete_all("/home/andreea/Desktop/ceva2")