#_____________________________________________________________________________________UI___5v1__________________________________________________________________________________________
from tkinter import *
import math
import tkinter
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import os
#________________________________________________________________________________BOOKS INITIALISATION_________________________________________________________________________________

books=np.array([["","","",""]])
quan=0
kk=0
xy=4
xyz=0
cback="black"
ctext="white"
cfile="sky blue"
cotxt="white"
#____________________________________________________________________________CHOICE MENU FOR COLOR SELECTION___________________________________________________________________________

def choose():
    chz=Tk()
    chz.configure(background="tomato")
    def choi(num):
        global x
        if num==6:
            x=6
            chz.destroy()
        else:
            x=num
            chz.destroy()
        return x
    button0 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="    DARK      ",fg="white",command=lambda:choi(1)).grid(row=0,column=0)
    button1 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="    LIGHT     ",fg="white",command=lambda:choi(2)).grid(row=1,column=0)
    button2 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="  TOMATO   ",fg="white",command=lambda:choi(3)).grid(row=2,column=0)
    button3 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="     GOLD     ",fg="white",command=lambda:choi(4)).grid(row=3,column=0)
    button4 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="MAIN MENU",fg="white",command=lambda:choi(5)).grid(row=4,column=0)
    button5 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="      EXIT     ",fg="white",command=lambda:choi(6)).grid(row=5,column=0)
    chz.mainloop()
    return x
    Tk.quit()
#____________________________________________________________________________________________________________________________________________________________________________________
#__________________________________________________________________________________________BOOKSHELF_______________________________________________________________________________________________

def bs():
            cback="black"
            ctext="white"
            cfile="sky blue"
            cotxt="white"
            global books,quan,kk

                                                                                           #COLOR CHOICES
            choice=choose()

            if choice==1:
                cback="black"
                ctext="white"
                cfile="tomato"
                cotxt="white"
            elif choice==2:
                cback="orange"
                ctext="white"
                cfile="midnight blue"
                cotxt="white"
            elif choice==3:
                cback="tomato"
                ctext="white"
                cfile="midnight blue"
                cotxt="white"
            elif choice==4:
                cback="gold"
                ctext="white"
                cfile="midnight blue"
                cotxt="white"
            elif choice==5:
                import main
                main.main()
            elif choice==6:
                if os.path.isfile('awsui.py'):
                    os.remove('awsui.py')
                if os.path.isfile('log.txt'):
                    os.remove('log.txt')
                if os.path.isfile('axsi.py'):
                    os.remove('axsi.py')
                if os.path.isfile('axcr.py'):
                    os.remove('axcr.py')
                if os.path.isfile('axbs.py'):
                    os.remove('axbs.py')
                if os.path.isfile('axsc.py'):
                    os.remove('axsc.py')
                exit()
            else:
                print("\nWRONG CHOICE\n")
                bookshelf()

                                                                                        #FRAME

            root = Tk()
            frame=Frame(root)
            frame.configure(background=cback)
            frame.pack()
            tframe=Frame(root)
            tframe.configure(background=cfile)
            tframe.pack()

            root.title('BOOK STORE')
            root.configure(background=cback)
            operator=""
            rev=StringVar()
            num1=StringVar()

            bookno=StringVar()
            booknm=StringVar()
            bookpr=StringVar()
            bookau=StringVar()

                                                                                        #FUNCTIONS

            def disp(x):
                global books,quan,kk

                ds=Tk()
                ds.title('SEARCH RESULT')
                ds.configure(background=cback)

                def delete(x):
                    global books,quan,kk
                    books=np.delete(books,(x),axis=0)
                    quan=quan-1
                    ds.destroy()
                    if kk==1:
                        print(kk)
                        kk=0
                        showt()
                        return

                def upgdr(x):
                    global books,kk
                    bookno.set(books[x][0])
                    booknm.set(books[x][1])
                    bookpr.set(books[x][2])
                    bookau.set(books[x][3])
                    kk=0
                    p=0
                    delete(x)
                    ds.destroy
                    return


                bknm=Label(ds,font=('Courier New Bold',15,'bold'),text='BOOK NAME:',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=1,column=0)
                bknm1=Label(ds,font=('Courier New Bold',15,'bold'),text=books[x][1],justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=1,column=1)
                bksn=Label(ds,font=('Courier New Bold',15,'bold'),text='SERIAL NUMBER:',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=0,column=0)
                bksn1=Label(ds,font=('Courier New Bold',15,'bold'),text=books[x][0],justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=0,column=1)
                bkpr=Label(ds,font=('Courier New Bold',15,'bold'),text='PRICE:',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=2,column=0)
                bkpr1=Label(ds,font=('Courier New Bold',15,'bold'),text=books[x][2],justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=2,column=1)
                bkau=Label(ds,font=('Courier New Bold',15,'bold'),text='AUTHOR:',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=3,column=0)
                bkau1=Label(ds,font=('Courier New Bold',15,'bold'),text=books[x][3],justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=3,column=1)

                dele=Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="DELETE",fg=ctext,command=lambda:delete(x)).grid(row=4,column=0)
                upgr=Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="UPGRADE",fg=ctext,command=lambda:upgdr(x)).grid(row=4,column=1)

                ds.mainloop()
                return

            def add():
                global books,quan
                quan=quan+1
                books=np.append(books,[[0,"",0,""]],axis=0)
                books[quan][0]=int(bookno.get())
                books[quan][3]=str(bookau.get())
                books[quan][2]=int(bookpr.get())
                books[quan][1]=str(booknm.get())
                clear()

                                                                                    #SH0W MENU

            def showt():

                global books,quan,kk
                ds=Tk()
                ds.title('SEARCH RESULT')
                ds.configure(background=cback)

                def lkno():
                    global books,quan,kk
                    a=lsn.curselection()
                    p=books[a][0]
                    for i in range(1,quan+1):
                        if books[i][0]==p:
                            kk=1
                            ds.destroy()
                            disp(i)
                            return

                def lknm():
                    global books,quan,kk
                    a=lnm.curselection()
                    p=books[a][1]
                    for i in range(1,quan+1):
                        if books[i][1]==p:
                            kk=1
                            ds.destroy()
                            disp(i)
                            return

                def lkpr():
                    global books,quan,kk
                    a=lpr.curselection()
                    p=books[a][2]
                    for i in range(1,quan+1):
                        if books[i][2]==p:
                            kk=1
                            ds.destroy()
                            disp(i)
                            return

                def lkau():
                    global books,quan,kk
                    a=lau.curselection()
                    p=books[a][3]
                    for i in range(1,quan+1):
                        if books[i][3]==p:
                            kk=1
                            ds.destroy()
                            disp(i)
                            return

                def lkdno():
                    global books,quan
                    a=lsn.curselection()
                    p=books[a][0]
                    for i in range(1,quan+1):
                        if books[i][0]==p:
                            books=np.delete(books,(i),axis=0)
                            quan=quan-1
                            ds.destroy()
                            showt()

                def lkdnm():
                    global books,quan
                    a=lnm.curselection()
                    p=books[a][1]
                    for i in range(1,quan+1):
                        if books[i][1]==p:
                            books=np.delete(books,(i),axis=0)
                            quan=quan-1
                            ds.destroy()
                            showt()

                def lkdpr():
                    global books,quan
                    a=lpr.curselection()
                    p=books[a][2]
                    for i in range(1,quan+1):
                        if books[i][2]==p:
                            books=np.delete(books,(i),axis=0)
                            quan=quan-1
                            ds.destroy()
                            showt()

                def lkdau():
                    global books,quan
                    a=lau.curselection()
                    p=books[a][3]
                    for i in range(1,quan+1):
                        if books[i][3]==p:
                            books=np.delete(books,(i),axis=0)
                            quan=quan-1
                            ds.destroy()
                            showt()

                lsn=Listbox(ds,bg=cback,fg=ctext,width=20,selectmode=EXTENDED)
                lsn.grid(row=1,column=0)
                lsn.insert(1,"SERIAL NUMBER")
                for i in range(1,quan+1):
                    lsn.insert(i,str(books[i][0]))

                lnm=Listbox(ds,bg=cback,fg=ctext,width=20,selectmode=EXTENDED)
                lnm.grid(row=1,column=1)
                lnm.insert(1,"BOOK NAME")
                for i in range(1,quan+1):
                    lnm.insert(i,str(books[i][1]))

                lpr=Listbox(ds,bg=cback,fg=ctext,width=20,selectmode=EXTENDED)
                lpr.grid(row=1,column=2)
                lpr.insert(1,"PRICE")
                for i in range(1,quan+1):
                    lpr.insert(i,str(books[i][2]))

                lau=Listbox(ds,bg=cback,fg=ctext,width=20,selectmode=EXTENDED)
                lau.grid(row=1,column=3)
                lau.insert(1,"AUTHOR")
                for i in range(1,quan+1):
                    lau.insert(i,str(books[i][3]))

                buttonno = Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="SELECT",fg=ctext,command=lkno).grid(row=2,column=0)
                buttonnm = Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="SELECT",fg=ctext,command=lknm).grid(row=2,column=1)
                buttonpr = Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="SELECT",fg=ctext,command=lkpr).grid(row=2,column=2)
                buttonau = Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="SELECT",fg=ctext,command=lkau).grid(row=2,column=3)
                buttonnod = Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="DELETE",fg=ctext,command=lkdno).grid(row=3,column=0)
                buttonnmd = Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="DELETE",fg=ctext,command=lkdnm).grid(row=3,column=1)
                buttonprd = Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="DELETE",fg=ctext,command=lkdpr).grid(row=3,column=2)
                buttonaud = Button(ds,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="DELETE",fg=ctext,command=lkdau).grid(row=3,column=3)

                ds.mainloop()

            def searchbno():
                x=str(bookno.get())
                for i in range(1,quan+1):
                    if books[i][0]==x:
                        disp(i)
                        return

            def searchbnm():
                x=str(booknm.get())
                for i in range(1,quan+1):
                    if books[i][1]==x:
                        disp(i)
                        return

            def searchbpr():
                x=str(bookpr.get())
                for i in range(1,quan+1):
                    if books[i][2]==x:
                        disp(i)
                        return

            def searchbau():
                x=str(bookau.get())
                for i in range(1,quan+1):
                    if books[i][3]==x:
                        disp(i)
                        return

                                                                                    #DELETE FUNCTIONS

            def delt():
                global quan,books
                for i in range(1,quan+1):
                    books=np.array([["","","",""]])
                    quan=0
                return

            def delbno():
                global quan,books
                x=str(bookno.get())
                for i in range(1,quan+1):
                    if books[i][0]==x:
                        books=np.delete(books,(i),axis=0)
                        quan=quan-1
                        return

            def delbnm():
                global quan,books
                x=str(booknm.get())
                for i in range(1,quan+1):
                    if books[i][1]==x:
                        books=np.delete(books,(i),axis=0)
                        quan=quan-1
                        return

            def delbpr():
                global quan,books
                x=str(bookpr.get())
                for i in range(1,quan+1):
                    if books[i][2]==x:
                        books=np.delete(books,(i),axis=0)
                        quan=quan-1
                        return

            def delbau():
                global quan,books
                x=str(bookau.get())
                for i in range(1,quan+1):
                    if books[i][3]==x:
                        books=np.delete(books,(i),axis=0)
                        quan=quan-1
                        return

                                                                                    #AUTHOR AND HELP
            def aut():
                messagebox.showinfo("AUTHOR","hey!!!  i am created by AARYAN SAHA")

            def help1():
                messagebox.showinfo("HELP","you can use function like search and delete\n")
            def clear():
                global operator
                bookno.set("")
                bookpr.set("")
                bookau.set("")
                booknm.set("")

            def dsmain():
                root.destroy()
                import main
                main.main()
                return


                                                                                #MENU INITIALISATION
            menu=Menu(root)
            root.config(menu=menu)
            menu.configure(background=cfile,fg=ctext,font=('Courier New Bold',10))

                                                                                    #FILE MENU

            subMenu= Menu(menu)
            subMenu.configure(background=cback,fg=ctext)
            menu.add_cascade(label="File",menu=subMenu)
            subMenu.add_command(label="main menu",command=dsmain)
            subMenu.add_command(label="reset",command=clear)
            subMenu.add_command(label="author",command=aut)
            subMenu.add_command(label="help",command=help1)
            subMenu.add_command(label="exit",command=quit)

                                                                                    #SHOW MENU

            showal= Menu(menu)
            showal.configure(background=cback,fg=ctext)
            menu.add_cascade(label="Search",menu=showal)
            showal.add_command(label="SEARCH BY SERIAL NUMBER",command=searchbno)
            showal.add_command(label="SEARCH BY BOOK NAME",command=searchbnm)
            showal.add_command(label="SEARCH BY BOOK PRICE",command=searchbpr)
            showal.add_command(label="SEARCH BY BOOK AUTHOR",command=searchbau)
            showal.add_command(label="SHOW ALL",command=showt)

                                                                                    #DELETE MENU

            dele= Menu(menu)
            dele.configure(background=cback,fg=ctext)
            menu.add_cascade(label="Delete",menu=dele)
            dele.add_command(label="DELETE BY SERIAL NUMBER",command=delbno)
            dele.add_command(label="DELETE BY BOOK NAME",command=delbnm)
            dele.add_command(label="DELETE BY BOOK PRICE",command=delbpr)
            dele.add_command(label="DELETE BY BOOK AUTHOR",command=delbau)
            dele.add_command(label="DELETE ALL",command=delt)

                                                                                    #BUTTONS MENU

            button0 = Button(frame,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="SERIAL NUMBER",fg=ctext,command=searchbno).grid(row=0,column=0)
            button1 = Button(frame,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="   BOOK NAME   ",fg=ctext,command=searchbnm).grid(row=1,column=0)
            button2 = Button(frame,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="       PRICE         ",fg=ctext,command=searchbpr).grid(row=2,column=0)
            button3 = Button(frame,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="       AUTHOR     ",fg=ctext,command=searchbau).grid(row=3,column=0)

                                                                                    #ENTRY MENU

            bkno=Entry(frame,relief='flat',width=17,bg=ctext,bd=3,highlightthickness=3,font=('Bold and Compact',25,'bold'),textvariable=bookno,fg=cfile,insertwidth=3,justify='right').grid(row=0,column=1)
            bknm=Entry(frame,relief='flat',width=17,bg=ctext,bd=3,highlightthickness=3,font=('Bold and Compact',25,'bold'),textvariable=booknm,fg=cfile,insertwidth=3,justify='right').grid(row=1,column=1)
            bkpr=Entry(frame,relief='flat',width=17,bg=ctext,bd=3,highlightthickness=3,font=('Bold and Compact',25,'bold'),textvariable=bookpr,fg=cfile,insertwidth=3,justify='right').grid(row=2,column=1)
            bkau=Entry(frame,relief='flat',width=17,bg=ctext,bd=3,highlightthickness=3,font=('Bold and Compact',25,'bold'),textvariable=bookau,fg=cfile,insertwidth=3,justify='right').grid(row=3,column=1)

            buttonadd = Button(tframe,font=('Courier New Bold',20,'bold'),padx=8,pady=10,relief='flat',bg=cfile,highlightthickness=0,justify='center',text="ADD DATA",fg=ctext,command=add).grid(row=4,column=3)
            buttonshow = Button(tframe,font=('Courier New Bold',20,'bold'),padx=8,pady=10,relief='flat',bg=cfile,highlightthickness=0,justify='center',text=" SHOW ALL",fg=ctext,command=showt).grid(row=4,column=2)
            buttondelete = Button(tframe,font=('Courier New Bold',20,'bold'),padx=8,pady=10,relief='flat',bg=cfile,highlightthickness=0,justify='center',text="DELETE ALL",fg=ctext,command=delt).grid(row=4,column=0)
            buttonreset = Button(tframe,font=('Courier New Bold',20,'bold'),padx=8,pady=10,relief='flat',bg=cfile,highlightthickness=0,justify='center',text=" RESET ",fg=ctext,command=clear).grid(row=4,column=1)


            root.mainloop()
            return

