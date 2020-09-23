import numpy as np
from vpython import *


"""
#----------------------------------------------------------------------------#

#particulas = carga , masa
particula = [-1.6*(10**-19),9.1*(10**-31)]

el plano esta en centimetros

#variables
velocidad_inicial=5*(10**6)
angulo_inicial = 90
campo_electrico = 714

en centimetros

largo_suelo = 0.06
#----------------------------------------------------------------------------#
"""

def valores (particula, velocidad_inicial,angulo_inicial,largo_suelo, campo_electrico):
        


    largo_suelo = largo_suelo*100

    #componentes de velocidades:
    velocidad_X = velocidad_inicial * np.cos(np.deg2rad(angulo_inicial))
    velocidad_Y = velocidad_inicial * np.sin(np.deg2rad(angulo_inicial))

    #aceleracion
    aceleracion = ((particula[0]*campo_electrico)/particula[1])

    #tiempo total
    tiempo_total =  (2*velocidad_Y)/(aceleracion*-1)

    #distancia total
    distancia_total = velocidad_X*tiempo_total*100


    #suleo
    suelo = box(
        pos= vector(largo_suelo/2,-1,0),
        size=vector(largo_suelo,1,10),
        color= color.green
        )

    #cañon
    canyon = cylinder(
        pos = vector(0,0,0),
        axis= vector(
            2 * np.cos(np.deg2rad(angulo_inicial)), 
            2 * np.sin(np.deg2rad(angulo_inicial)),
            0
            )
    )


    #particula en movimiento.
    bola = sphere(pos = vector(0,0,0))
    bola.trail = curve(color=bola.color)

    #flecha del movimiento de la particula

    flecha = arrow(
        pos= vector(0,0,0),
        axis = vector(velocidad_X/1000000,velocidad_Y/1000000,0),
        color = color.yellow
    )

    #posicion en X
    text_Y = label(
        pos= bola.pos,
        text = "posicion y = 0 m",
        xoffset=1,
        yoffset = 80,
        space = bola.radius,
        font = "sans",
        box = False,
        height  = 10
    )

    #posicion en Y
    text_X = label(
        pos= bola.pos,
        text = "posicion x = 0 m",
        xoffset=1,
        yoffset = 40,
        space = bola.radius,
        font = "sans",
        box = False,
        height  = 10
    )

    #tiempo
    text_tiempo = label(
        pos = bola.pos,
        text = "tiempo = 0 s",
        xoffset = 1,
        yoffset = 60,
        space = bola.radius,
        font = "sans",
        box = False,
        height = 10
    )


    tiempo_inicial = 0


    while tiempo_inicial <= tiempo_total:

        if ((velocidad_X*tiempo_inicial*100)<= largo_suelo):
            #posicion de la pelota *100 para lograr ver el movimiento
            bola.pos = vector (
                (velocidad_X*tiempo_inicial)*100,
                (velocidad_Y*tiempo_inicial+0.5*aceleracion*tiempo_inicial**2)*100,
                0
            )

            #posicion de la flecha *100 para lograr seguir el movimiento de la pelota
            flecha.pos = vector(
                velocidad_X*tiempo_inicial*100,
                (velocidad_Y*tiempo_inicial+0.5*aceleracion*tiempo_inicial**2)*100,
                0
            )
            #movimientos de los objetos.
            #particula
            bola.trail.append(pos=bola.pos)
            #flecha
            flecha.axis = vector(velocidad_X/1000000, (velocidad_Y+aceleracion*tiempo_inicial)/1000000,0)
            #textos
            #posicion en x
            text_X.pos = bola.pos
            text_X.text = "posicion x = %s m" % str(velocidad_X * tiempo_inicial)
            #posicion en y
            text_Y.pos = bola.pos
            text_Y.text= "posicion y = %s m" % str(velocidad_Y * tiempo_inicial - 0.5 * aceleracion * tiempo_inicial**2)
            #tiempo recorrido
            text_tiempo.pos = bola.pos
            text_tiempo.text= "tiempo = %s s" % str(tiempo_inicial)
            #tiempo
            tiempo_inicial = tiempo_inicial + tiempo_total/100

            distancia_y_= (velocidad_Y*tiempo_inicial+0.5*aceleracion*tiempo_inicial**2)*100
            #frames por segundo o velocidad de la animacion
            rate(10)





