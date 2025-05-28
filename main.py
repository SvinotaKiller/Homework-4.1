from tkinter import *
from tkinter import ttk


#Создание окна
root = Tk()
root.title("Registration")
root.geometry("300x330")
root.resizable(False, False)


#Надпись сверху
auxiliary_label = ttk.Label(text="Форма регистрации")
auxiliary_label.pack(pady=10)


#Поле для ввода имени
name_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

name_label = ttk.Label(name_frame, text="Имя:")
name_label.pack(anchor=NW)

name_entry = ttk.Entry(name_frame)
name_entry.pack(anchor=W, fill=X)

name_frame.pack(fill=X, padx=25, pady=5)


#Поле для ввода фамилии
surname_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

surname_label = ttk.Label(surname_frame, text="Фамилия:")
surname_label.pack(anchor=NW)

surname_entry = ttk.Entry(surname_frame)
surname_entry.pack(anchor=W, fill=X)

surname_frame.pack(fill=X, padx=25, pady=10)


#Поле для ввода email'а
email_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

email_label = ttk.Label(email_frame, text="Email:")
email_label.pack(anchor=NW)

email_entry = ttk.Entry(email_frame)
email_entry.pack(anchor=W, fill=X)

email_frame.pack(fill=X, padx=25, pady=10)


#Переменные, в которые записываются данные
name = ""
surname = ""
email = ""


#Отправка данных
def processing_send_button():
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()

    print(f"{"="*30}\nДанные, которые ввёл пользователь:")
    print(f"-> Имя: \"{name}\"")
    print(f"-> Фамилия: \"{surname}\"")
    print(f"-> Email: \"{email}\"")
    print("="*30)

    #Очистка полей ввода
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    email_entry.delete(0, END)

    
#Кнопка отправить
send_button = ttk.Button(text="Отправить", command=processing_send_button)
send_button.pack(pady=8)



#Второе окно
second_root = Tk()
second_root.title("Switches")
second_root.geometry("200x130") 
second_root.resizable(False, False)


#Текст, который будет переключаться
switching_label = ttk.Label(second_root, text="Нажмите на одну из кнопок")
switching_label.pack(pady=15)


#Смена текста на "Привет!"
def changing_text_hello():
    switching_label.config(text="Привет!")


#Смена текста на "До свидания!"
def changing_text_goodbye():
    switching_label.config(text="До свидания!")


#Кнопка "Привет"
hello_button = ttk.Button(second_root, text="Привет", command=changing_text_hello)
hello_button.pack(ipadx=7)


#Кнопка "До свидания"
goodbye_button = ttk.Button(second_root, text="До свидания", command=changing_text_goodbye)
goodbye_button.pack(ipadx=5, pady=5)


second_root.mainloop()
root.mainloop()