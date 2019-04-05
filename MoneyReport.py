import sys
from tkinter import *
import decimal
def sav_Report():
    ex1_info = nContent1.get()
    ex2_info = nContent2.get()
    ex3_info = nContent3.get()
    ex4_info = nContent4.get()
    ex5_info = nContent5.get()
    inc_info = nContent6.get()
    if inc_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if ex1_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if ex2_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if ex3_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if ex4_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if ex5_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    eMonthly = ex1_info+ ex2_info + ex3_info + ex4_info + ex5_info
    eWeekly = eMonthly // 2.0
    iMonthly = inc_info - eMonthly
    iWeekly = iMonthly//2.0

    eMonthly = round(eMonthly,2)
    eWeekly = round(eWeekly,2)
    iMonthly = round(iMonthly,2)
    iWeekly = round(iWeekly,2)

    eWeekly = str(eWeekly)
    eMonthly = str(eMonthly)
    iMonthly = str(iMonthly)
    iWeekly = str(iWeekly)
    print("Monthly expense total: ",eMonthly)
    print("Biweekly expenses: ",eWeekly)
    print("Monthly leftover funds: ",iMonthly)
    print("Weekly leftover funds: ",iWeekly)

    file = open("expenditure.txt", "w")
    file.writelines("Monthly expenditure:$")
    file.write(eMonthly)
    file.writelines("\nBiweekly expenditure:$")
    file.write(eWeekly)
    file.writelines("\nMonthly Leftover:$")
    file.write(iMonthly)
    file.writelines("\nBiweekly Leftover:$")
    file.write(iWeekly)
    file.close()
    print("saved")

#Gui Setup
root = Tk()
root.geometry('500x500')
root.title("Money Management Report")
#Labels
tLabel = Label(root, text = "Enter in the value of what you're paying for and your income: \ntakes your income and accounts for your expenses",bg="grey", width = "500", height = "2")
tLabel.pack()

Label(root, text="Monthly Income:" ).place( x= 15, y = 70)
Label(root, text="Expense 1:" ).place( x=15, y = 120)
Label(root, text="Expense 2:" ).place( x=15, y = 170)
Label(root, text="Expense 3:" ).place( x=15, y = 220)
Label(root, text="Expense 4:" ).place( x=15, y = 270)
Label(root, text="Expense 5:" ).place( x=15, y = 320)
nContent1 = DoubleVar("")
nContent2 = DoubleVar("")
nContent3 = DoubleVar("")
nContent4 = DoubleVar("")
nContent5 = DoubleVar("")
nContent6 = DoubleVar("")
exp1 = Entry(text= nContent1).place( x=15, y = 140)
exp2 = Entry(text= nContent2).place( x=15, y = 190)
exp3 = Entry(text= nContent3).place( x=15, y = 240)
exp4 = Entry(text= nContent4).place( x=15, y = 290)
exp5 = Entry(text= nContent5).place( x=15, y = 340)
inc1 = Entry(text= nContent6).place( x=15, y = 90)
_Results = Label(root, text ="Results:\n")
_Results.place(x= 250, y= 115)
#OutputField
wDisplay= ""
wWindow = Label(root, text =wDisplay, bg="white")
wWindow.place(x= 145, y= 175)

mDisplay= ""
mWindow = Label(root, text =mDisplay, bg="white")
mWindow.place(x= 145, y= 145)

mLDisplay= ""
mLeftover = Label(root, text =mLDisplay, bg="white")
mLeftover.place(x= 275, y= 145)

wLDisplay= ""
wLeftover = Label(root, text =wLDisplay, bg="white")
wLeftover.place(x= 275, y= 175)

def menu_Report():
    exp1_info = nContent1.get()
    exp2_info =nContent2.get()
    exp3_info =nContent3.get()
    exp4_info =nContent4.get()
    exp5_info =nContent5.get()
    inc1_info =nContent6.get()
    if inc1_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if exp1_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if exp2_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if exp3_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if exp4_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError
    if exp5_info < 0:
        negError = ValueError("We dont count,money you dont have")
        raise negError

    e2Monthly = exp1_info + exp2_info + exp3_info + exp4_info + exp5_info
    e2Weekly = e2Monthly/2.0
    i2Monthly = inc1_info- e2Monthly
    i2Weekly = i2Monthly/2.0

    e2Monthly = round(e2Monthly, 2)
    e2Weekly = round(e2Weekly, 2)
    i2Monthly = round(i2Monthly, 2)
    i2Weekly = round(i2Weekly, 2)



    i2Monthly =str(i2Monthly)
    i2Weekly = str(i2Weekly)
    e2Weekly = str(e2Weekly)
    e2Monthly = str(e2Monthly)
    mLDisplay = ("Leftover amount month: "+i2Monthly)
    wLDisplay = ("Leftover amount biweekly: "+i2Weekly)
    mDisplay = ("Monthly total: "+e2Monthly)
    wDisplay = ("Biweekly total: "+e2Weekly)


    mWindow.config(text=mDisplay)
    wWindow.config(text=wDisplay)
    wLeftover.config(text=wLDisplay)
    mLeftover.config(text=mLDisplay)
    print("Working")


#InputFields
pButton = Button(root, text = "Print Report", width = 10, command = sav_Report)
pButton.place(x = 250, y =400)

eButton = Button(root, text = "Get Report", width = 10, command =menu_Report)
eButton.place(x = 165, y =400)

root.resizable(width=FALSE, height=FALSE)
root.mainloop()