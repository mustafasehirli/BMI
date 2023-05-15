import tkinter


window = tkinter.Tk()
window.title("BMI")
window.minsize(width=300, height=300)


def click_btn():
    if inp_kg.get() == "":
        kg = 1
    else:
        kg = int(inp_kg.get())

    if inp_cm.get() == "":
        cm = 1
    else:
        cm = float(inp_cm.get())

    result_txt = kg / (cm * cm)
    message = result(result_txt)
    mes.config(text=f"{message}")


txt_kg = tkinter.Label(text="Kilosunuzu Giriniz.", pady=10, padx=10)
txt_kg.pack()


inp_kg = tkinter.Entry()
inp_kg.pack()


txt_kg = tkinter.Label(text="Boyunuzu Giriniz.", pady=10, padx=10)
txt_kg.config(padx=30)
txt_kg.pack()

inp_cm = tkinter.Entry()
inp_cm.pack()

result_btn = tkinter.Button(text="Result", padx=10, command=click_btn)
result_btn.pack()

mes = tkinter.Label()
mes.pack()


def result(index):
    message = ""

    if index < 18:
        message = "ideal kilonun altında"

    elif 18 < index < 25:
        message = "İdeal kiloda"

    elif 25 < index < 30:
        message = "İdeal kilonun üzerinde"

    elif 30 < index < 40:
        message = "İdeal kilonun ÇOK üzerinde (OBEZ)"

    else:
        message = "Boş Alan Bırakmayınız"

    return message


window.mainloop()
