#### File malipulation program ####

####imports####
import sys

def main():
    x=init()
    file_name=x[0]
    separate_file_flag=x[1]
    sf_Flag=separate_file_flag
    busy_spin()
    x=file_open(file_name,sf_Flag)
    file_name=x[0]
    busy_spin()
    file_read(file_name)
    close()

def init():
    print("Note that all files generated and used are .txt files.")
    print("File create module start(along with config).")
    file_create=input("Do you want to create a file?Y/N\n---->")
    if file_create=="Y":
        file_name=input("File name?\n---->")
        file_name=str(file_name)+'.txt'
        try:
            file=open(str(file_name),"x")   ###x mode with open() attempts to create a file
            print("File "+str(file_name)+" sucessfully created.")
            print("Now closing file.")
            file.close()
        except FileExistsError:             ###if this error is thrown , we know that the file already exists
            print("File "+str(file_name)+" alredy exists.")
            print("Using given file name as target file.")
        separate_file=input("Do you want to open a separte file?Y/N\n---->")
        if separate_file!="Y":              ###avoid issues with flags...
            separate_file="N"
    else:
        separate_file="N"
        file_name=input("Name of file to open?\n---->")
    print("File create module end.\n----------------")
    return(separate_file,file_name)

def file_open(arg_1,arg_2):
    if arg_1=="Y":
        new_file_name=input("Name of file to open?\n---->")
        file_name=new_file_name
    else:
        file_name=arg_2
    print("File open module start")
    print("Attempting to open file "+str(file_name))
    try:
        file=open(file_name)
        print("Sucessfully found and opened file "+str(file_name))
        file.close()
    except FileNotFoundError:
        print("File "+str(file_name)+" was not found.")
    print("File open module end.\n----------------")
    return(file_name)                           ###If a new file name was selected
                                                ###;this will pass the new file name back
                                                ###,else the original is sent
def file_read(arg_1):
    print("File read module start.")
    file_name=arg_1
    file=open(file_name,"r+")           ####may need error condition for when file may not be read(eg. security or acl)####
    initial_offset=input("Initial offest?\n---->")
    final_offset=input("Final offset(note that this is measured from the start of the file)?\n----)")
    text = file.read().strip().split()
    size = sum(len(word) for word in text)
    type_check_init_offset="N"
    type_check_final_offset="N"
    checks_passed="N"
    try:
        initial_offset=int(initial_offset)
        type_check_init_offset="Y"
    except:
        print("Initial offset should be a postive integer")
    if initial_offset<0:                                    #####WARN: all checks are assuming that 0 means the start of a file#####
        type_check_init_offset="N"
        print("Initial offset should be a postive integer")
    try:
        final_offset=int(final_offset)
        type_check_final_offset="Y"
    except:
        type_check_final_offset="N"
        print("Final offset should be a postive integer")
    if final_offset<0:
        type_check_final_offset="N"
        print("Final offset should be a postive integer")
    if type_check_init_offset=="N" or type_check_final_offset=="N":
        print("Defaulting to full file")
        initial_offset=0
        final_offset=size-1
        checks_passed="Y"
    if checks_passed!="Y":
        if initial_offset>size or final_offset>size:
            print("Both initial and final offset may not be more than the maxinum amount of characters in the file.")
            print("Defaulting to reading full file.")
            initial_offset=0
            final_offset=size-1
        else:
            checks_passed="Y"
    file.seek(initial_offset)
    file.seek(final_offset-initial_offset,1)
    data=file.read()
    print("Data is")
    print(str(data))
    file.close()
    print("File read module end.\n----------------")

def file_add(arg_1):            ###TO DO###
    print("File append module start.")
    file_name=arg_1
    shift=input("shift?(in characters)")
    file=open(file_name,"w+")
    text = file.read().strip().split()
    size = sum(len(word) for word in text)
    try:
        shift=int(shift)
    except:
        print("The offset is not an integer.\nDefaulting to a offset of 0.")
        shift=0
    if shift+1>size:
        print("Defaulting")
        shift=0
    data=input("Data to write?\n---->")
    
    quit()      ###replace with something else

def busy_spin():
    leave="N"                   ###replace naive implentation later
    while leave!="Y":
        leave=input("Procede?Y/N\n---->")
    

def close():
    close="NO"
    while close!="quit":
        close=input("Enter quit to exit.\n---->")
    sys.exit
    
if 1==1:
    main()
