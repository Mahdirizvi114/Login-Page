from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("1000x500")
root.title("Login Page")

En1 = Entry(root, width=30)
En1.place(x=700, y=130)

En2 = Entry(root, width=30)
En2.place(x=700, y=170)

Bt1 = Button(root, text="Log in", bg="#1877F2", fg="white", width=25, height=1, font="Arial 9")
Bt1.place(x=700, y=215)

Bt2 = Button(root, text="Create New Account", bg="#66CD00", fg="white", width=18, height=1, font="Arial 9")
Bt2.place(x=725, y=320)

Lb1 = Label(root, text="Forgot Password?", fg="#1877F2")
Lb1.place(x=745, y=260)

Lb2 = Label(root, text="------------------------------------------")
Lb2.place(x=685, y=290)

Lb3 = Label(root, text="Create A Page For Celebrity, Brand Or Business")
Lb3.place(x=670, y=400)

Lb4 = Label(root, text="facebook", fg="#1877F2", font="Arial 25 bold")
Lb4.place(x=100, y=80)

Lb5 = Label(root, text="Recent Logins", font="Arial 17")
Lb5.place(x=100, y=130)

Lb6 = Label(root, text="Click Your Picture Or Add An Account.", fg="grey")
Lb6.place(x=100, y=159)

Image = Image.open("1.png")
Photo = ImageTk.PhotoImage(Image)
ImgLabel = Label(root, image=Photo)
ImgLabel.place(x=100, y=200)

root.mainloop()