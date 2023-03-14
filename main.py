import json
import tkinter as tk
from types import SimpleNamespace
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mp06uf3"]
mycol = mydb["coleccio"]
print(mydb.list_collection_names())


class producte:
    def __init__(self, nom, preu, descripcio, descripcio_llarga, destacat, valoracio, imatge):
        self.nom, self.preu, self.descripcio, self.descripcio_llarga, self.destacat, self.valoracio, self.imatge = nom, preu, descripcio, descripcio_llarga, destacat, valoracio, imatge





def botoInserir():

        arrayJsons.clear()
        lbl_error.config(text="")
        with open('productes.json') as fitxer:
            json_02 = json.load(fitxer)
            print("JSON llegit des de fitxer: ", json_02)
            for pepe in json_02:
                arrayJsons.append(pepe)
        try:
            preuFloat = float(ent_preu.get())
        except ValueError:
            lbl_error.config(text="El preu te que ser un número!!")
        try:
            intValoracio= int(ent_valoracio.get())
            if (intValoracio >= 0) and (intValoracio < 6) :
                valoracioFloat = float(ent_valoracio.get())
            else:
                lbl_error.config(text="El número de valoració te que estar entre el 0 i el 5!!")

        except ValueError:
            lbl_error.config(text="La valoració te que ser un número!!")
        try:
            if len(ent_nom.get())>0 or len(ent_descripcio.get())>0 or len(ent_descripcio_llarga.get())>0 or len(ent_preu.get())>0 or len(ent_valoracio.get())>0 or len(ent_imatge.get())>0:
                if __name__ == '__main__':
                    prod = producte(ent_nom.get(), preuFloat, ent_descripcio.get(), ent_descripcio_llarga.get(),
                                    destacat.get(), valoracioFloat, ent_imatge.get())
                    json_prod = json.dumps(prod.__dict__)
                    print(json_prod)
                    arrayJsons.append(json_prod)
            else:
                lbl_error.config(text="No et deixes cap casella buida!")
        except Exception:
            pass



        with open('productes.json', 'w') as fitxer:
            json.dump(arrayJsons, fitxer)




window = tk.Tk()
window.title('AleixC')
destacat = tk.BooleanVar()
arrayJsons = []
#Labels
lbl_nom = tk.Label(master=window, text="Nom", )
lbl_preu = tk.Label(master=window, text="Preu", )
lbl_descripcio = tk.Label(master=window, text="Descripció", )
lbl_descripcio_llarga = tk.Label(master=window, text="Descripció llarga", )
lbl_destacat = tk.Label(master=window, text="Destacat", )
lbl_valoracio = tk.Label(master=window, text="Valoració", )
lbl_imatge = tk.Label(master=window, text="Imatge", )
lbl_error = tk.Label(master=window, text="", )

# Entrys
ent_nom = tk.Entry(master=window)
ent_preu = tk.Entry(master=window)
ent_descripcio = tk.Entry(master=window)
ent_descripcio_llarga = tk.Entry(master=window)
check_destacat = tk.Checkbutton(window, text="", variable=destacat,
               onvalue=True, offvalue=False)
ent_valoracio = tk.Entry(master=window)
ent_imatge = tk.Entry(master=window)
# Botons
btn_inserir = tk.Button(master=window, text="Guardar", command=botoInserir, width="15")


# Enters i labels
lbl_nom.grid(row=0, column=0)
ent_nom.grid(row=0, column=1)

lbl_preu.grid(row=1, column=0)
ent_preu.grid(row=1, column=1)

lbl_descripcio.grid(row=2, column=0)
ent_descripcio.grid(row=2, column=1)

lbl_descripcio_llarga.grid(row=3, column=0)
ent_descripcio_llarga.grid(row=3, column=1)


lbl_valoracio.grid(row=4, column=0)
ent_valoracio.grid(row=4, column=1)

lbl_imatge.grid(row=5, column=0)
ent_imatge.grid(row=5, column=1)

lbl_destacat.grid(row=6, column=0)
check_destacat.grid(row=6, column=1)

lbl_error.grid(row=8, column=0)
# Botons
btn_inserir.grid(row=7, column=1)


window.mainloop()