from tkinter import *


root=Tk()
root.title("ASTRA TYPE")
root.configure(bg="#87cefa")
root.geometry("1060x620+110+50")
root.resizable(height=False,width=False)



monitor=LabelFrame(root,width=800,height=50,padx=50,pady=30,bg="#87ceeb")
monitor.pack(padx=5, pady=10)


label_string="A S D F G H J K L ;"
#split the string into individual labels
labels_list=label_string.split()

row_val=0
column_val=0

for label_text in labels_list:
    label=Label(monitor,text=label_text,bg="#87ceeb")
    label.grid(row=row_val,column=column_val,padx=5,pady=5)
    column_val+=1

for i in range(column_val):
    monitor.grid_columnconfigure(i,weight=1)


def release(event):
    key=event.keysym
#NUMBERSROW
    if key=="1":
        button_1.config(bg="white")
    elif key=="2":
          button_2.config(bg="white")
    elif key=="3":
          button_3.config(bg="white")
    elif key=="4":
          button_4.config(bg="white")
    elif key=="5":
          button_5.config(bg="white")
    elif key=="6":
          button_6.config(bg="white")
    elif key=="7":
          button_7.config(bg="white")
    elif key=="8":
          button_8.config(bg="white")
    elif key=="9":
          button_9.config(bg="white")
    elif key=="0":
          button_10.config(bg="white")
    elif key=="minus":
          button_11.config(bg="white")
    elif key=="equal":
          button_12.config(bg="white")
    elif key=="BackSpace":
          button_13.config(bg="white")



    #QWERTY LINE
    if key=="q":
        button_Q.config(bg="white")
    elif key=="w":
          button_W.config(bg="white")
    elif key=="e":
          button_E.config(bg="white")
    elif key=="r":
          button_R.config(bg="white")
    elif key=="t":
          button_T.config(bg="white")
    elif key=="y":
          button_Y.config(bg="white")
    elif key=="u":
          button_U.config(bg="white")
    elif key=="i":
          button_I.config(bg="white")
    elif key=="o":
          button_O.config(bg="white")
    elif key=="p":
          button_P.config(bg="white")
    elif key=="bracketleft":
          button_list1.config(bg="white")
    elif key=="bracketright":
          button_list2.config(bg="white")
    elif key=="backslash":
          button_slash1.config(bg="white")  

    # HOME ROW
    if key=="a":
        button_A.config(bg="white")
    elif key=="s":
          button_S.config(bg="white")
    elif key=="d":
          button_D.config(bg="white")
    elif key=="f":
          button_F.config(bg="white")
    elif key=="g":
          button_G.config(bg="white")
    elif key=="h":
          button_H.config(bg="white")
    elif key=="j":
          button_J.config(bg="white")
    elif key=="k":
          button_K.config(bg="white")
    elif key=="l":
          button_L.config(bg="white")
    elif key=="semicolon":
          button_colon.config(bg="white")
    elif key=="apostrophe":
          button_quote.config(bg="white")

    # shift ROW
    if key=="Shift_L":
        button_shift.config(bg="white")
    elif key=="z":
        button_Z.config(bg="white")
    elif key=="x":
          button_X.config(bg="white")
    elif key=="c":
          button_C.config(bg="white")
    elif key=="v":
          button_V.config(bg="white")
    elif key=="b":
          button_B.config(bg="white")
    elif key=="n":
          button_N.config(bg="white")
    elif key=="m":
          button_M.config(bg="white")
    elif key=="comma":
          button_comma.config(bg="white")
    elif key=="period":
          button_stop.config(bg="white")
    elif key=="slash":
          button_slash.config(bg="white")
    elif key=="Shift_R":
        button_shiftR.config(bg="white")

        #space row

    if key=="space":
        space.config(bg="white")
    elif key=="Return":
          button_enter.config(bg="white")
    elif key=="Caps_Lock":
          button_caps.config(bg="white")
    

   
    


          
def click(event):
    key=event.keysym
    

    # HOME ROW
    if key=="1":
        button_1.config(bg="grey")
    elif key=="2":
          button_2.config(bg="grey")
    elif key=="3":
          button_3.config(bg="grey")
    elif key=="4":
          button_4.config(bg="grey")
    elif key=="5":
          button_5.config(bg="grey")
    elif key=="6":
          button_6.config(bg="grey")
    elif key=="7":
          button_7.config(bg="grey")
    elif key=="8":
          button_8.config(bg="grey")
    elif key=="9":
          button_9.config(bg="grey")
    elif key=="0":
          button_10.config(bg="grey")
    elif key=="minus":
          button_11.config(bg="grey")
    elif key=="equal":
          button_12.config(bg="grey")
    elif key=="BackSpace":
          button_13.config(bg="grey")

     #QWERTY LINE
    if key=="q":
        button_Q.config(bg="grey")
    elif key=="w":
          button_W.config(bg="grey")
    elif key=="e":
          button_E.config(bg="grey")
    elif key=="r":
          button_R.config(bg="grey")
    elif key=="t":
          button_T.config(bg="grey")
    elif key=="y":
          button_Y.config(bg="grey")
    elif key=="u":
          button_U.config(bg="grey")
    elif key=="i":
          button_I.config(bg="grey")
    elif key=="o":
          button_O.config(bg="grey")
    elif key=="p":
          button_P.config(bg="grey")
    elif key=="bracketleft":
          button_list1.config(bg="grey")
    elif key=="bracketright":
          button_list2.config(bg="grey")
    elif key=="backslash":
          button_slash1.config(bg="grey")  

    # HOME ROW
    if key=="a":
        button_A.config(bg="grey")
    elif key=="s":
          button_S.config(bg="grey")
    elif key=="d":
          label.destroy()
          button_D.config(bg="grey")
    elif key=="f":
          button_F.config(bg="grey")
    elif key=="g":
          button_G.config(bg="grey")
    elif key=="h":
          button_H.config(bg="grey")
    elif key=="j":
          button_J.config(bg="grey")
    elif key=="k":
          button_K.config(bg="grey")
    elif key=="l":
          button_L.config(bg="grey")
    elif key=="semicolon":
          button_colon.config(bg="grey")
    elif key=="apostrophe":
          button_quote.config(bg="grey")



    # shift ROW
    if key=="Shift_L":
        button_shift.config(bg="grey")
    elif key=="z":
        button_Z.config(bg="grey")
    elif key=="x":
          button_X.config(bg="grey")
    elif key=="c":
          button_C.config(bg="grey")
    elif key=="v":
          button_V.config(bg="grey")
    elif key=="b":
          button_B.config(bg="grey")
    elif key=="n":
          button_N.config(bg="grey")
    elif key=="m":
          button_M.config(bg="grey")
    elif key=="comma":
          button_comma.config(bg="grey")
    elif key=="period":
          button_stop.config(bg="grey")
    elif key=="slash":
        button_slash.config(bg="grey")
    elif key=="Shift_R":
        button_shiftR.config(bg="grey")


        #space row

    if key=="space":
        space.config(bg="grey")
    elif key=="Return":
          button_enter.config(bg="grey")
    elif key=="Caps_Lock":
          button_caps.config(bg="grey")
    elif key=="grave":
          button_first.config(bg="grey")   
        

monitor.focus_set()
monitor.bind("<KeyPress>",click)
monitor.bind("<KeyRelease>",release)



frame=LabelFrame(root, text="astra type master", padx=15,pady=25)
frame.pack(padx=15,pady=25)
frame.config(bg="#1A1A1A")


esc=Button(frame,text='esc',width=6,height=2,bg="white")
esc.grid(row=2,column=0,padx=5)

f1=Button(frame,text='f1',width=6,height=2,bg="white")
f1.grid(row=2,column=1,padx=5)

f2=Button(frame,text='f2',width=6,height=2,bg="white")
f2.grid(row=2,column=2)

f3=Button(frame,text='f3',width=6,height=2,bg="white")
f3.grid(row=2,column=3,padx=5)

f4=Button(frame,text='f4',width=6,height=2,bg="white")
f4.grid(row=2,column=4)

f5=Button(frame,text='f5',width=6,height=2,bg="white")
f5.grid(row=2,column=5,padx=5)

f6=Button(frame,text='f6',width=6,height=2,bg="white")
f6.grid(row=2,column=6)

f7=Button(frame,text='f7',width=6,height=2,bg="white")
f7.grid(row=2,column=7,padx=5,pady=5)

f8=Button(frame,text='f8',width=6,height=2,bg="white")
f8.grid(row=2,column=8)

f9=Button(frame,text='f9',width=6,height=2,bg="white")
f9.grid(row=2,column=9,padx=5)

f10=Button(frame,text='f10',width=6,height=2,bg="white")
f10.grid(row=2,column=10)

f11=Button(frame,text='f11',width=6,height=2,bg="white")
f11.grid(row=2,column=11,padx=5)

f12=Button(frame,text='f12',width=6,height=2,bg="white")
f12.grid(row=2,column=12)

f13=Button(frame,text='insert',width=6,height=2,bg="white")
f13.grid(row=2,column=13,padx=5)

f14=Button(frame,text='prt scr',width=6,height=2,bg="white")
f14.grid(row=2,column=14)

f15=Button(frame,text='delete',width=6,height=2,bg="white")
f15.grid(row=2,column=15,padx=5)


#numbers row

    

button_first=Button(frame,text='`',width=6,height=3,bg="white")
button_first.grid(row=3,column=0)

button_1=Button(frame,text='1',width=6,height=3,bg="white")
button_1.grid(row=3,column=1)

button_2=Button(frame,text='2',width=6,height=3,bg="white")
button_2.grid(row=3,column=2)

button_3=Button(frame,text='3',width=6,height=3 ,bg="white")
button_3.grid(row=3,column=3)

button_4=Button(frame,text='4',width=6,height=3 ,bg="white")
button_4.grid(row=3,column=4)

button_5=Button(frame,text='5',width=6,height=3,bg="white")
button_5.grid(row=3,column=5)

button_6=Button(frame,text='6',width=6,height=3 ,bg="white")
button_6.grid(row=3,column=6)

button_7=Button(frame,text='7',width=6,height=3,bg="white")
button_7.grid(row=3,column=7)

button_8=Button(frame,text='8',width=6,height=3 ,bg="white")
button_8.grid(row=3,column=8)

button_9=Button(frame,text='9',width=6,height=3,bg="white")
button_9.grid(row=3,column=9)

button_10=Button(frame,text='0',width=6,height=3,bg="white")
button_10.grid(row=3,column=10)

button_11=Button(frame,text='-',width=6,height=3,bg="white")
button_11.grid(row=3,column=11)

button_12=Button(frame,text='=',width=6,height=3,bg="white")
button_12.grid(row=3,column=12)

button_13=Button(frame,text='<',width=12,height=3,bg="white")
button_13.grid(row=3,column=13,columnspan=2)

button_15=Button(frame,text='home',width=6,height=3,bg="white")
button_15.grid(row=3,column=15)

# qwerty row

button_tab=Button(frame,text='tab',width=8,height=3,bg="white",state=DISABLED)
button_tab.grid(row=4,column=0,pady=5)

button_Q=Button(frame,text='Q',width=6,height=3,bg="white")
button_Q.grid(row=4,column=1)

button_W=Button(frame,text='W',width=6,height=3,bg="white")
button_W.grid(row=4,column=2)

button_E=Button(frame,text='E',width=6,height=3,bg="white")
button_E.grid(row=4,column=3)

button_R=Button(frame,text='R',width=6,height=3,bg="white")
button_R.grid(row=4,column=4)

button_T=Button(frame,text='T',width=6,height=3,bg="white")
button_T.grid(row=4,column=5)

button_Y=Button(frame,text='Y',width=6,height=3,bg="white")
button_Y.grid(row=4,column=6)

button_U=Button(frame,text='U',width=6,height=3,bg="white")
button_U.grid(row=4,column=7)

button_I=Button(frame,text='I',width=6,height=3,bg="white")
button_I.grid(row=4,column=8)

button_O=Button(frame,text='O',width=6,height=3,bg="white")
button_O.grid(row=4,column=9)

button_P=Button(frame,text='P',width=6,height=3,bg="white")
button_P.grid(row=4,column=10)

button_list1=Button(frame,text='[',width=6,height=3,bg="white")
button_list1.grid(row=4,column=11)

button_list2=Button(frame,text=']',width=6,height=3,bg="white")
button_list2.grid(row=4,column=12)

button_slash1=Button(frame,text="|",width=6,height=3,bg="white")
button_slash1.grid(row=4,column=13,columnspan=2)

button_up=Button(frame,text='pg up',width=6,height=3,bg="white")
button_up.grid(row=4,column=15)


# home row;

button_caps=Button(frame,text='caps lock',width=8,height=3,bg="white")
button_caps.grid(row=5,column=0)

button_A=Button(frame,text='A',width=6,height=3,bg="white")
button_A.grid(row=5,column=1)

button_S=Button(frame,text='S',width=6,height=3,bg="white")
button_S.grid(row=5,column=2)

button_D=Button(frame,text='D',width=6,height=3,bg="white")
button_D.grid(row=5,column=3)

button_F=Button(frame,text='F',width=6,height=3,bg="white")
button_F.grid(row=5,column=4)

button_G=Button(frame,text='G',width=6,height=3,bg="white")
button_G.grid(row=5,column=5)

button_H=Button(frame,text='H',width=6,height=3,bg="white")
button_H.grid(row=5,column=6)

button_J=Button(frame,text='J',width=6,height=3,bg="white")
button_J.grid(row=5,column=7)

button_K=Button(frame,text='k',width=6,height=3,bg="white")
button_K.grid(row=5,column=8)

button_L=Button(frame,text='l',width=6,height=3,bg="white")
button_L.grid(row=5,column=9)

button_colon=Button(frame,text=";",width=6,height=3,bg="white")
button_colon.grid(row=5,column=10)

button_quote=Button(frame,text="'",width=6,height=3,bg="white")
button_quote.grid(row=5,column=11)

button_enter=Button(frame,text='enter',width=12,height=3,bg="white")
button_enter.grid(row=5,column=12)

button_down=Button(frame,text='pg dn',width=6,height=3,bg="white")
button_down.grid(row=5,column=15)


# SHIFT ROW

button_shift=Button(frame,text='shift',width=12,height=3,bg="white")
button_shift.grid(row=6,column=0,pady=5)

button_Z=Button(frame,text='Z',width=6,height=3,bg="white")
button_Z.grid(row=6,column=1)

button_X=Button(frame,text='X',width=6,height=3,bg="white")
button_X.grid(row=6,column=2)

button_C=Button(frame,text='C',width=6,height=3,bg="white")
button_C.grid(row=6,column=3)

button_V=Button(frame,text='V',width=6,height=3,bg="white")
button_V.grid(row=6,column=4)

button_B=Button(frame,text='B',width=6,height=3,bg="white")
button_B.grid(row=6,column=5)

button_N=Button(frame,text='N',width=6,height=3,bg="white")
button_N.grid(row=6,column=6)

button_M=Button(frame,text='M',width=6,height=3,bg="white")
button_M.grid(row=6,column=7)

button_comma=Button(frame,text=',',width=6,height=3,bg="white")
button_comma.grid(row=6,column=8)

button_stop=Button(frame,text='.',width=6,height=3,bg="white")
button_stop.grid(row=6,column=9)

button_slash=Button(frame,text="/",width=6,height=3,bg="white")
button_slash.grid(row=6,column=10)

button_shiftR=Button(frame,text='shift',width=12,height=3,bg="white")
button_shiftR.grid(row=6,column=13, columnspan=2)

button_end=Button(frame,text='end',width=6,height=3,bg="white")
button_end.grid(row=6,column=15)


#space row

control1=Button(frame,text='ctrl',width=6,height=2,bg="white")
control1.grid(row=7,column=1)

find=Button(frame,text='fn',width=6,height=2,bg="white")
find.grid(row=7,column=2)

windows=Button(frame,text='wind',width=6,height=2 ,bg="white", state=DISABLED)
windows.grid(row=7,column=3)

alt1=Button(frame,text='alt',width=6,height=2,bg="white")
alt1.grid(row=7,column=4)

space=Button(frame,text='space',width=6,height=2,bg="white")
space.grid(row=7,column=5)

alt2=Button(frame,text='alt',width=6,height=2,bg="white")
alt2.grid(row=7,column=6)

page=Button(frame,text='pg',width=6,height=2,bg="white")
page.grid(row=7,column=7)

ctrl2=Button(frame,text='ctrl',width=6,height=2,bg="white")
ctrl2.grid(row=7,column=8)

west=Button(frame,text='<',width=6,height=2,bg="white")
west.grid(row=7,column=9)

north=Button(frame,text='north',width=6,height=2,bg="white")
north.grid(row=7,column=10)

east=Button(frame,text='>',width=6,height=2,bg="white")
east.grid(row=7,column=11)

root.mainloop()
