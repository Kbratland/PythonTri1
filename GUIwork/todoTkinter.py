from tkinter import *
from shelve import *

root = Tk()
root.title("TODO List")
num = 0

name_var = StringVar()
num_var = IntVar()

listbox = Listbox(root, height=num, width=40)


def submit(event):
    global listbox
    global num
    name = name_var.get()
    name_var.set("")
    if (name != ""):
        listbox.insert(num, f"{num + 1}. " + name)
        num += 1


def changeEntry():
    global listbox
    global num
    changeNum = num_var.get() - 1
    name = name_var.get()
    if (name != ""):
        listbox.insert(changeNum, f"{changeNum + 1}. " + name)
        listbox.delete(changeNum + 1)


def delete():
    global num
    listbox.delete(ANCHOR)
    if num > 0:
        num -= 1
        
def quitList(listBin):
    global num
    listFile = open("listFile")
    tempList = []
    for lp in range(0,num):
        tempList.append(listBin.get(lp))
    print(tempList)
    listFile["numHold"] = num
    listFile["listHold"] = tempList
    listFile.close()
    exit()
    
def loadList(listBin):
    global num
    try:
        listFile = open("listFile")
        tempList2 = listFile["listHold"]
        num = listFile["numHold"]
        print(tempList2)
        for lp in range(len(tempList2)-1):
            listBin.insert(lp,tempList2[lp])
        listFile.close()
    except:
        pass

loadList(listbox)



name_label = Label(root, text=' Add to Todo List',font=('calibre', 20, 'bold'))

name_entry = Entry(root, textvariable=name_var, font=('calibre', 12, 'normal'), bg="black")

num_label = Label(root, text='Edit Index:', font=('calibre', 20, 'bold'))

num_entry = Entry(root, textvariable=num_var, font=('calibre', 12, 'normal'), bg="black")

root.bind('<Return>', submit)

sub_btn = Button(root, text='Enter', command=lambda: submit(1))

sub_btn3 = Button(root, text="Edit", command=changeEntry)

sub_btn2 = Button(root, text='Remove Selected', command=delete)

exitButton = Button(root,text = "Save and quit",command=lambda: quitList(listbox))

name_label.grid(row=0, column=0)
name_entry.grid(row=1, column=0)
sub_btn.grid(row=2, column=0)
sub_btn2.grid(row=3, column=0)
num_label.grid(row=4, column=0)
num_entry.grid(row=5, column=0)
sub_btn3.grid(row=6, column=0)
listbox.grid(row=7, column=0)
exitButton.grid(row=8,column=0)

root.mainloop()