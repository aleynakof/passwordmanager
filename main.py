from tkinter import *
from tkinter import messagebox
import password


# ---------------- Functions Part
def generate_password():
    password_text.set("")
    password_text.set(password.sifre_uret())


def center_window(w=300, h=300):
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="uyarı", message="boş alanları geçemezsin!")
    else:
        sonuc = messagebox.askokcancel(title=website, message=f"These info is entered:\n"f"Email:{email}\n"f"Password:{password}\n"f"Are you sure to save?")
        with open("data.txt", "a") as data_file:
            # another way of formatting
            data_file.write(f"{website} | {email} | {password}\n")
        messagebox.showinfo(title=website, message="Your info is saved successfully")

        clear()


def clear():
    website_text.set("")
    # email_text.set("")
    password_text.set("")


# ---------------- UI Part

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
generate_password_button = Button(text="generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

center_window(500, 400)
window.mainloop()
