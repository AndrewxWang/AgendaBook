import time, sys

def checkFiles():
    exceptions = 0
    try:
        with open("classes", "r") as r:
            pass
    except:
        print("No \"classes\" file was found")
        print("Creating \"classes\" file...")
        time.sleep(1)
        r = open("classes","w+")
        print("\"classes\" was created!")
        exceptions+=1
    print("")
    try:
        with open("agenda", "r") as r:
            pass
    except:
        print("No \"agenda\" file was found")
        print("Creating \"agenda\" file...")
        time.sleep(1)
        r = open("agenda","w+")
        print("\"agenda\" was created!")
        exceptions+=1
    print("")
    if (exceptions > 0):
        print("Restart program to use")
        time.sleep(5)
        sys.exit()

def make_agenda():
    with open("classes", "r") as r:
        r_class = r.readlines()
        r_class = [sub[ : -1] for sub in r_class]
        set_hw(r_class)
    with open("agenda", "r") as r:
        r_ad = r.readlines()
        r_ad = [sub[:-1] for sub in r_ad]
    agenda = []
    for x in range(len(r_class)):
        agenda.append([r_class[x], r_ad[x]])
    return agenda

def print_agenda(agenda):
    print("")
    print("Agenda:")
    print("========")
    for x in agenda:
        for y in range(len(agenda[1])):
            print(x[y] + " - ", end="")
        print("")
        print("========")

def edit_hw(agenda):
    ag = [agenda[x][0].lower() for x in range(len(agenda))]

    r_class = input("Enter the class of the homework you would like to edit: ")
    if str(r_class).lower()in ag:
        print("Class found!")
        r_edit = input("Enter new homework: ")
        count = ag.index(r_class.lower())
        agenda[count][1] = r_edit
        print(count)
        with open("agenda", "r") as r:
            r_agenda = r.readlines()
            r_agenda[count] = r_edit + "\n"

        with open("agenda", "w") as w:
            w_agenda = w.writelines(r_agenda)
    else:
        print("Class was not found.")

def reset():
    with open ("classes", "r+") as r:
        r.truncate(0)
        r.close()
    with open("agenda", "r+") as f:
        f.truncate(0)
        f.close()
    print("Everything has been reset.")
    print("Restart the program to use.")
    time.sleep(5)
    sys.exit()
        

def set_classes():
    with open("classes", "r") as r:
        read = r.read()
    if read == "":
        while(True):
            with open("classes", "a") as f:
                myClass = input("Enter class. Type \"stop\" to stop: ")
                if myClass.lower() == "stop":
                    break
                f.write(myClass)
                f.write("\n")

def set_hw(r_class):
    with open("agenda", "r") as r:
        r_ad = r.read()
    if r_ad == "":
        for x in r_class:
            with open("agenda", "a") as f:
                myAgenda = input("Enter homework class for " + x + ": ")
                f.write(myAgenda)
                f.write("\n")

checkFiles()
set_classes()
agenda = make_agenda()

print("Online Agenda Book: By Andrew Wang")
while(True):
    print("")
    print("========")
    print_agenda(agenda)
    print("")
    print("[0] = edit homework")
    print("[1] = reset everything")
    print("[2] = exit")
    inp = input("Select number: ")

    if inp == "0":
        print("Editing homework...")
        print("")
        edit_hw(agenda)
    elif inp == "1":
        inp2 = input("Are you sure you want to reset everything? (y/n): ")
        if inp2.lower() == "y":
            reset()
        print("Nothing was changed.")
    elif inp == "2":
        print("Exiting program...")
        time.sleep(1)
        print("")
        break
    else:
        print("Invalid number")
        print("")
print("Thank you!")
time.sleep(5)
