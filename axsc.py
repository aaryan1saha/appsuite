#_____________________________________________________________________________________UI___5v1__________________________________________________________________________________________
from tkinter import *
import math
import tkinter
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import os

rev=np.array([""])
rq=-1
cback="black"
ctext="white"
cfile="sky blue"
cotxt="white"
cent="black"
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

def sc():
                                                                                        #COLOR CHOIC
            choice=choose()
            cback="black"
            ctext="white"
            cfile="sky blue"
            cotxt="white"
            cent="black"
            
            if choice==1:
                cback="black"
                ctext="white"
                cfile="tomato"
                cotxt="sky blue"
                cent="black"
            elif choice==2:
                cback="white"
                ctext="black"
                cfile="orange"
                cotxt="midnight blue"
                cent="white"
            elif choice==3:
                cback="tomato"
                ctext="white"
                cfile="midnight blue"
                cotxt="midnight blue"
                cent="white"
            elif choice==4:
                cback="gold"
                ctext="white"
                cfile="midnight blue"
                cotxt="tomato"
                cent="white"
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
                scicalculator()
            choice=6
                                                                                        #FUNCTIONS

            def fact():
                global operator
                n=int(num1.get())
                f=1
                for i in range(1,n+1):
                    f=f*i
                num1.set(f)
                operator=str(f)

            def inverse():
                global operator
                n=float(num1.get())
                if n==0:
                    f="INFINITY"
                else:
                    f=1/n
                num1.set(f)
                operator=str(f)

            def delete():
                global operator
                n=list(str(num1.get()))
                l=len(n)
                if l==0:
                    return
                del n[l-1]
                m=[str(elem) for elem in n]
                m=''.join(m)
                num1.set(m)
                operator=str(m)

            def click(num):
                global operator
                operator=str(num1.get())
                operator+=str(num)
                num1.set(operator)

            def clear():
                global operator
                operator=""
                num1.set("")

            def equals():
                global operator,rev,rq
                r=str(num1.get())
                sumup=str(eval(num1.get()))
                num1.set(sumup)
                operator=str(sumup)
                rev=np.append(rev,[str(r)])
                rev=np.append(rev,[str(sumup)])
                rq=rq+2

            def reverse():
                global operator,rev,rq
                r=rev[rq-1]
                rq=rq-1
                num1.set(r)
                operator=str(r)

            def forward():
                global operator,rev,rq
                r=rev[rq+1]
                rq=rq+1
                num1.set(r)
                operator=str(r)

                                                                                    #LOGIRITHMIC

            def log2():
                global operator
                x=float(num1.get())
                y=math.log2(x)
                num1.set(y)
                operator=str(y)

            def log():
                global operator
                x=float(num1.get())
                y=math.log(x)
                num1.set(y)
                operator=str(y)

            def log10():
                global operator
                x=float(num1.get())
                y=math.log10(x)
                num1.set(y)
                operator=str(y)

                                                                                        #GRAPHS

            def gsqrt():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(0,n+1):
                    x[i]=i
                    y[i]=i**0.5
                pl.plot(x,y,label='square root')
                pl.legend()
                pl.show()

            def glog2():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i
                    y[i]=math.log2(i)
                pl.plot(x-1,y,label='log 2')
                pl.legend()
                pl.show()

            def glog():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i
                    y[i]=math.log(i)
                pl.plot(x,y,label='log e')
                pl.legend()
                pl.show()

            def glog10():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i
                    y[i]=math.log10(i)
                pl.plot(x,y,label='log 10')
                pl.legend()
                pl.show()


            def ginverse():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i
                    y[i]=1/i
                pl.plot(x,y,label='inverse')
                pl.legend()
                pl.show()

            def gsin():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(0,n+1):
                    x[i]=i
                    y[i]=math.sin(i/57.296)
                pl.xlabel('angles')
                pl.ylabel('value')
                pl.plot(x,y,label='sin x')
                pl.legend()
                pl.show()

            def gcos():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(0,n+1):
                    x[i]=i
                    y[i]=math.cos(i/57.296)
                pl.xlabel('angles')
                pl.ylabel('value')
                pl.plot(x,y,label='cos x')
                pl.legend()
                pl.show()

            def gtan():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(0,n+1):
                    x[i]=i
                    y[i]=math.tan(i/57.296)
                pl.xlabel('angles')
                pl.ylabel('value')
                pl.plot(x,y,label='tan x')
                pl.legend()
                pl.show()

            def gcot():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i
                    y[i]=1/math.tan(i/57.296)
                pl.xlabel('angles')
                pl.ylabel('value')
                pl.plot(x,y,label='cot x')
                pl.legend()
                pl.show()

            def gcosec():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i
                    y[i]=1/math.sin(i/57.296)
                pl.xlabel('angles')
                pl.ylabel('value')
                pl.plot(x,y,label='cosec x')
                pl.legend()
                pl.show()
            def gsec():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i
                    y[i]=1/math.cos(i/57.296)
                pl.xlabel('angles')
                pl.ylabel('value')
                pl.plot(x,y,label='sec x')
                pl.legend()
                pl.show()

            def gasin():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i/100
                    y[i]=math.asin(i/100)
                pl.xlabel('value')
                pl.ylabel('angles')
                pl.plot(x,57.296*y,label='asin x')
                pl.legend()
                pl.show()
            def gacos():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(1,n+1):
                    x[i]=i/100
                    y[i]=math.acos(i/100)
                pl.xlabel('values')
                pl.ylabel('angles')
                pl.plot(x,57.296*y,label='acos x')
                pl.legend()
                pl.show()
            def gatan():
                n=int(num1.get())
                x=np.zeros(n+1)
                y=np.zeros(n+1)
                for i in range(0,n+1):
                    x[i]=i/100
                    y[i]=math.atan(i/100)
                pl.xlabel('values')
                pl.ylabel('angles')
                pl.plot(x,57.296*y,label='atan x')
                pl.legend()
                pl.show()

                                                                                    #TRIGONOMETRY

            def sin():
                global operator
                x=float(num1.get())
                y=math.sin(x)
                num1.set(y)
                operator=str(y)

            def atan():
                global operator
                x=float(num1.get())
                y=math.atan(x)
                num1.set(y)
                operator=str(y)

            def asin():
                global operator
                x=float(num1.get())
                y=math.asin(x)
                num1.set(y)
                operator=str(y)

            def cos():
                global operator
                x=float(num1.get())
                y=math.cos(x)
                num1.set(y)
                operator=str(y)

            def acos():
                global operator
                x=float(num1.get())
                y=math.acos(x)
                num1.set(y)
                operator=str(y)

            def tan():
                global operator
                x=float(num1.get())
                y=math.tan(x)
                num1.set(y)
                operator=str(y)

            def cosec():
                global operator
                x=float(num1.get())
                y=1/math.sin(x)
                num1.set(y)
                operator=str(y)

            def acot():
                global operator
                x=float(num1.get())
                y=1/math.atan(x)
                num1.set(y)
                operator=str(y)

            def acosec():
                global operator
                x=float(num1.get())
                y=1/math.asin(x)
                num1.set(y)
                operator=str(y)

            def sec():
                global operator
                x=float(num1.get())
                y=1/math.cos(x)
                num1.set(y)
                operator=str(y)

            def asec():
                global operator
                x=float(num1.get())
                y=1/math.acos(x)
                num1.set(y)
                operator=str(y)

            def cot():
                global operator
                x=float(num1.get())
                y=1/math.tan(x)
                num1.set(y)
                operator=str(y)

                                                                                        #TIME

            def m2s():
                global operator
                c=float(num1.get())
                f=c*60
                num1.set(f)
                operator=str(f)

            def h2s():
                global operator
                f=float(num1.get())
                c=f*3600
                num1.set(c)
                operator=str(c)
            def d2s():
                global operator
                c=float(num1.get())
                f=c*24*3600
                num1.set(f)
                operator=str(f)

            def h2m():
                global operator
                f=float(num1.get())
                c=f*60
                num1.set(c)
                operator=str(c)

            def d2m():
                global operator
                c=float(num1.get())
                f=c*24*60
                num1.set(f)
                operator=str(f)

            def d2h():
                global operator
                f=float(num1.get())
                c=f*24
                num1.set(c)
                operator=str(c)

            def mo2h():
                global operator
                c=float(num1.get())
                f=c*30*24
                num1.set(f)
                operator=str(f)

            def mo2d():
                global operator
                f=float(num1.get())
                c=f*30
                num1.set(c)
                operator=str(c)

            def mo2m():
                global operator
                c=float(num1.get())
                f=c*30*24*60
                num1.set(f)
                operator=str(f)

            def y2d():
                global operator
                f=float(num1.get())
                c=f*365.25
                num1.set(c)
                operator=str(c)

                                                                                        #ANGLES

            def d2r():
                global operator
                c=float(num1.get())
                f=c*0.017453
                num1.set(f)
                operator=str(f)

            def d2g():
                global operator
                f=float(num1.get())
                c=f*1.11111111112
                num1.set(c)
                operator=str(c)

            def r2g():
                global operator
                c=float(num1.get())
                f=c*63.66198
                num1.set(f)
                operator=str(f)

            def g2r():
                global operator
                f=float(num1.get())
                c=f*0.015708
                num1.set(c)
                operator=str(c)

            def r2d():
                global operator
                c=float(num1.get())
                f=c*57.29578
                num1.set(f)
                operator=str(f)

            def g2d():
                global operator
                f=float(num1.get())
                c=f*0.9
                num1.set(c)
                operator=str(c)

                                                                                    #TEMPERATURE

            def f2c():
                global operator
                f=float(num1.get())
                c=(f-32)*5/9
                num1.set(c)
                operator=str(c)

            def c2f():
                global operator
                c=float(num1.get())
                f=9*c/5+32
                num1.set(f)
                operator=str(f)

            def k2c():
                global operator
                f=float(num1.get())
                c=f-273.15
                num1.set(c)
                operator=str(c)

            def c2k():
                global operator
                c=float(num1.get())
                f=c+273.15
                num1.set(f)
                operator=str(f)

            def f2k():
                global operator
                f=float(num1.get())
                c=(f-32)*5/9+273.15
                num1.set(c)
                operator=str(c)

            def k2f():
                global operator
                c=float(num1.get())
                f=9*(c-273.15)/5+32
                num1.set(f)
                operator=str(f)
            def calmain():
                root.destroy()
                import main
                main.main()
                return

                                                                                 #AUTHOR AND HELP

            def aut():
                messagebox.showinfo("AUTHOR","hey!!!  i am created by AARYAN SAHA")

            def help1():
                messagebox.showinfo("HELP","THIS IS A SCIENTIFIC CALCULATOR\nALL THE FUNCTIONS ARE EXPLAINED HERE\n\n\n    !    :THIS ONE STANDS FOR CALCULATING FACTORIAL VALUE\nPOW :THIS ONE STANDS FOR CALCULATING POWER\n  1/2  :THIS ONE STANDS FOR CALCULATING SQUARE ROOT\n   %   :THIS ONE STANDS FOR CALCULATING MODULUS\n   C   :THIS ONE IS USED TO CLEAR THE SCREEN\n  1/X  :THIS ONE STANDS FOR CALCULATING INVERSE\n")

                                                                                        #FRAME

            root = Tk()
            frame=Frame(root)
            frame.pack()

            root.title('calculator')
            root.configure(background=cback)
            operator=""
            num1=StringVar()

            topFrame = Frame(root)
            topFrame.configure(background=cback)
            topFrame.pack(side=TOP)

                                                                                #MENU INITIALISATION

            menu=Menu(root)
            root.config(menu=menu)
            menu.configure(background=cfile,fg=ctext)

                                                                                    #MAIN MENU

            subMenu= Menu(menu)
            subMenu.configure(background=cback,fg=ctext)
            menu.add_cascade(label="file",menu=subMenu)
            subMenu.add_command(label="reset",command=clear)
            subMenu.add_command(label="delete",command=delete)
            subMenu.add_command(label="equals",command=equals)
            subMenu.add_command(label="reverse",command=reverse)
            subMenu.add_command(label="forward",command=forward)
            subMenu.add_separator()
            subMenu.add_command(label="main menu",command=calmain)
            subMenu.add_command(label="author",command=aut)
            subMenu.add_command(label="help",command=help1)
            subMenu.add_command(label="exit",command=quit)

                                                                                    #FUNCTIONS MENU

            fun= Menu(menu)
            fun.configure(background=cback,fg=ctext)
            menu.add_cascade(label="functions",menu=fun)
            fun.add_command(label="factorial",command=fact)
            fun.add_command(label="inverse",command=inverse)
            fun.add_command(label="modulus",command=lambda:click("%"))
            fun.add_command(label="power",command=lambda:click("**"))
            fun.add_command(label="root",command=lambda:click("**0.5"))

                                                                                   #TEMPERATURE MENU

            temp= Menu(menu)
            temp.configure(background=cback,fg=ctext)
            menu.add_cascade(label="temp",menu=temp)
            temp.add_command(label="celsius to farhenhiet",command=c2f)
            temp.add_command(label="farhenhiet to celsius",command=f2c)
            temp.add_command(label="celsius to kelvin",command=c2k)
            temp.add_command(label="kelvin to celsius",command=k2c)
            temp.add_command(label="kelvin to farhenhiet",command=k2f)
            temp.add_command(label="farhenhiet to kelvin",command=f2k)

                                                                                    #GRAPH MENU

            graph= Menu(menu)
            graph.configure(background=cback,fg=ctext)
            menu.add_cascade(label="graph",menu=graph)
            graph.add_command(label="sin",command=gsin)
            graph.add_command(label="asin",command=gasin)
            graph.add_command(label="cos",command=gcos)
            graph.add_command(label="acos",command=gacos)
            graph.add_command(label="tan",command=gtan)
            graph.add_command(label="atan",command=gatan)
            graph.add_command(label="cosec",command=gcosec)
            graph.add_command(label="sec",command=gsec)
            graph.add_command(label="cot",command=gcot)
            graph.add_command(label="log",command=glog)
            graph.add_command(label="log2",command=glog2)
            graph.add_command(label="log10",command=glog10)
            graph.add_command(label="inverse",command=ginverse)
            graph.add_command(label="square root",command=gsqrt)

                                                                                #TRIGONOMETRY MENU

            trigo= Menu(menu)
            trigo.configure(background=cback,fg=ctext)
            menu.add_cascade(label="trigo",menu=trigo)
            trigo.add_command(label="sin",command=sin)
            trigo.add_command(label="asin",command=asin)
            trigo.add_command(label="cos",command=cos)
            trigo.add_command(label="acos",command=acos)
            trigo.add_command(label="tan",command=tan)
            trigo.add_command(label="atan",command=atan)
            trigo.add_command(label="cosec",command=cosec)
            trigo.add_command(label="acosec",command=acosec)
            trigo.add_command(label="sec",command=sec)
            trigo.add_command(label="asec",command=asec)
            trigo.add_command(label="cot",command=cot)
            trigo.add_command(label="acot",command=acot)

                                                                                        #TIME MENU

            time= Menu(menu)
            time.configure(background=cback,fg=ctext)
            menu.add_cascade(label="time",menu=time)
            time.add_command(label="minute to second",command=m2s)
            time.add_command(label="hour to second",command=h2s)
            time.add_command(label="day to second",command=d2s)
            time.add_command(label="hour to minute",command=h2m)
            time.add_command(label="day to minute",command=d2m)
            time.add_command(label="month to minute",command=mo2m)
            time.add_command(label="day to hour",command=d2h)
            time.add_command(label="month to hour",command=mo2h)
            time.add_command(label="month to day",command=mo2d)
            time.add_command(label="year to day",command=y2d)

                                                                                        #ANGLE MENU

            angle= Menu(menu)
            angle.configure(background=cback,fg=ctext)
            menu.add_cascade(label="angles",menu=angle)
            angle.add_command(label="degree to radian",command=d2r)
            angle.add_command(label="degree to gradian",command=d2g)
            angle.add_command(label="radian to gradian",command=r2g)
            angle.add_command(label="gradian to radian",command=g2r)
            angle.add_command(label="radian to degree",command=r2d)
            angle.add_command(label="gradian to degree",command=g2d)

                                                                                        #LOG MENU

            logirithm= Menu(menu)
            logirithm.configure(background=cback,fg=ctext)
            menu.add_cascade(label="log",menu=logirithm)
            logirithm.add_command(label="log",command=log)
            logirithm.add_command(label="log10",command=log10)
            logirithm.add_command(label="log2",command=log2)

                                                                                        #DISPLAY

            txtDisplay=Entry(frame,relief='flat',width=20,bg=cent,highlightthickness=0,font=('Bold and Compact',25,'bold'),textvariable=num1,fg=cotxt,insertwidth=1,justify='right').grid(row=0,column=0)

                                                                                        #BUTTONS

            button1 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="1",fg=ctext,command=lambda:click(1))
            button2 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="2",fg=ctext,command=lambda:click(2))
            button3 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="3",fg=ctext,command=lambda:click(3))
            button4 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="4",fg=ctext,command=lambda:click(4))
            button5 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="5",fg=ctext,command=lambda:click(5))
            button6 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="6",fg=ctext,command=lambda:click(6))
            button7 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="7",fg=ctext,command=lambda:click(7))
            button8 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="8",fg=ctext,command=lambda:click(8))
            button9 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="9",fg=ctext,command=lambda:click(9))
            button0 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="0",fg=ctext,command=lambda:click(0))
            button10 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="c",fg=ctext,command=clear)
            button11 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="+",fg=ctext,command=lambda:click("+"))
            button12 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="-",fg=ctext,command=lambda:click("-"))
            button13 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="x",fg=ctext,command=lambda:click("*"))
            button14 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="/",fg=ctext,command=lambda:click("/"))
            button15 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="=",fg=ctext,command=equals)
            button16 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="^x",fg=ctext,command=lambda:click("**"))
            button17 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="^½",fg=ctext,command=lambda:click("**0.5"))
            button18 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="%",fg=ctext,command=lambda:click("%"))
            button19 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="!",fg=ctext,command=fact)
            button20 = Button(topFrame,font=('Courier New Bold',23,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text=".",fg=ctext,command=lambda:click("."))
            button21 = Button(topFrame,font=('Courier New Bold',20,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="(",fg=ctext,command=lambda:click("("))
            button22 = Button(topFrame,font=('Courier New Bold',20,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text=")",fg=ctext,command=lambda:click(")"))
            button23 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="1/x",fg=ctext,command=inverse)
            button24 = Button(topFrame,font=('Courier New Bold',15,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="DEL",fg=ctext,command=delete)
            button25 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="sin",fg=ctext,command=sin)
            button26 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="asin",fg=ctext,command=asin)
            button27 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="cos",fg=ctext,command=cos)
            button28 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="acos",fg=ctext,command=acos)
            button29 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="tan",fg=ctext,command=tan)
            button30 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="atan",fg=ctext,command=atan)
            button31 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="PI",fg=ctext,command=lambda:click(3.141592654))
            button32 = Button(topFrame,font=('Courier New Bold',15,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="log10",fg=ctext,command=log10)
            button33 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="log",fg=ctext,command=log)
            button34 = Button(topFrame,font=('Courier New Bold',18,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="log2",fg=ctext,command=log2)

                                                                                #BUTTON POSITIONS

            button1.grid(row=0,column=0)
            button2.grid(row=0,column=1)
            button3.grid(row=0,column=2)
            button4.grid(row=1,column=0)
            button5.grid(row=1,column=1)
            button6.grid(row=1,column=2)
            button7.grid(row=2,column=0)
            button8.grid(row=2,column=1)
            button9.grid(row=2,column=2)
            button0.grid(row=3,column=1)
            button10.grid(row=3,column=2)
            button11.grid(row=2,column=3)
            button12.grid(row=2,column=4)
            button13.grid(row=0,column=3)
            button14.grid(row=0,column=4)
            button15.grid(row=3,column=3)
            button16.grid(row=1,column=4)
            button17.grid(row=1,column=3)
            button18.grid(row=4,column=0)
            button19.grid(row=4,column=2)
            button20.grid(row=3,column=0)
            button21.grid(row=4,column=3)
            button22.grid(row=4,column=4)
            button23.grid(row=4,column=1)
            button24.grid(row=3,column=4)
            button25.grid(row=5,column=0)
            button26.grid(row=6,column=0)
            button27.grid(row=5,column=1)
            button28.grid(row=6,column=1)
            button29.grid(row=5,column=2)
            button30.grid(row=6,column=2)
            button31.grid(row=5,column=3)
            button32.grid(row=6,column=3)
            button33.grid(row=5,column=4)
            button34.grid(row=6,column=4)

            root.mainloop()
