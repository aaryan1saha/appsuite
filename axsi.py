#_____________________________________________________________________________________UI___5v1__________________________________________________________________________________________
from tkinter import *
import math
import tkinter
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import os

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
#___________________________________________________________________________________SIMPLE INTEREST___________________________________________________________________________________

def si():
                                                                                    #COLOR CHOICE
            choice=choose()
            cback="black"
            ctext="white"
            cfile="sky blue"
            cotxt="white"
            if choice==1:
                    cback="black"
                    ctext="white"
                    cfile="tomato"
                    cotxt="midnight blue"
            elif choice==2:
                    cback="sky blue"
                    ctext="white"
                    cfile="black"
                    cotxt="midnight blue"
            elif choice==3:
                    cback="tomato"
                    ctext="white"
                    cfile="midnight blue"
                    cotxt="black"
            elif choice==4:
                    cback="gold"
                    ctext="white"
                    cfile="midnight blue"
                    cotxt="midnight blue"
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
                    simpleint()

                                                                                    #FUNCTIONS

            def principal():
                global operator
                pra=float(ra.get())
                pti=float(ti.get())
                psi=float(si.get())
                ppr=psi*100/(pra*pti)
                pr.set(ppr)
            def rate():
                global operator
                ppr=float(pr.get())
                pti=float(ti.get())
                psi=float(si.get())
                pra=psi*100/(ppr*pti)
                ra.set(pra)
            def time():
                global operator
                pra=float(ra.get())
                ppr=float(pr.get())
                psi=float(si.get())
                pti=psi*100/(pra*ppr)
                ti.set(pti)
            def simple():
                global operator
                pra=float(ra.get())
                pti=float(ti.get())
                ppr=float(pr.get())
                psi=(pra*pti*ppr)/100
                si.set(psi)
            def total():
                global operator
                pra=float(ra.get())
                pti=float(ti.get())
                ppr=float(pr.get())
                psi=(pra*pti*ppr)/100
                pto=psi+ppr
                to.set(pto)
            def comp():
                global operator
                ppr=float(pr.get())
                pra=float(ra.get())
                pti=float(ti.get())
                pncc=str(nc.get())
                panc=1
                if pncc=="ANUALLY":
                    panc=1
                if pncc=="SEMI-ANUALLY":
                    panc=2
                if pncc=="QUARTERLY":
                    panc=3
                if pncc=="MONTHLY":
                    panc=12
                pci=ppr*(1+pra/panc)**(panc*pti)
                ci.set(pci)

                                                                                    #INITIALISATION

            interest= Tk()
            pr=StringVar()
            ra=StringVar()
            ti=StringVar()
            to=StringVar()
            si=StringVar()
            ci=StringVar()
            nc=StringVar()
            nc.set("YEARLY")

            interest.title('simple interest')
            interest.configure(background=cback)

                                                                                    #AUTHOR AND HELP

            def clear():
                    global operator
                    pr.set("")
                    ra.set("")
                    ti.set("")
                    si.set("")
                    to.set("")
                    ci.set("")
                    nc.set("")

            def aut():
                    messagebox.showinfo("AUTHOR","hey!!!  i am created by AARYAN SAHA")

            def help1():
                    messagebox.showinfo("HELP","THIS IS A SIMPLE INTEREST CALCULATOR\n\n\n\nPLEASE CLICK ON THE BUTTONS WHOSE VALUE YOU WANNA EVALUATE.\n")

            def intmain():
                interest.destroy()
                import main
                main.main()
                return

                                                                                    #MENU INITIALISATION

            menu=Menu(interest)
            interest.config(menu=menu)
            menu.configure(background=cfile,fg=ctext)

                                                                                        #MAIN MENU

            subMenu= Menu(menu)
            subMenu.configure(background=cback,fg=ctext)
            menu.add_cascade(label="file",menu=subMenu)
            subMenu.add_command(label="main menu",command=intmain)
            subMenu.add_command(label="reset",command=clear)
            subMenu.add_command(label="author",command=aut)
            subMenu.add_command(label="help",command=help1)
            subMenu.add_command(label="exit",command=quit)

                                                                                        #ENTRY MENU

            p=Entry(interest,bd=4,width=12,font=('Bold and Compact',30,'bold'),highlightthickness=0,textvariable=pr,fg=cotxt,insertwidth=3,justify='center')
            r=Entry(interest,bd=4,width=12,font=('Bold and Compact',30,'bold'),highlightthickness=0,textvariable=ra,fg=cotxt,insertwidth=3,justify='center')
            t=Entry(interest,bd=4,width=12,font=('Bold and Compact',30,'bold'),highlightthickness=0,textvariable=ti,fg=cotxt,insertwidth=3,justify='center')
            s=Entry(interest,bd=4,width=12,font=('Bold and Compact',30,'bold'),highlightthickness=0,textvariable=si,fg=cotxt,insertwidth=3,justify='center')
            tot=Entry(interest,bd=4,width=12,font=('Bold and Compact',30,'bold'),highlightthickness=0,textvariable=to,fg=cotxt,insertwidth=3,justify='center')
            cmb=Entry(interest,bd=4,width=12,font=('Bold and Compact',30,'bold'),highlightthickness=0,textvariable=ci,fg=cotxt,insertwidth=3,justify='center')
            anc=OptionMenu(interest,nc,"ANUALLY","SEMI-ANUALLY","QUARTERLY","MONTHLY").grid(row=6,column=1)

                                                                                        #BUTTONS MENU

            button0 = Button(interest,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="PRINCIPAL",fg=ctext,command=principal)
            button1 = Button(interest,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="RATE",fg=ctext,command=rate)
            button2 = Button(interest,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="TIME",fg=ctext,command=time)
            button3 = Button(interest,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="S.I.",fg=ctext,command=simple)
            button4 = Button(interest,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="TOTAL",fg=ctext,command=total)
            button5 = Button(interest,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="COMPUND",fg=ctext,command=comp)
            button6 = Button(interest,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="INTERVAL",fg=ctext).grid(row=6,column=0)

            button0.grid(row=0,column=0)
            p.grid(row=0,column=1)
            button1.grid(row=1,column=0)
            r.grid(row=1,column=1)
            button2.grid(row=2,column=0)
            t.grid(row=2,column=1)
            button3.grid(row=3,column=0)
            s.grid(row=3,column=1)
            button4.grid(row=4,column=0)
            tot.grid(row=4,column=1)
            button5.grid(row=5,column=0)
            cmb.grid(row=5,column=1)

            interest.mainloop()
