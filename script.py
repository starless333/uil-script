import os

def get_dat_files(files: list[list[chr]]) -> list[list[chr]]:
    dats = []
    for f in files:
        arr = f.split('.')
        if arr[-1] == 'dat':
            dats.append(f)
    return dats

def write_file(string) -> None:
    f = open(string+'/' + string + '.java', "w")
    f.write("import java.util.*;\nimport java.io.*;\n")
    f.write("import static java.lang.System;\n\n")
    f.write("public class " + string + "{\n    public static void main(String[]args) throws IOException {\n        ");
    f.write("Scanner sc = new Scanner(new File(\"" + string.lower() +".dat\"))\n        ")
    f.write("int T = sc.nextInt();\n        while(T-- > 0) {\n");
    f.write("            solve(sc);\n        }\n        sc.close();\n    }\n")
    f.write("    public static void solve(Scanner sc) throws IOException {\n    ")
    f.write("    int m; int n; int[][] mat; int[] arr;\n        \n")
    f.write("    }\n}")
    f.close()
def make_dirs(dats: list[list[chr]]) -> None:
    for f in dats:
        name = f.split('.')[0]
        name = name.capitalize()
        os.mkdir(name)
        os.rename(f,name+'/'+f)
        os.close(os.open(name + '/' + name + '.java' , os.O_CREAT))
        write_file(name)
        os.popen("cp ~/Makefile " + name + "/Makefile")
def __main__():
    dir = os.curdir
    files = os.listdir(dir)
    files = [f for f in files if os.path.isfile(dir+'/'+f)]
    dats = get_dat_files(files)
    make_dirs(dats)

__main__()
