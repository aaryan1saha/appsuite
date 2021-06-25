#_____________________________________________________________________________________UI___5v1__________________________________________________________________________________________
from tkinter import *
import math
import tkinter
from tkinter import messagebox
import numpy as np
import boto3
import os
#_________________________________________________________________________CHOICE MENU FOR APLLICATION SELECTION___________________________________________________________________________

def cmain():
    cm=Tk()
    cm.configure(background="black")
    def cmain(num):
        global xy
        if num==5:
            xy=5
            cm.destroy()
        else:
            xy=num
            cm.destroy()
        return xy
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
        if os.path.isfile('main.py'):
            os.remove('main.py')
        cm.quit()
        
    button0 = Button(cm,font=('Courier New Bold',20,'bold'),bg="black",padx=14,highlightthickness=0,pady=14,bd=0,text="CALCULATOR",fg="white",command=lambda:cmain(1)).grid(row=0,column=0)
    button1 = Button(cm,font=('Courier New Bold',20,'bold'),bg="black",padx=14,highlightthickness=0,pady=14,bd=0,text="   INTEREST   ",fg="white",command=lambda:cmain(2)).grid(row=1,column=0)
    button2 = Button(cm,font=('Courier New Bold',20,'bold'),bg="black",padx=14,highlightthickness=0,pady=14,bd=0,text="BOOK  STORE",fg="white",command=lambda:cmain(3)).grid(row=2,column=0)
    button4 = Button(cm,font=('Courier New Bold',20,'bold'),bg="black",padx=14,highlightthickness=0,pady=14,bd=0,text="    CRICKET    ",fg="white",command=lambda:cmain(4)).grid(row=3,column=0)
    button3 = Button(cm,font=('Courier New Bold',20,'bold'),bg="black",padx=14,highlightthickness=0,pady=14,bd=0,text="       EXIT       ",fg="white",command=lambda:cmain(5)).grid(row=4,column=0)
    cm.mainloop()
    return xy

#_________________________________________________________________________________________MAIN___________________________________________________________________________________________

def main():
    global chc
    chc=0
#_______________________________________________________________________________________UI CHOICE____________________________________________________________________________________
    while chc!=5:
        chc=cmain()
        if chc==5:
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
            if os.path.isfile('main.py'):
                os.remove('main.py')
            quit()
        else:
                if chc==1:
                    BUCKET_NAME = 'mus1307' # replace with your bucket name
                    KEY = 'axsc.py' # replace with your object key

                    s3 = boto3.resource('s3')

                    try:
                        s3.Bucket(BUCKET_NAME).download_file(KEY, 'axsc.py')
                    except botocore.exceptions.ClientError as e:
                        if e.response['Error']['Code'] == "404":
                            print("The object does not exist.")
                        else:
                            raise
                    import axsc
                    axsc.sc()
                    os.remove('axsc.py')
                elif chc==2:
                    BUCKET_NAME = 'mus1307' # replace with your bucket name
                    KEY = 'axsi.py' # replace with your object key

                    s3 = boto3.resource('s3')

                    try:
                        s3.Bucket(BUCKET_NAME).download_file(KEY, 'axsi.py')
                    except botocore.exceptions.ClientError as e:
                        if e.response['Error']['Code'] == "404":
                            print("The object does not exist.")
                        else:
                            raise
                    import axsi
                    axsi.si()
                    os.remove('axsi.py')
                elif chc==3:
                    BUCKET_NAME = 'mus1307' # replace with your bucket name
                    KEY = 'axbs.py' # replace with your object key

                    s3 = boto3.resource('s3')

                    try:
                        s3.Bucket(BUCKET_NAME).download_file(KEY, 'axbs.py')
                    except botocore.exceptions.ClientError as e:
                        if e.response['Error']['Code'] == "404":
                            print("The object does not exist.")
                        else:
                            raise
                    import axbs
                    axbs.bs()
                    os.remove('axbs.py')
                elif chc==4:
                    BUCKET_NAME = 'mus1307' # replace with your bucket name
                    KEY = 'axcr.py' # replace with your object key

                    s3 = boto3.resource('s3')

                    try:
                        s3.Bucket(BUCKET_NAME).download_file(KEY, 'axcr.py')
                    except botocore.exceptions.ClientError as e:
                        if e.response['Error']['Code'] == "404":
                            print("The object does not exist.")
                        else:
                            raise
                    import axcr
                    axcr.cr()
                    os.remove('axcr.py')
                else:
                    print("\nWRONG CHOICE\n")
                    main()
    return
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
if os.path.isfile('main.py'):
    os.remove('main.py')
