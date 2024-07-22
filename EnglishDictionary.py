from tkinter import * 
from PIL import Image,ImageTk
from PyDictionary import PyDictionary 

window=Tk()
window.title("ENGLISH DICTIONARY")
dictionary=PyDictionary()


window.geometry('2000x1000+1+1')#setting width and height parameter
pi=PhotoImage(file='Backgound.png')
bglabel=Label(window,image=pi)#placing image with help of label
bglabel.place(x=0,y=0)
#creating GUI
ta=Text(window,width=90,height=10,font=('Times New Roman',12,'bold',),foreground='Blue')
ta.place(x=520,y=700)

enterword=Label(window,text='ENGLISH DICTIONARY',font=('castellar',25,'bold',),foreground='Blue')
enterword.place(x=700,y=100)

enterword=Label(window,text='ENTER WORD',font=('castellar',25,'bold',),foreground='Blue')
enterword.place(x=800,y=200)

word=Entry(window,font=('Times New Roman',25,'bold'),foreground='Blue',justify=CENTER)
word.place(x=750,y=350)
try:
    def search():
            input = word.get()
            print(input)
            print(dictionary)
            meaning=dictionary.meaning(input)
            print(meaning)
            if (meaning == None):
                ta.delete(1.0,END)
                ta.insert(END,'Invalid Word')      
            else:
                ta.delete(1.0,END)
                ta.insert(END,meaning)
        
except Exception as e:
    print(e)
global dic1
dic1={"Pinal":"God of Child"}   
def add():
    inputw=word.get()
    mean=ta.get(1.0, "end-1c")
    dic={inputw:mean}
    global dic1
    dic1[inputw]=mean
    ta.delete(1.0,END)
    ta.insert(END,"WORD ADDED SUCCESSFULLY!!!")
    print("Added",dic1)
   
def delete():
    
    inputw=word.get()
    global dic1
    dic1.pop(inputw)
    ta.delete(1.0,END)
    ta.insert(END,"WORD DELETED SUCCESSFULLY!!!")
    print("Deleted",dic1)

def update():
    inputw=word.get()
    mean=ta.get(1.0, "end-1c")
    dic={inputw:mean}
    global dic1
    dic1.update(dic)
    ta.delete(1.0,END)
    ta.insert(END,"WORD UPDATED SUCCESSFULLY!!!")
    print("Updated",dic1)
    
def printMean():
    global dic1
    ta.delete(1.0,)
    ta.insert(END,dic1)
    
b1=Button(window,text='SEARCH MEANING',font=('castellar',15,'bold'),foreground='White',background='blue',command=lambda:search())
b1.place(x=200,y=500)

b1=Button(window,text='ADD WORD',font=('castellar',15,'bold'),foreground='White',background='blue',command=lambda:add())
b1.place(x=520,y=500)

b1=Button(window,text='UPDATE WORD',font=('castellar',15,'bold'),foreground='White',background='blue',command=lambda:update())
b1.place(x=740,y=500)

b1=Button(window,text='DELETE WORD',font=('castellar',15,'bold'),foreground='White',background='blue',command=lambda:delete())
b1.place(x=1010,y=500)

b1=Button(window,text='PRINT LIST',font=('castellar',15,'bold'),foreground='White',background='blue',command=lambda:printMean())
b1.place(x=1270,y=500)

b1=Button(window,text='EXIT DICTIONARY',font=('castellar',15,'bold'),foreground='White',background='blue',command=window.destroy)
b1.place(x=1480,y=500)

mean=Label(window,text='MEANING',font=('castellar',25,'bold',),foreground='Blue')
mean.place(x=850,y=600)


window.mainloop()#main loop keps everything in loop
