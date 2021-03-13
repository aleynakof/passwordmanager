import string
import random


def sifre_uret():
    kucuk_harfler = list(string.ascii_lowercase)
    buyuk_harfler = list(string.ascii_uppercase)
    # concatenate ederken sorun çıkarmaması için stringe aldık
    rakamlar = list(string.digits)
    isaretler = list(string.punctuation)

    no_buyuk_harf = random.randint(1, 2)
    # print(no_buyuk_harf)
    no_kucuk_harf = random.randint(2, 3)
    no_rakamlar = random.randint(1, 2)
    no_isaretler = random.randint(2, 4)

    password_list = []
    for i in range(no_buyuk_harf):
        password_list.append(random.choice(buyuk_harfler))

    for i in range(no_kucuk_harf):
        password_list.append(random.choice(kucuk_harfler))

    for i in range(no_isaretler):
        password_list.append(random.choice(isaretler))

    for i in range(no_rakamlar):
        password_list.append(random.choice(rakamlar))

    random.shuffle(password_list)

    password = ""
    for c in password_list:
        password = password + c

    return password;


print(sifre_uret())
