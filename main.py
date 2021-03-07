from tkinter import *


# ---------------- Fonksiyon Bölümü
def center_window(w=300, h=300):
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


# ---------------- UI Bölümü


window = Tk()
window.title("Password Manager-v1.0")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="lock-2.png")
canvas.create_image(100, 100, image=logo_img)
# canvas.pack() çok fazla kullanmayacağız,
# grid kullanımı daha yaygın.
# birden fazla buton vs içeren kompleks sistemlerde grid
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky=E)
email_label = Label(text="E-mail/Username: ")
email_label.grid(row=2, column=0, sticky=E)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_text = StringVar()
website_entry = Entry(width=52, textvariable=website_text)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_text = StringVar()
email_text.set("aleynakof@gmail.com")
email_entry = Entry(width=52, textvariable=email_text)
email_entry.grid(row=2, column=1, columnspan=2)

password_text = StringVar()
password_entry = Entry(width=33, textvariable=password_text, show="*")
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="generate password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2)

center_window(500, 400)
window.mainloop()
