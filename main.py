from tkinter import *


# ---------------- Fonksiyon Bölümü
def center_window(w=300, h=300):
    w = window.winfo_reqwidth()
    h = window.winfo_reqheight()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


# ---------------- UI Bölümü


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="lock-2.png")
canvas.create_image(100, 100, image=logo_img)
# canvas.pack() çok fazla kullanmayacağız,
# grid kullanımı daha yaygın.
# birden fazla buton vs içeren kompleks sistemlerde grid
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="E-mail/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


center_window(500, 500)
window.mainloop()
