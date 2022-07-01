import sys
import enum
VERSION_FILE = "Version.txt"

version_convert = {
    "MAJOR": 0,
    "MINOR": 1,
    "PATCH": 2
}

def read_version():
    lines = []
    with open(VERSION_FILE) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def write_version(lines):
    with open(VERSION_FILE, "w") as file:
        file.writelines(lines)
        

def print_usage():
    print("usage: ver.py <get/increase> <MAJOR/MINOR/PATCH>")
    print("example:")
    print("python3 ver.py get MAJOR")
    print("python3 ver.py increase PATCH")


def program():
    if len(sys.argv) == 1:
        print_usage()
    else:
        if sys.argv[1] == "get" and sys.argv[2] in version_convert:
            lines = read_version()
            index = version_convert[sys.argv[2]]
            print(lines[index])
        elif sys.argv[1] == "increase" and sys.argv[2] in version_convert:
            lines = read_version()
            index  = version_convert[sys.argv[2]]
            value = int(lines[index])
            value += 1
            lines[index] = str(value)
            write_version(lines)
        else:
            print("bad input")
            print_usage()
    
        

if __name__ == "__main__":
    program()

    