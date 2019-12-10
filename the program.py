#### File malipulation program ####

####imports####
import sys

def main():
    x=init()
    file_open(x[0],x[1])
    close()

def init():
    print("Note that all files generated and used are .txt files.")
    file_create=input("Do you want to create a file?Y/N\n---->")
    if file_create=="Y":
        file_name=input("File name?\n---->")
        file_name=str(file_name)+'.txt'
        file_exist="Y"
        try:
            open(str(file_name))
        except FileNotFoundError:
            open(str(file_name),"w+")
            file_exist="N"
            print("File "+str(file_name)+" sucessfully created.")
        if file_exist=="Y":
            print("File "+str(file_name)+" alredy exists.")
            print("Using given file name as target file.")
            separate_file="N"
        else:
            separate_file=input("Do you want to open another file?Y/N\n---->")
    else:
        separate_file="N"
        file_name=input("Name of file to open?\n---->")
    return(separate_file,file_name)

def file_open(arg_1,arg_2):
    if arg_1=="Y":
        new_file_name=input("Name of file to open?\n---->")
        file_name=new_file_name
    else:
        file_name=arg_2
    print("Attempting to open file "+str(file_name))
    try:
        open(file_name)
        print("Sucessfully found and opened file "+str(file_name))
    except FileNotFoundError:
        print("File "+str(file_name)+" was not found.")

def file_add(arg_1):
    close()

def close():
    close="NO"
    while close!="quit":
        close=input("Enter quit to exit.\n---->")
    sys.exit
    
if 1==1:
    main()
