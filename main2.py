import json
import tkinter as tk
from tkinter import ttk, CENTER, RIGHT, BOTH, BOTTOM, END
from types import SimpleNamespace
import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mp06uf3"]
mycol = mydb["coleccio"]


class producte:
    def __init__(self, nom, preu, descripcio, descripcio_llarga, destacat, valoracio, imatge):
        self.nom, self.preu, self.descripcio, self.descripcio_llarga, self.destacat, self.valoracio, self.imatge = nom, preu, descripcio, descripcio_llarga, destacat, valoracio, imatge


def gestioElement():
    global preuFloat, valoracioFloat
    try:
        preuFloat = float(ent_preu.get())
    except ValueError:
        lbl_error.config(text="El preu te que ser un número!!")
    try:
        intValoracio = int(ent_valoracio.get())
        if (intValoracio >= 0) and (intValoracio < 6):
            valoracioFloat = float(ent_valoracio.get())
        else:
            lbl_error.config(text="El número de valoració te que estar entre el 0 i el 5!!")
        return preuFloat, valoracioFloat
    except ValueError:
        lbl_error.config(text="La valoració te que ser un número!!")
    except Exception:
        pass


def botoInserir():
    print(mydb.list_collection_names())
    gestioElement()
    try:
        if len(ent_nom.get()) > 0 or len(ent_descripcio.get()) > 0 or len(ent_descripcio_llarga.get()) > 0 or len(
                ent_preu.get()) > 0 or len(ent_valoracio.get()) > 0 or len(ent_imatge.get()) > 0:
            if __name__ == '__main__':
                product = producte(ent_nom.get(), preuFloat, ent_descripcio.get(), ent_descripcio_llarga.get(),
                                   destacat.get(), valoracioFloat, ent_imatge.get())
                mydict = product.__dict__
                x = mycol.insert_one(mydict)
                print(x)
                mostrarDades()

        else:
            lbl_error.config(text="No et deixes cap casella buida!")
    except Exception:
        pass

    with open('productes.json', 'w') as fitxer:
        json.dump(arrayJsons, fitxer)


def mostrarDades():
    try:
        for item in tree.get_children():
            tree.delete(item)
        for x in mycol.find():
            tree.insert('', 'end', text="1",
                        values=(
                        x.get("_id"), x.get("nom"), x.get("preu"), x.get("descripcio"), x.get("descripcio_llarga"),
                        x.get("valoracio"), x.get("imatge"), x.get("destacat")))
            tree.bind('<ButtonRelease-1>', selectItem)
    except Exception:
        pass


def botoEliminar():
    myquery = {"_id": ObjectId(ent_id.get())}
    mycol.delete_one(myquery)
    mostrarDades()


def botoActualitzar():
        gestioElement()
        myquery = {"_id": ObjectId(ent_id.get())}
        newvalues = {"$set": {"nom": ent_nom.get(), "preu": preuFloat, "descripcio": ent_descripcio.get(),
                              "descripcio_llarga": ent_descripcio_llarga.get(), "valoracio": valoracioFloat,
                              "imatge": ent_imatge.get(), "destacat": destacat.get()}}

        mycol.update_one(myquery, newvalues)

        # print "customers" after the update:
        for x in mycol.find():
            print(x)
            mostrarDades()



def selectItem(a):
    try:
        curItem = tree.focus()
        print(tree.item(curItem))
        text = tree.item(curItem)["values"]
        ent_id.delete(0, END)
        ent_nom.delete(0, END)
        ent_preu.delete(0, END)
        ent_descripcio.delete(0, END)
        ent_descripcio_llarga.delete(0, END)
        ent_valoracio.delete(0, END)
        ent_imatge.delete(0, END)
        check_destacat.deselect()

        ent_id.insert(0, text[0])
        ent_nom.insert(0, text[1])
        ent_preu.insert(0, text[2])
        ent_descripcio.insert(0, text[3])
        ent_descripcio_llarga.insert(0, text[4])
        ent_valoracio.insert(0, text[5])
        ent_imatge.insert(0, text[6])
        if text[7] == 'True':
            check_destacat.select()
    except Exception:
        pass


window = tk.Tk()
window.title('AleixC')
destacat = tk.BooleanVar()
arrayJsons = []
# tree
tree = ttk.Treeview(window,
                    column=("ID", "Nom", "Preu", "Descripció", "Descripció llarga", "Valoració", "Imatge", "Destacat"),
                    show='headings')
# Adding a vertical scrollbar to Treeview widget
treeScrollY = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=treeScrollY.set)
treeScrollY.grid(row=0, column=8, sticky="ns")
tree.grid(row=0, column=0, columnspan=8, sticky="nw")

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Nom")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Preu")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Descripció")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="Descripció llarga")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="Valoració")
tree.column("# 7", anchor=CENTER)
tree.heading("# 7", text="Imatge")
tree.column("# 8", anchor=CENTER)
tree.heading("# 8", text="Destacat")
# Labels
lbl_nom = tk.Label(master=window, text="Nom", )
lbl_preu = tk.Label(master=window, text="Preu", )
lbl_descripcio = tk.Label(master=window, text="Descripció", )
lbl_descripcio_llarga = tk.Label(master=window, text="Descripció llarga", )
lbl_destacat = tk.Label(master=window, text="Destacat", )
lbl_valoracio = tk.Label(master=window, text="Valoració", )
lbl_imatge = tk.Label(master=window, text="Imatge", )
lbl_error = tk.Label(master=window, text="", )
lbl_id = tk.Label(master=window, text="ID (Per esborrar i editar)", )

# Entrys
ent_nom = tk.Entry(master=window)
ent_preu = tk.Entry(master=window)
ent_descripcio = tk.Entry(master=window)
ent_descripcio_llarga = tk.Entry(master=window)
check_destacat = tk.Checkbutton(window, text="", variable=destacat,
                                onvalue=True, offvalue=False)
ent_valoracio = tk.Entry(master=window)
ent_imatge = tk.Entry(master=window)
ent_id = tk.Entry(master=window)
# Botons
btn_inserir = tk.Button(master=window, text="Inserir", command=botoInserir, width="15")
btn_eliminar = tk.Button(master=window, text="Eliminar", command=botoEliminar, width="15")
btn_actualitzar = tk.Button(master=window, text="Actualitzar", command=botoActualitzar, width="15")

# Enters i labels
tree.grid(row=0, column=0, columnspan=8, sticky="nw")
lbl_nom.grid(row=1, column=3, sticky="SE")
ent_nom.grid(row=1, column=4)

lbl_preu.grid(row=2, column=3, sticky="SE")
ent_preu.grid(row=2, column=4)

lbl_descripcio.grid(row=3, column=3, sticky="SE")
ent_descripcio.grid(row=3, column=4)

lbl_descripcio_llarga.grid(row=4, column=3, sticky="SE")
ent_descripcio_llarga.grid(row=4, column=4)

lbl_valoracio.grid(row=5, column=3, sticky="SE")
ent_valoracio.grid(row=5, column=4)

lbl_imatge.grid(row=6, column=3, sticky="SE")
ent_imatge.grid(row=6, column=4)

lbl_destacat.grid(row=7, column=3, sticky="SE")
check_destacat.grid(row=7, column=4)

lbl_id.grid(row=8, column=3, sticky="SE")
ent_id.grid(row=8, column=4)

lbl_error.grid(row=10, column=4, columnspan=2, sticky="nw")
# Botons
btn_inserir.grid(row=9, column=3, sticky="SE")
btn_eliminar.grid(row=9, column=4)
btn_actualitzar.grid(row=9, column=5, sticky="nw")
mostrarDades()
window.mainloop()
