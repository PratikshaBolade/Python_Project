import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os


def selected():
    global img_path, img
    img_path = tk.filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas.create_image(300, 210, image=img1)
    canvas.image = img1


def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    ext = img_path.split(".")[-1]
    file = askopenfilename(defaultextension=f".{ext}", filetypes=[("All Files", "*.*"), ("PNG File", "*.png"),
                                                                  ("jpg File", "*.jpg"), ("jpeg file", "*.jpeg")])
    if file:
        if canvas.image == img1:
            imgg.save(file)
        elif canvas.image == img3:
            img2.save(file)
        elif canvas.image == img5:
            img4.save(file)
        elif canvas.image == img7:
            img6.save(file)
        elif canvas.image == img9:
            img8.save(file)
        elif canvas.image == img11:
            img10.save(file)


def blur(e):
    global img_path, img1, imgg
    for n in range(0, v1.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = img.filter(ImageFilter.BoxBlur(n))
        img1 = ImageTk.PhotoImage(imgg)
        canvas.create_image(300, 210, image=img1)
        canvas.image = img1


def contrast(e):
    global img_path, img4, img5
    for n in range(0, v2.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(img)
        img4 = imgg.enhance(n)
        img5 = ImageTk.PhotoImage(img4)
        canvas.create_image(300, 210, image=img5)
        canvas.image = img5


def rotate_image(e):
    global img_path, img6, img7
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img6 = img.rotate(int(rotate_combo.get()))
    img7 = ImageTk.PhotoImage(img6)
    canvas.create_image(300, 210, image=img7)
    canvas.image = img7


def flip_image(e):
    global img_path, img8, img9
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if flip_combo.get() == "FLIP LEFT TO RIGHT":
        img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_combo.get() == "FLIP TOP TO BOTTOM":
        img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img9 = ImageTk.PhotoImage(img8)
    canvas.create_image(300, 210, image=img9)
    canvas.image = img9


root = ttk.Window(themename='darkly')
my_label = ttk.Label(root, text="Photo Editor", font=('Helvetica', 20), bootstyle="Success", justify='center')
my_label.pack()
Blur = ttk.Label(root, text="Blur", font=("Ariel", 17, "bold"))
Blur.place(x=650, y=100)
v1 = ttk.IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur)
scale1.place(x=800, y=110)
Contrast = ttk.Label(root, text="Contrast", font=("Ariel", 17, "bold"))
Contrast.place(x=650, y=180)
v2 = ttk.IntVar()
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=contrast)
scale2.place(x=800, y=190)

Rotate = ttk.Label(root, text="Rotate", font=("Ariel", 17, "bold"))
Rotate.place(x=950, y=100)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=("Ariel", 10, "bold"))
rotate_combo.place(x=1060, y=100)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)
Flip = ttk.Label(root, text="Flip", font=("Ariel", 17, "bold"))
Flip.place(x=950, y=180)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=("Ariel", 10, "bold"))
flip_combo.place(x=1060, y=180)
flip_combo.bind("<<ComboboxSelected>>", flip_image)
canvas = ttk.Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas.place(x=650, y=300)
btn = ttk.Button(root, text="Select Image", bootstyle="info-outline", command=selected)
btn.place(x=750, y=800)
btn1 = ttk.Button(root, text="Save", width=12, bootstyle="info-outline", command=save)
btn1.place(x=900, y=800)
btn2 = ttk.Button(root, text="Exit", width=12, bootstyle="danger-outline", command=root.destroy)
btn2.place(x=1050, y=800)
root.mainloop()