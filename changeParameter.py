import os

print("which file")
filename = input()

while 1:
    Dir = "/Users/gao/Desktop/"
    Dir = Dir+filename
    os.chdir(Dir)

    print("which parameter to change:")
    para = input()
    print("input the number you want:")
    para_num = input()

    new_line = ""

    for dirs, paths, file in os.walk("."):
        for f in file:
            f = os.path.join(dirs, f)
            if f.find("config") != -1 and f.endswith(".txt") is True:
                new_line = ""
                print(f)
                input_file = open(f, "r+")
                for line in input_file:
                    if line.find(para) != -1:
                        temp = line.split("=")
                        new_line += temp[0]+"= "+para_num+"\n"
                    else:
                        new_line += line

                input_file.seek(0)
                input_file.write(new_line)
                input_file.close()










