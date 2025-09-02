from tkinter import*

window=Tk()
window.title("My first Calculator")

#adding the functions
def add():
    num1=eval(firstnumber.get())
    num2=eval(secondnumber.get())
    sum=num1+num2
    thirdnumber.set("Addition: "+str(sum))
def subtract():
    num1=eval(firstnumber.get())
    num2=eval(secondnumber.get())
    sub=num1-num2
    thirdnumber.set("Subtraction: "+str(sub))
def multiply():
    num1=eval(firstnumber.get())
    num2=eval(secondnumber.get())
    mul=num1*num2
    thirdnumber.set("Multiplication: "+str(mul))
def divide():
    num1=eval(firstnumber.get())
    num2=eval(secondnumber.get())
    div=num1/num2
    thirdnumber.set("Division: "+str(div))

#adding the labels
firstlabel=Label(window, text="First \nNumber")
firstlabel.grid(row=0,column=0)
secondlabel=Label(window, text="Second \nNumber")
secondlabel.grid(row=0,column=2)

#adding the entries
firstnumber=StringVar()
firstentry=Entry(window, width=8, textvariable=firstnumber)
firstentry.grid(row=1,column=0)
secondnumber=StringVar()
secondentry=Entry(window, width=8, textvariable=secondnumber)
secondentry.grid(row=1,column=2)

#adding the entry that prints the result
thirdnumber=StringVar()
thirdentry=Entry(window, state="readonly", width=20, textvariable=thirdnumber)
thirdentry.grid(row=4,column=0, columnspan=3, padx=40, pady=5)

#adding the buttons
btnadd=Button(window,text="+", width=3, command=add)
btnadd.grid(row=0,column=1,padx=15)
btnsub=Button(window,text="-", width=3, command=subtract)
btnsub.grid(row=1,column=1,padx=15)
btnmul=Button(window,text="*", width=3, command=multiply)
btnmul.grid(row=2,column=1,padx=15)
btndiv=Button(window,text="/", width=3, command=divide)
btndiv.grid(row=3,column=1,padx=15)



