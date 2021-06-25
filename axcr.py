#_____________________________________________________________________________________UI___5v1__________________________________________________________________________________________
from tkinter import *
import math
import tkinter
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import os

quant=0
x=6
#____________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________________________________CRICKET____________________________________________________________________________________________
def cr():
    global team1,team2,totovr,wickt,team1p,typet,balls,bs,quant,ovr,wicket,playerstat,bat11,bat10,bat12,bat21,bat22,bat20,scr,wkt,bal

    def tv():
            chz=Tk()
            chz.configure(background="tomato")
            def choi(num):
                global x
                if num==4:
                    x=1
                    chz.destroy()
                elif num==1:
                    x=20
                    chz.destroy()
                elif num==2:
                    x=50
                    chz.destroy()
                elif num==5:
                    chz.destroy()
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
                elif num==6:
                    chz.destroy()
                    import main
                    main.main()
                else:
                    x=3
                    chz.destroy()
            button0 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="        T-20        ",fg="white",command=lambda:choi(1)).grid(row=0,column=0)
            button1 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="    ONE DAY     ",fg="white",command=lambda:choi(2)).grid(row=1,column=0)
            button2 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="      FAST-3      ",fg="white",command=lambda:choi(3)).grid(row=2,column=0)
            button3 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="  SUPER-OVER ",fg="white",command=lambda:choi(4)).grid(row=3,column=0)
            button5 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="   MAIN MENU  ",fg="white",command=lambda:choi(6)).grid(row=4,column=0)
            button4 = Button(chz,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="        EXIT        ",fg="white",command=lambda:choi(5)).grid(row=5,column=0)
            chz.mainloop()
            return x
            Tk.quit()

    team1="         IND"
    team2="         AUS"
    totovr=tv()
    wickt=0
    team1p=np.array(["A","B","C","D","E","F","G","H","I","J","K","L"])
    typet=np.array(["BATSMAN","WICKET KEEPERR","BATSMAN","BATSMAN","BATSMAN","BATSMAN","BALLER","BALLER","BALLER","BALLER","BALLER"])
    balls=0
    bs=1
    root=Tk()
    frame=Frame(root)
    frame.configure(background="black")
    frame.pack()
    tframe=Frame(root)
    tframe.configure(background="tomato")
    tframe.pack()

    root.title('CRICKET')
    root.configure(background="tomato")
    #--------------------------------------------------------------------------STRINGVAR--------------------------------------------------------------------------------------------
    scr=StringVar()
    wkt=StringVar()
    ovr=StringVar()
    bal=StringVar()
    tovr=StringVar()

    oscr=str(scr.get())
    oscr+=str("0")
    scr.set(str(oscr))

    owkt=str(wkt.get())
    owkt+=str("0")
    wkt.set(str(owkt))

    oovr=str(ovr.get())
    oovr+=str("0")
    ovr.set(str(oovr))

    obal=str(bal.get())
    obal+=str("0")
    bal.set(str(obal))

    def balo():
        obal=str("0")
        bal.set(str(obal))

    def equalscr(x):
        global oscr
        oscr=str(scr.get())
        oscr+=str(x)
        scr.set(str(oscr))

    def adedscr(x):
        oscr=str(scr.get())
        oscr+=str(x)
        scr.set(str(eval(oscr)))

    def adedwkt():
        owkt=str(wkt.get())
        owkt+=str("+1")
        wkt.set(str(eval(owkt)))

    def adedovr():
        oovr=str(ovr.get())
        oovr+=str("+1")
        ovr.set(str(eval(oovr)))

    def adedbal():
        obal=str(bal.get())
        obal+=str("+1")
        bal.set(str(eval(obal)))

    def tovru(x):
        otovr=str(tovr.get())
        otovr+=str(" ")
        otovr+=str(x)
        tovr.set(str(otovr))

    def tovrr():
        otovr=str("")
        tovr.set(str(otovr))

    cback="black"
    ctext="white"


    playerstat=np.array([["","",0,0,"",""]])

    def showt():
        global playerstat,scr,wkt,ovr,bal
        ds=Tk()
        ds.title('RESULTS')
        ds.configure(background="black")
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text="IND",justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=0,column=0)
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text="SCORE",justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=1,column=0)
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text="WICKET",justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=1,column=1)
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text="OVER",justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=1,column=2)
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text="BALLS",justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=1,column=3)
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text=str(scr.get()),justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=2,column=0)
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text=str(wkt.get()),justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=2,column=1)
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text=str(ovr.get()),justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=2,column=2)
        bt1=Label(ds,font=('Courier New Bold',15,'bold'),text=str(bal.get()),justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=2,column=3)
    #    bt1=Label(ds,font=('Courier New Bold',15,'bold'),text=,justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=0,column=0)
    #    bt1=Label(ds,font=('Courier New Bold',15,'bold'),text=,justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=0,column=0)


    def matchend():
        global ovr,totovr
        a=int(ovr.get())
        b=int(wkt.get())
        if a==totovr or b==10:
            showt()
            root.destroy()
            return

    def adplstat():
        global quant,playerstat,team1p,bat10,bat11,bat12
        playerstat=np.append(playerstat,[["","",0,0,"",""]],axis=0)
        playerstat[quant][0]=str(team1p[quant])
        playerstat[quant][1]=str(typet[quant])
        playerstat[quant][2]=str(bat11)
        playerstat[quant][3]=str(bat12)
        playerstat[quant][4]="fours"
        playerstat[quant][5]="six"
        return

    def adplstat2():
        global quant,playerstat,team1p,bat21,bat22
        playerstat=np.append(playerstat,[["","",0,0,"",""]],axis=0)
        playerstat[quant][0]=str(team1p[quant])
        playerstat[quant][1]=str(typet[quant+1])
        playerstat[quant][2]=str(bat21)
        playerstat[quant][3]=str(bat22)
        playerstat[quant][4]="fours"
        playerstat[quant][5]="six"
        return

    bat10=StringVar()
    bat11=StringVar()
    bat12=StringVar()
    bat20=StringVar()
    bat21=StringVar()
    bat22=StringVar()

    obt10=str(team1p[0])
    bat10.set(str(obt10))
    obt20=str(team1p[1])
    bat20.set(str(obt20))

    def bt10(i):
        obt10=str(team1p[i])
        bat10.set(str(obt10))

    def bt20(i):
        obt20=str(team1p[i])
        bat20.set(str(obt20))

    def bt11(x):
        obal=str(bat11.get())
        obal+=str("+")
        obal+=str(x)
        bat11.set(str(eval(obal)))

    def bt12():
        obal=str(bat12.get())
        obal+=str("+1")
        bat12.set(str(eval(obal)))

    def bt21(x):
        obal=str(bat21.get())
        obal+=str("+")
        obal+=str(x)
        bat21.set(str(eval(obal)))

    def bt22():
        obal=str(bat22.get())
        obal+=str("+1")
        bat22.set(str(eval(obal)))



    def addr(x):
        global scr,ovr,balls,tovr,bat1,bat2,bs,oscr
        matchend()
        equalscr("+")
        adedscr(x)
        balls=balls+1

        if balls==6:
            tovrr()
            adedovr()
            balls=0
            balo()
            switchpl()
        else:
            tovru(x)
            adedbal()
        matchend()
        if bs==1:
            bt11(x)
            bt12()
        else:
            bt21(x)
            bt22()
        if x==1 or x==3 or x==5:
            switchpl()
        return

    def wide():
        global scr,tovr
        equalscr("+")
        adedscr(1)
        tovru("E")
        return

    def wicket():
        global wkt,wickt,balls,ovr,tovr,bs,bat1,bat2,team1,quant
        matchend()
        adedwkt()
        balls=balls+1
        wickt=wickt+1
        if balls==6:
            tovrr()
            adedovr()
            balls=0
            balo()
            switchpl()
        else:
            tovru("W")
            adedbal()
        if bs==1:
            quant=quant+1
            adplstat()
            bt10(wickt+1)
            bat11.set(str(0))
            bat12.set(str(0))
        else:
            quant=quant+1
            adplstat2()
            bt20(wickt+1)
            bat21.set(str(0))
            bat22.set(str(0))
        return

    def switchpl():
        global bs
        if bs==1:
            bs=2
        else:
            bs=1
        return

    catext="gold"
    b1=Label(frame,font=('Courier New Bold',15,'bold'),text=team1,justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="sky blue").grid(row=0,column=0)
    b2=Label(frame,font=('Courier New Bold',15,'bold'),text=' SCORE ',justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="orange").grid(row=1,column=0)
    b3=Label(frame,font=('Courier New Bold',15,'bold'),text=' WICKETS',justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="orange").grid(row=1,column=1)
    b4=Label(frame,font=('Courier New Bold',15,'bold'),text='  OVERS ',justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="orange").grid(row=1,column=2)
    b4a=Label(frame,font=('Courier New Bold',15,'bold'),text='  BALLS ',justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="orange").grid(row=1,column=3)
    b5=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=scr,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="teal").grid(row=2,column=0)
    b6=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=wkt,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="teal").grid(row=2,column=1)
    b7=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=ovr,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="teal").grid(row=2,column=2)
    b7a=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=bal,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="teal").grid(row=2,column=3)
    b8=Label(frame,font=('Courier New Bold',15,'bold'),text='THIS OVER',justify=LEFT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="grey").grid(row=3,column=0)
    b9=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=tovr,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="tomato").grid(row=4,column=1)
    b10=Label(frame,font=('Courier New Bold',15,'bold'),text='BATSMAN',justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="dark red").grid(row=5,column=0)
    b11=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=bat10,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=catext).grid(row=6,column=0)
    b12=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=bat11,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=catext).grid(row=6,column=1)
    b11=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=bat12,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=catext).grid(row=6,column=2)
    b12=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=bat20,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=catext).grid(row=7,column=0)
    b11=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=bat21,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=catext).grid(row=7,column=1)
    b12=Label(frame,font=('Courier New Bold',15,'bold'),textvariable=bat22,justify=CENTER,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=catext).grid(row=7,column=2)
    b13=Label(frame,font=('Courier New Bold',15,'bold'),text="      V/S",justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="dark red").grid(row=0,column=1)
    b14=Label(frame,font=('Courier New Bold',15,'bold'),text=team2,justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg="yellow").grid(row=0,column=2)

    bn0=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="0",fg=ctext,command=lambda:addr(0)).grid(row=0,column=0)
    bn1=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="1",fg=ctext,command=lambda:addr(1)).grid(row=0,column=1)
    bn2=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="2",fg=ctext,command=lambda:addr(2)).grid(row=0,column=2)
    bn3=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="3",fg=ctext,command=lambda:addr(3)).grid(row=0,column=3)
    bn4=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="4",fg=ctext,command=lambda:addr(4)).grid(row=0,column=4)
    bn5=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="5",fg=ctext,command=lambda:addr(5)).grid(row=0,column=5)
    bn6=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="6",fg=ctext,command=lambda:addr(6)).grid(row=0,column=6)
    #bn7=Button(tframe,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="NB",fg=ctext,command=wide).grid(row=0,column=7)
    bn8=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="E",fg=ctext,command=wide).grid(row=0,column=8)
    bn9=Button(tframe,font=('Courier New Bold',20,'bold'),bg="tomato",padx=14,highlightthickness=0,pady=14,bd=0,text="W",fg=ctext,command=wicket).grid(row=0,column=9)
    #bn10=Button(tframe,font=('Courier New Bold',20,'bold'),bg=cback,padx=14,highlightthickness=0,pady=14,bd=0,text="SW",fg=ctext,command=switchpl).grid(row=0,column=10)

    root.mainloop()
