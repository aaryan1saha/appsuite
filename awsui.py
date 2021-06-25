import boto3
import botocore
import os

BUCKET_NAME = 'mus1307' # replace with your bucket name
KEY = 'log.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'log.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
#_____________________________________________________________________________________UI___5v1__________________________________________________________________________________________
from tkinter import *
import math
import tkinter
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd

BUCKET_NAME = 'mus1307' # replace with your bucket name
KEY = 'main.py' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'main.py')

except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
#_____________________________________________________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________SIGN__IN__________________________________________________________________________________________________

def signin():
    cback="white"
    ctext="black"
    cfile="white"
    cotxt="white"

    xroot=Tk()
#    xroot.attributes('-zoomed',True)
    xroot.title('log-in')
    xroot.configure(background=cback)
    userid=StringVar()
    password=StringVar()
   # panda=pd.read_csv('log.txt',header=None)
    userid.set("")
    useri=StringVar()
    passwor=StringVar()
    gns=StringVar()
    dats=StringVar()
    mons=StringVar()
    years=StringVar()
    useriq=StringVar()
    gnsq=StringVar()
    datsq=StringVar()
    monsq=StringVar()
    yearsq=StringVar()

    def login():
        global panda
        panda=pd.read_csv('log.txt',header=None)
        zx=int(panda.shape[0])
        for i in range(zx):
            if panda[0][i]==str(userid.get()):
                if panda[1][i]==int(password.get()):
                    xroot.destroy()
                    import main
                    main.main()
                else:
                    messagebox.showinfo("INCORRECT PASSWORD!","PLEASE TRY AGAIN")
                    return
        else:
            messagebox.showinfo("","DATA NOT FOUND OR WRONG ENTRY")
        return

    def forgot():
        global useriq,gnsq,datsq,monsq,yearsq
        xroot.destroy()
        panda=pd.read_csv('log.txt',header=None)
        zx=int(panda.shape[0])
        forg=Tk()
        froog=Frame(forg)
        froog.pack()
        prt=Frame(forg)
        prt.pack()
        prt.configure(background=cback)
        forg.title('sign-up')
        froog.configure(background=cback)
        forg.configure(background=cback)
        useriq=StringVar(forg)
        gnsq=StringVar(forg)
        datsq=StringVar(forg)
        monsq=StringVar(forg)
        yearsq=StringVar(forg)
        gnsq.set("MALE")
        datsq.set("1")
        monsq.set("1")
        yearsq.set("2000")

        def find():
            global useriq,passworq,gnsq,datsq,monsq,yearsq
            a=str(gnsq.get())
            if a=="MALE":
                b="m"
            else:
                b="f"
            panda=pd.read_csv('log.txt',header=None)
            zx=int(panda.shape[0])
            for i in range(zx):
                if panda[0][i]==str(useriq.get()):
                    if panda[2][i]==str(b):
                        if panda[3][i]==int(datsq.get()):
                            if panda[4][i]==int(monsq.get()):
                                if panda[5][i]==int(yearsq.get()):
                                    p="YOUR PASSWORD IS "+str(panda[1][i])
                                    messagebox.showinfo("",str(p))
                                    forg.destroy()
                                    return
            else:
                messagebox.showinfo("","DATA NOT FOUND OR WRONG ENTRY")
            return

        usd1=Entry(froog,width=15,bd=3,bg=cotxt,highlightthickness=0,font=('Bold and Compact',15,'bold'),textvariable=useriq,fg="black",insertwidth=1,justify='right').grid(row=1,column=1)
        gen1=OptionMenu(froog,gnsq,"MALE","FEMALE").grid(row=2,column=1)
        dt1=OptionMenu(prt,datsq,"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31").grid(row=0,column=1)
        mn1=OptionMenu(prt,monsq,"1","2","3","4","5","6","7","8","9","10","11","12").grid(row=0,column=2)
        yr1=OptionMenu(prt,yearsq,"1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018").grid(row=0,column=3)
        but1=Button(prt,font=('Courier New Bold',15,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="SEARCH",fg=ctext,command=find).grid(row=1,column=0)

        lb1=Label(froog,font=('Courier New Bold',15,'bold'),text='USER ID',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=1,column=0)
        lb3=Label(froog,font=('Courier New Bold',15,'bold'),text='GENDER',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=2,column=0)
        lb4=Label(prt,font=('Courier New Bold',15,'bold'),text='DOB      ',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=0,column=0)

        forg.mainloop()
        signin()
        return

    def signup():
        global app,useri,passwor,gns,dats,mons,years
        xroot.destroy()
        prot=Tk()
        proot=Frame(prot)
        proot.pack()
        art=Frame(prot)
        art.pack()
        art.configure(background=cback)
        prot.title('sign-up')
        proot.configure(background=cback)
        prot.configure(background=cback)
        useri=StringVar(prot)
        passwor=StringVar(prot)
        gns=StringVar(prot)
        dats=StringVar(prot)
        mons=StringVar(prot)
        years=StringVar(prot)
        gns.set("MALE")
        dats.set("1")
        mons.set("1")
        years.set("2000")

        def create():
            global useri,passwor,gns,dats,mons,years
            app=open("log.txt","a+")
            a=str(gns.get())
            if(str(useri.get())=="" or str(passwor.get())==""):
                print("please fill all the entries")
                return
            if a=="MALE":
                b="m"
            else:
                b="f"
            x=str(useri.get())+","+str(passwor.get())+","+str(b)+","+str(dats.get())+","+str(mons.get())+","+str(years.get())
            app.write(str(x)+"\n")
            prot.destroy()
            app.close()
            BUCKET_NAME = 'mus1307' # replace with your bucket name
            KEY = 'log.txt' # replace with your object key
            upnm='log.txt'
            s3 = boto3.client('s3')
            s3.upload_file(KEY,BUCKET_NAME,upnm)
            print("uploaded")
            return

        usd1=Entry(proot,width=15,bd=3,bg=cotxt,highlightthickness=0,font=('Bold and Compact',15,'bold'),textvariable=useri,fg="black",insertwidth=1,insertbackground="black",justify='right').grid(row=1,column=1)
        psw1=Entry(proot,width=15,bd=3,bg=cotxt,highlightthickness=0,font=('Bold and Compact',15,'bold'),textvariable=passwor,insertbackground="black",fg="black",insertwidth=1,justify='right').grid(row=2,column=1)
        gen1=OptionMenu(proot,gns,"MALE","FEMALE").grid(row=3,column=1)
        dt1=OptionMenu(art,dats,"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31").grid(row=0,column=1)
        mn1=OptionMenu(art,mons,"1","2","3","4","5","6","7","8","9","10","11","12").grid(row=0,column=2)
        yr1=OptionMenu(art,years,"1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018").grid(row=0,column=3)
        but1=Button(art,font=('Courier New Bold',15,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="SIGN-UP",fg=ctext,command=create).grid(row=1,column=0)

        lb1=Label(proot,font=('Courier New Bold',15,'bold'),text='USER ID',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=1,column=0)
        lb2=Label(proot,font=('Courier New Bold',15,'bold'),text='PASSWORD',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=2,column=0)
        lb3=Label(proot,font=('Courier New Bold',15,'bold'),text='GENDER',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=3,column=0)
        lb4=Label(art,font=('Courier New Bold',15,'bold'),text='DOB      ',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=0,column=0)

        prot.mainloop()
        signin()
        return

    usid=Entry(xroot,width=15,bd=1,bg=cfile,highlightthickness=0,font=('Bold and Compact',15,'bold'),textvariable=userid,fg="black",insertwidth=1,insertbackground="black",justify='right').grid(row=1,column=1)
    passw=Entry(xroot,width=15,bd=1,bg=cfile,highlightthickness=0,font=('Bold and Compact',15,'bold'),textvariable=password,insertbackground="black",fg="black",insertwidth=1,justify='right').grid(row=2,column=1)

    button1 = Button(xroot,font=('Courier New Bold',15,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="   LOG-IN   ",fg=ctext,command=login).grid(row=4,column=1)
    button2 = Button(xroot,font=('Courier New Bold',15,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="SIGN-UP",fg=ctext,command=signup).grid(row=4,column=0)
    button3 = Button(xroot,font=('Courier New Bold',12,'bold'),padx=14,pady=14,relief='flat',bg=cback,highlightthickness=0,text="forgot password",fg=ctext,command=forgot).grid(row=3,column=1)

    lab1=Label(xroot,font=('Courier New Bold',15,'bold'),text='USER ID',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=1,column=0)
    lab2=Label(xroot,font=('Courier New Bold',15,'bold'),text='PASSWORD',justify=RIGHT,padx=10,pady=10,relief='flat',bg=cback,highlightthickness=0,fg=ctext).grid(row=2,column=0)

    xroot.mainloop()
signin()
#_________________________________________________________________________________________END_________________________________________________________________________________________
os.remove('log.txt')
