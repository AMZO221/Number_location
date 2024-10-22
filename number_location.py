
from tkinter import*
from PIL import Image, ImageTk
import phonenumbers
from phonenumbers import geocoder

fen = Tk()
fen.title("NUMBER LOCATION")
# fen.geometry("400x500")
fen.minsize(400,500)
fen.maxsize(400,500)
fen['bg'] = "#FDA172"
fen.iconbitmap(r"C:\Users\HP\Desktop\BUREAU\mes projets\python fill\code  pays\phone.ico")

# Charger l'image
image = Image.open(r"C:\Users\HP\Desktop\BUREAU\mes projets\python fill\code  pays\telephone.jpeg")
photo = ImageTk.PhotoImage(file="C:\\Users\\HP\\Desktop\\BUREAU\\mes projets\\python fill\\code  pays\\telephone.jpeg")
# Créer un label pour l'image en arrière-plan
label_image1 = Label(fen, image=photo,width=400,height=70)
label_image1.pack(padx=0,pady=0)  # Prendre tout l'espace

label_image2 = Label(fen, image=photo,width=400,height=150)
label_image2.place(x=0,y=350)

numero = StringVar()
titre = Label(fen, text="BIENVENU",bg="#FDA172",
            font=("verdana",17,"bold")).pack()

presentation = Label(fen,text="Ceci est un programme qui permet\nde savoir le  Pays auquel est associé\nle code indicatif d'un numero de téléphone\n",
                    font=("arial",10),
                    bg="#FDA172").pack(padx=20)

text_num= Label(fen, text="VEILLEZ ENTRER UN NUMERO DE TÉLÉPHONE",
            font=("verdana",10,"bold"),
            bg="#FDA172").pack()
enter_num= Entry(fen,text=numero,
                border=1,
                highlightthickness=3).place(x=100,y=210,width=200,height=30)

def localiser():
    #print(geocoder.description_for_number(num1,"fr"))
    try:
        num1 = phonenumbers.parse(numero.get())
        msg=Label(fen,text=geocoder.description_for_number(num1,"fr"),
            font=("arial",14,"bold"),
            bg="#FDA172").place(x=155,y=285)
    except phonenumbers.phonenumberutil.NumberParseException:
        msg=Label(fen,text="NUMÉRO INVALIDE",
            font=("arial",10),
            bg="#FDA172",fg="red").place(x=140,y=320)
boutton = Button(fen,text="ENTER",bg="#4065A4",
                command=localiser).place(x=150,y=250,width=100,height=30)

fen.mainloop()