from tkinter import *


root=Tk()
root.title("ASTRA TYPE")

monitor=LabelFrame(root,text='here is the monitor', padx=10,pady=20)
monitor.pack(padx=5, pady=10)

e=Entry(monitor)
e.pack()

def button_press (number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

frame=LabelFrame(root, text="astra type master", padx=15,pady=25)
frame.pack(padx=15,pady=25)


esc=Button(frame,text='esc',width=6,height=2)
esc.grid(row=2,column=0)

f1=Button(frame,text='f1',width=6,height=2)
f1.grid(row=2,column=1)

f2=Button(frame,text='f2',width=6,height=2)
f2.grid(row=2,column=2)

f3=Button(frame,text='f3',width=6,height=2)
f3.grid(row=2,column=3)

f4=Button(frame,text='f4',width=6,height=2)
f4.grid(row=2,column=4)

f5=Button(frame,text='f5',width=6,height=2)
f5.grid(row=2,column=5)

f6=Button(frame,text='f6',width=6,height=2)
f6.grid(row=2,column=6)

f7=Button(frame,text='f7',width=6,height=2)
f7.grid(row=2,column=7)

f8=Button(frame,text='f8',width=6,height=2)
f8.grid(row=2,column=8)

f9=Button(frame,text='f9',width=6,height=2)
f9.grid(row=2,column=9)

f10=Button(frame,text='f10',width=6,height=2)
f10.grid(row=2,column=10)

f11=Button(frame,text='f11',width=6,height=2)
f11.grid(row=2,column=11)

f12=Button(frame,text='f12',width=6,height=2)
f12.grid(row=2,column=12)

f13=Button(frame,text='insert',width=6,height=2)
f13.grid(row=2,column=13)

f14=Button(frame,text='prt scr',width=6,height=2)
f14.grid(row=2,column=14)

f15=Button(frame,text='delete',width=6,height=2)
f15.grid(row=2,column=15)


#numbers row

    

button_first=Button(frame,text='`',width=6,height=3)
button_first.grid(row=3,column=0)

button_1=Button(frame,text='1',width=6,height=3,command=lambda:button_press(1))
button_1.grid(row=3,column=1)

button_2=Button(frame,text='2',width=6,height=3 ,command=lambda:button_press(2))
button_2.grid(row=3,column=2)

button_3=Button(frame,text='3',width=6,height=3 ,command=lambda:button_press(3))
button_3.grid(row=3,column=3)

button_4=Button(frame,text='4',width=6,height=3 ,command=lambda:button_press(4))
button_4.grid(row=3,column=4)

button_5=Button(frame,text='5',width=6,height=3,command=lambda:button_press(5))
button_5.grid(row=3,column=5)

button_6=Button(frame,text='6',width=6,height=3 ,command=lambda:button_press(6))
button_6.grid(row=3,column=6)

button_7=Button(frame,text='7',width=6,height=3,command=lambda:button_press(7) )
button_7.grid(row=3,column=7)

button_8=Button(frame,text='8',width=6,height=3 ,command=lambda:button_press(8))
button_8.grid(row=3,column=8)

button_9=Button(frame,text='9',width=6,height=3,command=lambda:button_press(9))
button_9.grid(row=3,column=9)

button_10=Button(frame,text='0',width=6,height=3,command=lambda:button_press(0))
button_10.grid(row=3,column=10)

button_11=Button(frame,text='-',width=6,height=3,command=lambda:str(button_press("-")))
button_11.grid(row=3,column=11)

button_12=Button(frame,text='=',width=6,height=3,command=lambda:str(button_press("=")))
button_12.grid(row=3,column=12)

button_13=Button(frame,text='<',width=12,height=3)
button_13.grid(row=3,column=13,columnspan=2)

button_15=Button(frame,text='home',width=6,height=3)
button_15.grid(row=3,column=15)

# qwerty row

button_tab=Button(frame,text='tab',width=8,height=3)
button_tab.grid(row=4,column=0)

button_Q=Button(frame,text='Q',width=6,height=3,command=lambda:str(button_press("q")))
button_Q.grid(row=4,column=1)

button_W=Button(frame,text='W',width=6,height=3,command=lambda:str(button_press("w")))
button_W.grid(row=4,column=2)

button_E=Button(frame,text='E',width=6,height=3,command=lambda:str(button_press("e")))
button_E.grid(row=4,column=3)

button_R=Button(frame,text='R',width=6,height=3,command=lambda:str(button_press("r")))
button_R.grid(row=4,column=4)

button_T=Button(frame,text='T',width=6,height=3,command=lambda:str(button_press("t")))
button_T.grid(row=4,column=5)

button_Y=Button(frame,text='Y',width=6,height=3,command=lambda:str(button_press("y")))
button_Y.grid(row=4,column=6)

button_U=Button(frame,text='U',width=6,height=3,command=lambda:str(button_press("u")))
button_U.grid(row=4,column=7)

button_I=Button(frame,text='I',width=6,height=3,command=lambda:str(button_press("i")))
button_I.grid(row=4,column=8)

button_O=Button(frame,text='O',width=6,height=3,command=lambda:str(button_press("o")))
button_O.grid(row=4,column=9)

button_P=Button(frame,text='P',width=6,height=3,command=lambda:str(button_press("p")))
button_P.grid(row=4,column=10)

button_list1=Button(frame,text='[',width=6,height=3,command=lambda:str(button_press("[")))
button_list1.grid(row=4,column=11)

button_list2=Button(frame,text=']',width=6,height=3,command=lambda:str(button_press("]")))
button_list2.grid(row=4,column=12)

button_slash=Button(frame,text="|",width=6,height=3,command=lambda:str(button_press("|")))
button_slash.grid(row=4,column=13,columnspan=2)

button_up=Button(frame,text='pg up',width=6,height=3)
button_up.grid(row=4,column=15)


# home row;

button_caps=Button(frame,text='caps lock',width=8,height=3)
button_caps.grid(row=5,column=0)

button_A=Button(frame,text='A',width=6,height=3,command=lambda:str(button_press("a")))
button_A.grid(row=5,column=1)

button_S=Button(frame,text='S',width=6,height=3,command=lambda:str(button_press("s")))
button_S.grid(row=5,column=2)

button_D=Button(frame,text='D',width=6,height=3,command=lambda:str(button_press("d")))
button_D.grid(row=5,column=3)

button_F=Button(frame,text='F',width=6,height=3,command=lambda:str(button_press("f")))
button_F.grid(row=5,column=4)

button_G=Button(frame,text='G',width=6,height=3,command=lambda:str(button_press("g")))
button_G.grid(row=5,column=5)

button_H=Button(frame,text='H',width=6,height=3,command=lambda:str(button_press("h")))
button_H.grid(row=5,column=6)

button_J=Button(frame,text='J',width=6,height=3,command=lambda:str(button_press("j")))
button_J.grid(row=5,column=7)

button_K=Button(frame,text='k',width=6,height=3,command=lambda:str(button_press("k")))
button_K.grid(row=5,column=8)

button_L=Button(frame,text='l',width=6,height=3,command=lambda:str(button_press("l")))
button_L.grid(row=5,column=9)

button_colon=Button(frame,text=";",width=6,height=3,command=lambda:str(button_press(";")))
button_colon.grid(row=5,column=10)

button_quote=Button(frame,text="'",width=6,height=3,command=lambda:str(button_press("'")))
button_quote.grid(row=5,column=11)

button_enter=Button(frame,text='enter',width=12,height=3)
button_enter.grid(row=5,column=12)

button_down=Button(frame,text='pg dn',width=6,height=3)
button_down.grid(row=5,column=15)


# SHIFT ROW

button_shift=Button(frame,text='shift',width=12,height=3)
button_shift.grid(row=6,column=0)

button_Z=Button(frame,text='Z',width=6,height=3,command=lambda:str(button_press("z")))
button_Z.grid(row=6,column=1)

button_X=Button(frame,text='X',width=6,height=3,command=lambda:str(button_press("x")))
button_X.grid(row=6,column=2)

button_C=Button(frame,text='C',width=6,height=3,command=lambda:str(button_press("c")))
button_C.grid(row=6,column=3)

button_V=Button(frame,text='V',width=6,height=3,command=lambda:str(button_press("v")))
button_V.grid(row=6,column=4)

button_B=Button(frame,text='B',width=6,height=3,command=lambda:str(button_press("b")))
button_B.grid(row=6,column=5)

button_N=Button(frame,text='N',width=6,height=3,command=lambda:str(button_press("n")))
button_N.grid(row=6,column=6)

button_M=Button(frame,text='M',width=6,height=3,command=lambda:str(button_press("m")))
button_M.grid(row=6,column=7)

button_comma=Button(frame,text=',',width=6,height=3,command=lambda:str(button_press(",")))
button_comma.grid(row=6,column=8)

button_stop=Button(frame,text='.',width=6,height=3,command=lambda:str(button_press(".")))
button_stop.grid(row=6,column=9)

button_slash=Button(frame,text="/",width=6,height=3,command=lambda:str(button_press("/")))
button_slash.grid(row=6,column=10)

button_shift2=Button(frame,text='shift',width=12,height=3)
button_shift2.grid(row=6,column=13, columnspan=2)

button_end=Button(frame,text='end',width=6,height=3)
button_end.grid(row=6,column=15)


#space row

control1=Button(frame,text='ctrl',width=6,height=2)
control1.grid(row=7,column=1)

find=Button(frame,text='fn',width=6,height=2)
find.grid(row=7,column=2)

windows=Button(frame,text='wind',width=6,height=2 , state=DISABLED)
windows.grid(row=7,column=3)

alt1=Button(frame,text='alt',width=6,height=2)
alt1.grid(row=7,column=4)

space=Button(frame,text='space',width=6,height=2)
space.grid(row=7,column=5)

alt2=Button(frame,text='alt',width=6,height=2)
alt2.grid(row=7,column=6)

page=Button(frame,text='pg',width=6,height=2)
page.grid(row=7,column=7)

ctrl2=Button(frame,text='ctrl',width=6,height=2)
ctrl2.grid(row=7,column=8)

west=Button(frame,text='<',width=6,height=2)
west.grid(row=7,column=9)

north=Button(frame,text='north',width=6,height=2)
north.grid(row=7,column=10)

east=Button(frame,text='>',width=6,height=2)
east.grid(row=7,column=11)












root.mainloop()
