import tkinter as tk
from tkinter import ttk
import neutro as neu
import atraccion as atrac
import repolcion as repul

"""
variables de particulas
    "proton",
    "electron",
    "neutron",
    "alfa",
    "positron",
    "deuterio",
    "muon",
    "tau",
    "tridio"
"""

proton = [1.6*(10**-19), 9.1*(10**-27), "blue"]
electron = [-1.6*(10**-19),9.10*(10**-31), "green"]
neutron = [0,1.67*(10**-27), "gray"]
alfa = [3.2*(10**-19), 6.65*(10**-27), "red"]
positron = [1.60*(10**-19), 9.11*(10**-31), "pink"]
deuterio = [1.6*(10**-19), 3.34*(10**-27), "purple"]
muon = [-1.6*(10**-19),1.88*(10**-28), "orange"]
tau = [-1.6*(10**-19), 2.76*(10**-29), "yellow"]
tridio = [1.6*(10**-19), 5.02*(10**-27), "brown"]


"""

funciones
"""
def asignar_particula(velocidad1,angulo1,particula1,tamanio1,fuerza1):
    if (angulo1<0 or angulo1 >90 or particula1 == "" or (particula1!= "electron" and particula1 != "proton" and particula1 != "neutron" 
        and particula1 != "alfa" and particula1 != "positron" and particula1 != "deuterio" and particula1 != "muon" and particula1 != "tau"
        and particula1 != "tridio")):

        window_error()
        
    if (particula1 == "electron"):
        datos_particula = electron
    if (particula1 == "proton"):
        datos_particula = proton
    if (particula1 == "neutron"):
        datos_particula = neutron
    if (particula1 == "alfa"):
        datos_particula = alfa
    if (particula1 == "positron"):
        datos_particula = positron
    if (particula1 == "deuterio"):
        datos_particula = deuterio
    if (particula1 == "muon"):
        datos_particula = muon
    if (particula1 == "tau"):
        datos_particula = tau
    if (particula1 == "tridio"):
        datos_particula = tridio

    if (datos_particula[0] == 0 or fuerza1 == 0):
        neu.valores(datos_particula,velocidad1,angulo1,tamanio1,fuerza1)
    
    elif((datos_particula[0]>0 and fuerza1 < 0) or (datos_particula[0]<0 and fuerza1 > 0) ):
        atrac.valores(datos_particula,velocidad1,angulo1,tamanio1,fuerza1)

    elif((datos_particula[0]<0 and fuerza1 < 0) or (datos_particula[0]>0 and fuerza1 > 0)):
        repul.repulcion(datos_particula,velocidad1,angulo1,tamanio1,fuerza1)



def get_values():
    try:
        velocidad1 = float(velocidad_inicial.get())
        angulo1 = float(angulo_inicial.get())
        particula1 = combo_particulas.get()
        tamanio1 = float(placa_tamanio.get())
        fuerza1 = float(fuerza_electrica.get())

        #asignar_particula(velocidad1,angulo1,particula1,tamanio1,fuerza1)

    except:
        window_error()
    
    if (velocidad_inicial.get() != "" and angulo_inicial.get() != "" and combo_particulas.get() != "" and placa_tamanio.get() != "" and fuerza_electrica != ""):
        asignar_particula(velocidad1,angulo1,particula1,tamanio1,fuerza1)



def clear():
    velocidad_inicial.delete(0, "end")
    angulo_inicial.delete(0, "end")
    combo_particulas.delete(0,"end")
    placa_tamanio.delete(0,"end")
    fuerza_electrica.delete(0,"end")



def window_error ():

    clear()

    error = tk.Tk()
    error.title("ERROR")
    #error.iconbitmap("icono.ico")
    
    tipo_error = tk.LabelFrame( error, pady = "10")
    tk.Label(tipo_error, text = "Ingreso mal o dejo en blanco datos.").grid(row = "0", column = "0", sticky = "e",padx= "10", pady= "10")

    tipo_error.pack()

    error.mainloop()



top = tk.Tk()
"""
titulo
"""
top.title("Proyecto 1 Fisica")
#top.iconbitmap ("icono.ico")


"""
tananio de la ventana
"""
#top.geometry("400x400")
top.resizable(0,0)

"""
frame del titulo
"""
titulo_frame = tk.Frame()
titulo_frame.pack(side = "top")
titulo_frame.config(
    width = "600",
    height = "600",
    pady = "30"
    )
titulo_frame.config( relief="sunken")



"""
textos
"""
titulo = tk.Label(titulo_frame, text = "Simulador de partícula cargada", font=("Comic Sans MS",18))
titulo2 = tk.Label(titulo_frame, text = "en campo eléctrico uniforme.",font=("Comic Sans MS",18))
titulo.pack(side = "top")
titulo2.pack(side = "top")
titulo2 = tk.Label(titulo_frame, text = "",font=("Comic Sans MS",18),pady = "10")
titulo.pack(side = "top")



"""
---------PARTICULA--------
"""


label_frame_particula = tk.LabelFrame( text = "particula", pady = "10")

"""
textos para particulas
"""
tk.Label(label_frame_particula, text = "Velocidad Inicial:").grid(row = "0", column = "0", sticky = "e",padx= "10", pady= "10")
tk.Label(label_frame_particula, text = "m/s").grid(row = "0", column = "2", sticky = "w")
tk.Label(label_frame_particula, text = "Angulo Inicial:").grid(row = "1", column = "0", sticky = "e",padx= "10", pady= "10")
tk.Label(label_frame_particula, text = "grados").grid(row= "1", column = "2",sticky = "w")
tk.Label(label_frame_particula, text = "particula/nucleo:").grid(row = "2", column = "0", sticky = "e", padx = "10", pady = "10")




"""
entradas particulas
"""
velocidad_inicial = tk.Entry(label_frame_particula)
velocidad_inicial.grid(row = "0", column = "1",padx= "10", pady= "10")

angulo_inicial = tk.Entry(label_frame_particula)
angulo_inicial.grid(row = "1", column = "1",padx= "10", pady= "10")

combo_particulas = ttk.Combobox(label_frame_particula,values = [
    "proton",
    "electron",
    "neutron",
    "alfa",
    "positron",
    "deuterio",
    "muon",
    "tau",
    "tridio"
])
combo_particulas.grid (row = "2", column = "1", padx= "10", pady = "10")


label_frame_particula.pack()



"""
frame del titulo
"""
espacio = tk.Frame()
espacio.pack(side = "top")
espacio.config(
    width = "25",
    height = "25",
    pady = "20"
    )
espacio.config( relief="sunken")






"""
campo electrico
"""
label_frame_campo = tk.LabelFrame( text = "Campo Electrico", pady = "10")

tk.Label(label_frame_campo, text = "Tamaño de placa:").grid(row = "0", column = "0", sticky = "e",padx= "10", pady= "10")
tk.Label(label_frame_campo, text= "m").grid(row = "0", column = "2", sticky = "w")
tk.Label(label_frame_campo, text = "Campo Electrico:").grid(row = "1", column = "0", sticky = "e",padx= "10", pady= "10")
tk.Label(label_frame_campo, text = "N/C").grid(row = "1", column = "2", sticky = "w")

placa_tamanio = tk.Entry(label_frame_campo)
placa_tamanio.grid(row = "0", column = "1",padx= "10", pady= "10")

fuerza_electrica = tk.Entry(label_frame_campo)
fuerza_electrica.grid(row = "1", column = "1",padx= "10", pady= "10")

label_frame_campo.pack()



"""
espacio
"""
espacio2 = tk.Frame()
espacio2.pack(side = "top")
espacio2.config(
    width = "25",
    height = "25",
    pady = "20"
    )
espacio2.config( relief="sunken")





"""
boton para obtener los datos
"""

tk.Button(text = "Iniciar",command = get_values, pady = "10", padx = "10").pack()





"""
espacio
"""
espacio3 = tk.Frame()
espacio3.pack(side = "top")
espacio3.config(
    width = "25",
    height = "25",
    pady = "20"
    )
espacio3.config( relief="sunken")










top.mainloop()