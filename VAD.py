#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Proabilidad y Estadística

José Miguel González Arias
Jose Andrés Sandoval Díaz
Alonso Azofeifa Jiménez
"""
#Librerías necesarias para debugging y manejo de excepciones
import sys
import os
import traceback
import time
import signal
import fcntl
import string
import re


#Utilizada para crear las diferentes gráficas
from matplotlib import pyplot as plt

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nbinom.html
from scipy.stats import nbinom
from scipy.stats import geom

import numpy as np

if __name__ == "__main__":
    
    #cant_intentos es la cantidad máxima de intentos disponibles
    cant_intentos = 20
    #X es un array desde 1 hasta (cant_intentos+1) con intervalos equidistantes.
    X = np.arange(1,cant_intentos+1)
    #P_c1 probabilidad de obtener un éxito para el caso 1 que es de 50%
    P_c1 = 0.5
    #P_c1 probabilidad de obtener un éxito para el caso 2 que es solo de un 30%
    P_c2 = 0.3

    #Función para obtener la función de masa de probabilidad para el caso 1 donde la probabilidad de obtener un éxito es de 50% y en el caso 2 un 30%
    #Teniendo como meta conocer probabilidad de la cantidad de lanzamiento antes de obtener un escudo
    x_c1 = geom.pmf(cant_intentos, P_c1)
    x_c2 = geom.pmf(cant_intentos, P_c2)
    #Imprime en pantalla el resultado obtenido 
    print("########################################")
    print("############### Parte #1 ###############")
    print("######## Distribución Geométrica #######\n")

    print("Probabilidad de encontrar 1 escudo dentro de {} lanzamientos con una probabilidad de {} de obtener un escudo es: {}".format(cant_intentos,P_c1,x_c1*100))

    print("Probabilidad de encontrar 1 escudo dentro de {} lanzamientos con una probabilidad de {} de obtener un escudo es: {}".format(cant_intentos,P_c2,x_c2*100))
    

    #Para el caso #1
    #Obtener la funcion de masa de probabilidad utilizando los rangos de intentos desde 1 hasta 20 intentos como máximo.
    prom_geom = geom.pmf(X, P_c1,1)
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    #Plotea la cantidad de lanzamientos que se dan vs la probabilidad de obtener un fallo en cumplir la meta
    ax.plot(X, prom_geom, 'go', ms=8, label='FMP Binomial Neg')
    plt.ylabel("Probabilidad de tener que repetir \nel lanzamiento una vez más", fontsize="12")
    plt.xlabel("X número de lanzamientos al aire", fontsize="12")
    plt.title("Distribución Geométrica para el Caso #1", fontsize="18")
    ax.vlines(X, 0, prom_geom, colors='g', lw=5, alpha=0.5)
    plt.show()

    #Para el caso #2
    #Obtener la funcion de masa de probabilidad utilizando los rangos de intentos desde 1 hasta 20 intentos como máximo.
    prom_geom = geom.pmf(X, P_c2,1)
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    #Plotea la cantidad de lanzamientos que se dan vs la probabilidad de obtener un fallo en cumplir la meta
    ax.plot(X, prom_geom, 'go', ms=8, label='FMP Binomial Neg')
    plt.ylabel("Probabilidad de tener que repetir \nel lanzamiento una vez más", fontsize="12")
    plt.xlabel("X número de lanzamientos al aire", fontsize="12")
    plt.title("Distribución Geométrica para el Caso #2", fontsize="18")
    ax.vlines(X, 0, prom_geom, colors='g', lw=5, alpha=0.5)
    plt.show()


    print("\n\n########################################")
    print("############### Parte #2 ###############")
    print("#### Distribución Binomial Negativa ####\n")
    #r cantidad de éxitos a obtener
    r = 3
    #Función para obtener la función de masa de probabilidad para el caso 1 donde la probabilidad de obtener un éxito es de 50%
    #Teniendo como meta conocer probabilidad de la cantidad de lanzamiento antes de obtener tres escudos
    x = nbinom.pmf(k=r, n=cant_intentos, p=P_c1)
    #Imprime en pantalla el resultado obtenido 
    print("Probabilidad de encontrar {} escudos dentro de {} lanzamientos con una probabilidad de {} de obtener un escudo es: {}".format(r,cant_intentos,P_c1,x*100))
    #Función para obtener la función de masa de probabilidad para el caso 2 donde la probabilidad de obtener un éxito es de 30%
    x = nbinom.pmf(k=r, n=cant_intentos, p=P_c2)
    #Imprime en pantalla el resultado obtenido
    print("Probabilidad de encontrar {} escudos dentro de {} lanzamientos con una probabilidad de {} de obtener un escudo es: {}".format(r,cant_intentos,P_c2,x*100))

    #Obtener la funcion de masa de probabilidad utilizando los rangos de intentos desde 1 hasta 20 intentos como máximo.
    prom_nbinom = nbinom.pmf(X, r, P_c1,1)
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    #Plotea la cantidad de lanzamientos que se dan vs la probabilidad de obtener un fallo en cumplir la meta
    ax.plot(X, prom_nbinom, 'bo', ms=8, label='FMP Binomial Neg')
    plt.ylabel("Porcentaje de fallos al conseguir la meta", fontsize="12")
    plt.xlabel("X número de lanzamientos al aire", fontsize="12")
    plt.title("Distribución Binomial Negativa para el Caso #1", fontsize="18")
    ax.vlines(X, 0, prom_nbinom, colors='b', lw=5, alpha=0.5)
    plt.show()

    prom_nbinom = nbinom.pmf(X, r, P_c2,1)
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))    
    #Plotea la cantidad de lanzamientos que se dan vs la probabilidad de obtener un fallo en cumplir la meta
    ax.plot(X, prom_nbinom, 'bo', ms=8, label='FMP Binomial Neg')
    plt.ylabel("Porcentaje de fallos al conseguir la meta", fontsize="12")
    plt.xlabel("X número de lanzamientos al aire", fontsize="12")
    plt.title("Distribución Binomial Negativa para el Caso #2", fontsize="18")
    ax.vlines(X, 0, prom_nbinom, colors='b', lw=5, alpha=0.5)
    plt.show()





