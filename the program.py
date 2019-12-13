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
    file_name=x     #scince out put is not a list or tuple, we can directly assign the name over
    busy_spin()
    file_read(file_name)
    busy_spin()
    file_append(file_name)
    busy_spin()
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
        separate_file=input("Do you want to open a separate file?Y/N\n---->")
        if separate_file!="Y":              ###avoid issues with flags...
            separate_file="N"
    else:
        separate_file="N"
        print("Aborting file creation.")
        file_name=input("Name of file to open?\n---->")
        file_name=str(file_name)+'.txt'
    print("File create module end.\n----------------")
    return(separate_file,file_name)

def file_open(arg_1,arg_2):
    if arg_1=="Y":
        new_file_name=input("Name of file to open?\n---->")
        file_name=str(new_file_name)+".txt"
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
    final_offset=input("Final offset(note that this is measured from the start of the file)?\n---->")
    text = file.read().strip().split()
    size = sum(len(word) for word in text)
    type_check_init_offset="N"
    type_check_final_offset="N"
    checks_passed="N"
    try:                                    ####refactor checks into separate function...( check()?) and needs to be able to handle str input
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
        if final_offset<0:      #handle a null file(size=0)
            final_offset=0
        checks_passed="Y"
    if checks_passed!="Y":
        if initial_offset>size or final_offset>size:
            print("Both initial and final offset may not be more than the maxinum amount of characters in the file.")
            print("Defaulting to reading full file.")
            initial_offset=0
            final_offset=size-1
            if final_offset<0:
                    final_offset=0
        else:
            if final_offset<initial_offset:
                print("Defaulting to full file")
                initial_offset=0
                final_offset=size-1
                if final_offset<0:
                    final_offset=0
    if final_offset==0:
        file.seek(initial_offset)
        data=file.read()
    else:
        file.seek(initial_offset)
        file.seek(final_offset-initial_offset,1)    ##update scince this methold does not work to read up to a limit
        data=file.read()
    if initial_offset==final_offset and initial_offset==0:
        print("The file "+str(file_name)+" is blank/empty.")    #handle null file
    else:
        print("Data is")
        print(str(data))
    file.close()
    print("File read module end.\n----------------")

def file_append(arg_1):
    print("File append module start.")
    run_module=input("Do you want to append data to the file?Y/N\n---->")
    if run_module=="Y":
        file_name=arg_1
        file=open(file_name,"a+")       #this mode starts the pointer at the end of the file always.
        data=input("Data to write?\n---->")
        file.write(data)
        print("Data appended.")
        file.seek(0)
        file_data=file.read()
        print("File is\n"+str(file_data))
        file.close()
        print("File append module end.\n----------------")
    else:
        print("Module aborted")

def file_add(arg_1):
    file_name=arg_1
    print("File write module start.")
    terminate="No"
    display_result=input("Display updated file after each write?Y/N\n---->")
    if display_result=="Y":
        display_delay=input("How many times do you want to see the updated file?(0 means always,1 means every other input)\n---->")
        if type_check(display_delay,"pos_int+0")!="Y":
            display_delay=int(dislay_delay)
        else:
            print("Defaulting to everytime.")
            display_delay=0
    if display_result=="Y":
        while terminate!="Y":
            terminate="Y"
    else:
        while terminate!="Y":
            terminate="Y"
    print("File write module end.\n----------------")

def type_check(arg_1,arg_2):
    inpt=arg_1
    data_type=arg_2
    dt=data_type
    match="M"
    if dt=="pos_int":
        try:
            inpt=int(inpt)
            if inpt>0:
                match="Y"
            else:
                macth="N"
        except:
            match="N" 
    elif dt=="neg_int":
        try:
            inpt=int(inpt)
            if inpt<0:
                match="Y"
            else:
                macth="N"
        except:
            match="N"
    elif dt=="int":
        try:
            inpt=int(inpt)
            match="Y"
        except:
            match="N"
    elif dt=="pos_int+0":
        try:
            inpt=int(inpt)
            if inpt>=0:
                match="Y"
            else:
                macth="N"
        except:
            match="N"
    elif dt=="neg_int+0":
        try:
            inpt=int(inpt)
            if inpt<=0:
                match="Y"
            else:
                macth="N"
        except:
            match="N"
    elif dt=="str":
        if type(inpt)==type("str"):
            match="Y"
        else:
            match="N"
    return(match)

def busy_spin():
    leave="N"                   ###replace naive implentation later
    while leave!="Y":
        leave=input("Procede?Y/N\n---->")
    

def close():
    close="NO"
    print("Program finished execution.")
    while close!="quit":
        close=input("Enter quit to exit.\n---->")
    sys.exit
    
if 1==1:
    main()
