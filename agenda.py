import time

def print_agenda(agenda):
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

def edit_class(agenda):
    pass
def reset(agenda):
    pass
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

def set_hw():
    with open("agenda", "r") as r:
        r_ad = r.read()
    if r_ad == "":
        for x in r_class:
            with open("agenda", "a") as f:
                myAgenda = input("Enter homework class for " + x + ": ")
                f.write(myAgenda)
                f.write("\n")

set_classes()

with open("classes", "r") as r:
    r_class = r.readlines()
    r_class = [sub[ : -1] for sub in r_class]
    
    
set_hw()

with open("agenda", "r") as r:
    r_ad = r.readlines()
    r_ad = [sub[:-1] for sub in r_ad]

agenda = []
for x in range(len(r_class)):
    agenda.append([r_class[x], r_ad[x]])

print("Online Agenda Book: By Andrew Wang")
while(True):
    print("")
    print("========")
    print_agenda(agenda)
    print("")
    print("[0] = edit homework")
    print("[1] = edit class")
    print("[2] = reset everything")
    print("[3] = exit")
    inp = input("Select number: ")

    if inp == "0":
        print("Editing homework...")
        time.sleep(1)
        print("")
        edit_hw(agenda)
    elif inp == "1":
        print("Editing class...")
        time.sleep(1)
        print("")
        edit_class(agenda)
    elif inp == "2":
        #have yes or no option
        reset(agenda)
    elif inp == "3":
        print("Exiting program...")
        time.sleep(1)
        print("")
        break
    else:
        print("Invalid number")
        print("")
print("Thank you!")
time.sleep(5)
