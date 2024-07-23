import os

def get_dat_files(files: list[list[chr]]) -> list[list[chr]]:
    dats = []
    for f in files:
        arr = f.split('.')
        if arr[-1] == 'dat':
            dats.append(f)
    return dats

def make_dirs(dats: list[list[chr]]) -> None:
    for f in dats:
        name = f.split('.')[0]
        name = name.capitalize()
        os.mkdir(name)
        os.rename(f,name+'/'+f)
        os.close(os.open(name + '/' + name + '.java' , os.O_CREAT))
        os.popen("cp ~/Makefile " + name + "/Makefile")

def __main__():
    dir = os.curdir
    files = os.listdir(dir)
    files = [f for f in files if os.path.isfile(dir+'/'+f)]
    dats = get_dat_files(files)
    make_dirs(dats)
    
    
__main__()
