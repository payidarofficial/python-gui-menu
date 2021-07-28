# Öncelikle "tkinter" Paketini Kurmanız Gerekiyor.
# Kurulum İçin "pip install tkinter" :)

# -------------------------------------------------------------- #
# Pâyidar Tarafından Kodlanmıştır.                               #
# -------------------------------------------------------------- #

import tkinter as tk 
from tkinter import *

# Arayüz Oluşturalım
pencere = tk.Tk()
pencere.title('Pâyidar Menu')
pencere.geometry("500x250")

# Def
def fonksiyon():
    yazi = Label(pencere, text="https://instagram.com/06.kadirx").pack()
def fonksiyon_2():
    yazi = Label(pencere, text="https://discord.gg/PhPEsF8qYE").pack()
def fonksiyon_3():
    yazi = Label(pencere, text="https://twitter.com/payidarorjinal").pack()
def menuexit():
    yazi = Label(pencere, text="Menü Kapatıldı").pack()

# Menü Oluşturalım
payidar_menu = Menu(pencere)

payidar = Menu(payidar_menu, tearoff = 0)
payidar.add_command(label="İnstagram",command=fonksiyon)
payidar.add_command(label="Discord",command=fonksiyon_2)
payidar.add_command(label="Twitter",command=fonksiyon_3)
payidar.add_separator()
payidar.add_command(label="Menüden Defol",command=menuexit)

payidar_menu.add_cascade(label="Sosyal Medya", menu=payidar)

# ortalama = Menu(payidar_menu,tearoff=0)
# ortalama.add_command(label="XD",command=fonksiyon)
# ortalama.add_command(label="XD2",command=fonksiyon_2)
# ortalama.add_command(label="XD3",command=fonksiyon_3)
# ortalama.add_separator()
# ortalama.add_command(label="XXX",command=menuexit)

# payidar_menu.add_cascade(label="Düzen", menu=ortalama)

pencere.config(menu=payidar_menu)
pencere.mainloop()
