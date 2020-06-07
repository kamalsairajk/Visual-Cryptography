from PIL import Image
from random import *
import sys
import time
import os
from tkinter import *
t=time.clock()


def filename(a):
    from PIL import Image
    a=E1.get()
    global va
    va=a


def shares(n):
    from PIL import Image
    j=Image.open(va)
    j.save(va)
    m=Image.open(va)
    pix=m.load()
    width,hieght=m.size
    n=int(E2.get())
    if n==2:
        share1 = Image.new("1", m.size, "white")
        share1pix = share1.load()
        for i in range(hieght):
            for j in range(width):
                x = randint(0,1)
                if x == 0:
                    share1pix[j, i] = 0
        share1.save("share1.png")

        
        share2 = Image.new("1", m.size)
        share2pix = share2.load()
        for i in range(hieght):
            for j in range(width):
                if pix[j,i]==0:
                    share2pix[j,i]=share1pix[j,i]
                else:
                    if share1pix[j,i]==0:
                        share2pix[j,i]=1
                    elif share1pix[j,i]==1:
                        x = randint(0,1)
                        if x == 0:
                            share2pix[j, i] = 0
        share2.save("share2.png")

        
        fullshare=Image.new("1", m.size)
        fullsharepix=fullshare.load()
        for i in range(hieght):
            for j in range(width):
                if share1pix[j,i]==share2pix[j,i]:
                   fullsharepix[j,i]=share1pix[j,i]
                else:
                   fullsharepix[j,i]=0
        fullshare.save("fullshare.png")

        
        full=Image.new("1", m.size)
        fullpix=full.load()
        for i in range(hieght):
            for j in range(width):
                if share1pix[j,i]==share2pix[j,i]:
                   fullpix[j,i]=1
                else:
                   fullpix[j,i]=0
        full.save("full.png")

        
        r=os.stat(va).st_size
        if r>7000:
            fullshare=Image.open("fullshare.png")
            full=Image.open("full.png")
            fullsharepix=fullshare.load()
            fullpix=full.load()
            for i in range(hieght):
                for j in range(width):
                    if fullsharepix[j,i]==0:
                        fullsharepix[j,i]=1
                    else:
                        fullsharepix[j,i]=0
                    if fullpix[j,i]==0:
                        fullpix[j,i]=1
                    else:
                        fullpix[j,i]=0
            fullshare.save("fullshare.png")
            full.save("full.png")
            
    elif n>2:
        o=Image.new("1",m.size,"white")
        opix=o.load()

        for i in range(hieght):
            for j in range(width):
                if pix[j,i]==0:
                    opix[j,i]=255
                else:
                    opix[j,i]=0


        full=Image.new("1",m.size,"white")
        fullpix=full.load()

        for k in range(1,n+1):
            share=Image.new("1",m.size,"white")
            sharepix=share.load()
            for i in range(hieght):
                for j in range(width):
                    for y in range((width//n)):
                        sharepix[y*n+k-1,i]=opix[y*n+k-1,i]
                    for x in range(hieght//n):
                        sharepix[j,x*n+k-1]=opix[j,x*n+k-1]
                    fullpix[j,i]+=sharepix[j,i]

            a="share"+str(k)+".png"
            share.save(a)


        for i in range(hieght):
            for j in range(width):
                s=0
                for k in range(1,n+1):
                    sh=Image.open("share"+str(k)+".png")
                    shpix=sh.load()
                    if shpix[j,i]==0:
                        s+=1

                if s>0:
                    fullpix[j,i]=0
                elif s==0:
                    fullpix[j,i]=1
        full.save("full.png")
    print(time.clock()-t)


root=Tk()
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
VCrypt=Label(topframe,text="VCyrpt",relief=FLAT,pady=40,width=50)
VCrypt.configure(font=("Times New Roman",40))
VCrypt.pack()
L1=Label(bottomframe,text="Enter the file location:",relief=FLAT,justify=LEFT,padx=8,pady=40)
L1.configure(font=("Times New Roman",20))
L1.grid(row=0,sticky=E)
E1=Entry(bottomframe,bd=5,width=30)
E1.bind("<Return>",filename)
E1.grid(row=1)
J1=Button(bottomframe,text="Enter",relief=RAISED)
J1.configure(font=("Times New Roman",20))
J1.grid(row=2)
E4=Label(bottomframe,relief=FLAT,pady=30)
E4.grid(row=3)
root.mainloop()
root_1=Tk()
topframe1=Frame(root_1)
topframe1.pack()
bottomframe1=Frame(root_1)
bottomframe1.pack(side=BOTTOM)
VCrypt1=Label(topframe1,text="VCyrpt",relief=FLAT,pady=40,width=50)
VCrypt1.configure(font=("Times New Roman",40))
VCrypt1.pack()
L2=Label(bottomframe1,text="Number of Shares:",relief=FLAT,justify=LEFT,padx=18,pady=30)
L2.configure(font=("Times New Roman",20))
L2.grid(row=0,sticky=E)
E2=Entry(bottomframe1,bd=5,width=30)
E2.bind("<Return>",shares)
E2.grid(row=1)
J2=Button(bottomframe1,text="Enter",relief=RAISED)
J2.configure(font=("Times New Roman",20))
J2.grid(row=2)
E3=Label(bottomframe1,relief=FLAT,pady=30)
E3.grid(row=3)
root_1.mainloop()



