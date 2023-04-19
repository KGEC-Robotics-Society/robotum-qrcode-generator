#============================================= All imports
import os
import qrcode
import tkinter as tk
from tkinter import *
from tkinter import Checkbutton, IntVar, filedialog
from PIL import Image, ImageTk

#============================================= Tkinter GUI
root = Tk()
root.title("QR Code Maker")
root.geometry('1100x650')
root.iconbitmap("images/robot.ico")
root.resizable(False,False)
root.configure(background="purple")

#============================================= Background Image
image = Image.open('images/optimised1.png')
photo_image = ImageTk.PhotoImage(image)
label = tk.Label(root, image = photo_image)
label.pack()

#============================================= Initialization
off_color = "red"
on_color = "green"
strva = StringVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()

#============================================= Functions
#==================== Name
def ntext(*args):
    if len(name.get()) <3:
        btn["fg"]=off_color
    else:
        btn["fg"]=on_color
    return name.get()

#==================== App Devolopment
def cmd1():
    AppD = var1.get()
    if AppD == 1:
        var1.set(0)
        appd["fg"] = off_color
        appd.deselect()
    elif AppD == 0:
        var1.set(1)
        appd.select()
        appd["fg"] = on_color
    print("self.var1 is", AppD)
    return AppD

#==================== IOT
def cmd2():
    IoT = var2.get()
    if IoT == 1:
        var2.set(0)
        iot.deselect()
        iot["fg"] = off_color
    elif IoT == 0:
        var2.set(1)
        iot.select()
        iot["fg"] = on_color
    print("self.var2 is", IoT)
    return IoT

#==================== Cloud Devolopement
def cmd3():
    CD = var3.get()
    if CD == 1:
        var3.set(0)
        cd.deselect()
        cd["fg"] = off_color
    elif CD == 0:
        var3.set(1)
        cd.select()
        cd["fg"] = on_color
    print("self.var3 is", CD)
    return CD

#==================== Machine Learning
def cmd4():
    ML = var4.get()
    if ML == 1:
        var4.set(0)
        ml.deselect()
        ml["fg"] = off_color
    elif ML == 0:
        var4.set(1)
        ml.select()
        ml["fg"] = on_color
    print("self.var4 is", ML)
    return ML

#==================== Mechatronics
def cmd5():
    Mecha = var5.get()
    if Mecha == 1:
        var5.set(0)
        mecha.deselect()
        mecha["fg"] = off_color
    elif Mecha == 0:
        var5.set(1)
        mecha.select()
        mecha["fg"] = on_color
    print("self.var5 is", Mecha)
    return Mecha

#==================== Web Devolopement
def cmd6():
    WebD = var6.get()
    if WebD == 1:
        var6.set(0)
        webd.deselect()
        webd["fg"] = off_color
    elif WebD == 0:
        var6.set(1)
        webd.select()
        webd["fg"] = on_color
    print("self.var6 is", WebD)
    return WebD

#==================== Design
def cmd7():
    Des = var7.get()
    if des == 1:
        var7.set(0)
        des.deselect()
        des["fg"] = off_color
    elif Des == 0:
        var7.set(1)
        des.select()
        des["fg"] = on_color
    print("self.var6 is", Des)
    return Des

#==================== Video Editor
def cmd8():
    Vid = var8.get()
    if Vid == 1:
        var8.set(0)
        vid.deselect()
        vid["fg"] = off_color
    elif Vid == 0:
        var8.set(1)
        vid.select()
        vid["fg"] = on_color
    print("self.var6 is", Vid)
    return Vid

#==================== Content Writing
def cmd9():
    Cont = var9.get()
    if Cont == 1:
        var9.set(0)
        cont.deselect()
        cont["fg"] = off_color
    elif Cont == 0:
        var9.set(1)
        cont.select()
        cont["fg"] = on_color
    print("self.var6 is", Cont)
    return Cont

#==================== Save
def save():
    Name=ntext()
    AppD=cmd1()
    IoT=cmd2()
    CD=cmd3()
    ML=cmd4()
    Mecha=cmd5()
    WebD=cmd6()
    Des=cmd7()
    Vid=cmd8()
    Cont=cmd9()
    if AppD == 1:
        AppD="no"
    else:
        AppD="yes"
    if IoT == 1:
        IoT="no"
    else:
        IoT="yes"
    if CD == 1:
        CD="no"
    else:
        CD="yes"
    if ML == 1:
        ML="no"
    else:
        ML="yes"
    if Mecha == 1:
        Mecha="no"
    else:
        Mecha="yes"
    if WebD == 1:
        WebD="no"
    else:
        WebD="yes"
    if Des == 1:
        Des="no"
    else:
        Des="yes"
    if Vid == 1:
        Vid="no"
    else:
        Vid="yes"
    if Cont == 1:
        Cont="no"
    else:
        Cont="yes"    
    qr= qrcode.QRCode(version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4)
    qr.add_data(f'Name:"{Name}", app:"{AppD}", iot:"{IoT}", ml:"{ML}", cloud:"{CD}", mechatronics:"{Mecha}", web:"{WebD}", design:"{Des}", video:"{Vid}", content:"{Cont}"')
    qr.make(fit=True)
    # create QR image
    qr_img = qr.make_image(back_color="transperent")
    # open logo image
    logo = Image.open("images/kgec_rs.png")
    # resize logo to fit in the QR code
    logo_w, logo_h = logo.size
    qr_w, qr_h = qr_img.size
    logo_size = int(qr_w / 4)
    logo = logo.resize((logo_size, logo_size), resample=Image.LANCZOS)
    # add logo to QR code
    pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)
    qr_img.paste(logo, pos)
    if qr_img.mode != "RGBA":
            qr_img = qr_img.convert("RGBA")
    txt = Image.new('RGBA', qr_img.size, (255,255,255,0))
    files = [("PNG file", "*.png"),
             ('All Files', '*.*')]
    file = filedialog.asksaveasfile(filetypes = files, mode='w', defaultextension=".png")
    if file:
        abs_path = os.path.abspath(file.name)
        out = Image.alpha_composite(qr_img, txt)
        out.save(abs_path)
    
#============================================= GUI Buttons and Lables
name_text= Label(root, text= 'Name : ',  state="disabled", background= "black", foreground= "white", font=max)
name_text.place(x=200, y=105, relwidth=.3, relheight=.08, anchor="center")

name = Entry(root, text="Enter Name", background= "black", foreground= "white", insertbackground="white", font=max, textvariable=strva)
name.place(x=420, y=80, relwidth=.3, relheight=.08)
strva.trace('w', ntext)
name.focus_set()

appd = Checkbutton(root, text='App Development ', variable=var1, command=cmd1, background= "black", foreground= on_color, onvalue=0, offvalue=1)
appd.place(x=580, y=200, relwidth=.3, relheight=.08, anchor="center")
iot = Checkbutton(root, text='Internet of things ', variable=var2, command=cmd2, background= "black", foreground= on_color, onvalue=0, offvalue=1)
iot.place(x=580, y=240, relwidth=.3, relheight=.08, anchor="center")
cd = Checkbutton(root, text='Cloud Computing ', variable=var3, command=cmd3, background= "black", foreground= on_color, onvalue=0, offvalue=1)
cd.place(x=580, y=280, relwidth=.3, relheight=.08, anchor="center")
ml = Checkbutton(root, text='Machine Learning ', variable=var4, command=cmd4, background= "black", foreground= on_color, onvalue=0, offvalue=1)
ml.place(x=580, y=320, relwidth=.3, relheight=.08, anchor="center")
mecha = Checkbutton(root, text='Mechatronics ', variable=var5, command=cmd5, background= "black", foreground= on_color, onvalue=0, offvalue=1)
mecha.place(x=580, y=360, relwidth=.3, relheight=.08, anchor="center")
webd = Checkbutton(root, text='Web Development ', variable=var6, command=cmd6, background= "black", foreground= on_color, onvalue=0, offvalue=1)
webd.place(x=580, y=400, relwidth=.3, relheight=.08, anchor="center")
des = Checkbutton(root, text='Graphics Design ', variable=var7, command=cmd7, background= "black", foreground= on_color, onvalue=0, offvalue=1)
des.place(x=580, y=440, relwidth=.3, relheight=.08, anchor="center")
vid = Checkbutton(root, text='Video Editor ', variable=var8, command=cmd8, background= "black", foreground= on_color, onvalue=0, offvalue=1)
vid.place(x=580, y=480, relwidth=.3, relheight=.08, anchor="center")
cont = Checkbutton(root, text='Content Writer ', variable=var9, command=cmd9, background= "black", foreground= on_color, onvalue=0, offvalue=1)
cont.place(x=580, y=520, relwidth=.3, relheight=.08, anchor="center")

btn= Button(root, text="Save QR code", background= "black", foreground= off_color, font=max, command=save)
btn.place(x=850, y=80, relwidth=.15, relheight=.08)

#============================================= Tkinter Looping
root.mainloop()