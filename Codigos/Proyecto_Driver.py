import location
from bs4 import BeautifulSoup
import requests
import lxml
import re
import pandas as pd
import numpy as np

from ETL_AenaToCSV import getDESTINOS
from WRAPPER_GetPrecio import getPRECIOS
from funciones_capitales import getCapitales, setCapitales 
from mejoresdestinos import MejoresDESTINOS
from funcionpablo import PablitoPlanes
import warnings
import ipywidgets as widgets
from IPython.display import display
warnings.filterwarnings('ignore')

def proyecto(sFlag = True):
    while sFlag == True:
    ##################################################################
    #
    # 1) Lo primero que hace esta función será llamar a la fución 
    # de la ubicación e imprimir por pantalla el output de esa función
    # sin mostrar la imagen aún
    #
    #################################################################

        mapa_Aeropuerto = location.driver()
        
    ##################################################################
    #
    # 2) A continuación se mostrarán por pantalla todos los destinos  
    #  Barajas.
    # 
    ##################################################################

        path_output="." 
        ReadCapitales=pd.read_csv(path_output+'/CAPITALES_CHINGONAS.csv')
        ReadCapitales = ReadCapitales.drop(columns='Unnamed: 0')

        print("A continuación se le mostrarán 20 de los destinos más destacables que hemos encontrado desde Barajas.")

        print(ReadCapitales.head(20))

    ##################################################################
    #
    # 3)  Por último se muestran los 5 destinos más baratos con los 
    #   planes de TripAdvisor 
    # 
    ##################################################################

        destinos_opt = input("¿Desea ver qué destinos son los más recomendables?")
        if destinos_opt.lower() == "si" or destinos_opt.lower() == "sí":
            Precios=getPRECIOS(ReadCapitales,"w",path_output)
            LISTA_5Destinos=MejoresDESTINOS(Precios)

            for ciudades in LISTA_5Destinos['Recomendaciones']:
                (a,b,c)=PablitoPlanes(ciudades.replace(' ',''),5)
                print("Ciudad: ",ciudades)
                print(b,"\n")
                print(c,"\n")
                print("Lista de planes: \n")
                print(a,"\n")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

            

        else:
            final_opt = input("¿Desea salir de la aplicación?")
            if  final_opt.lower() == "si" or final_opt.lower() == "sí":
                break

            else:
                continue


        while True:
            decision = input("¿Cuál es el destino que quiere ver más en detalle?")
            lista_planes,titulo,texto = PablitoPlanes(decision.upper(),5)

            location.dibujar_mapa(lista_planes, decision)

            close = input("¿Desea ver alguna ciudad más?")

            if  close.lower() == "si" or close.lower() == "sí":
                continue

            else:
                break

        print("La ruta hacia el aeropuerto es la siguiente:")
        mapa_Aeropuerto

        sFlag = False



def arbol_decision(opciones, texto: str):

    dropdown = widgets.Dropdown(
    options=opciones,
    value=opciones[0][0],
    description=texto,
    disabled=False,
    )

    return dropdown


def step_1():
    """
    1) Lo primero que hace esta función será llamar a la fución 
    de la ubicación e imprimir por pantalla el output de esa función
    sin mostrar la imagen aún
    """
    mapa_Aeropuerto = location.driver()

    return mapa_Aeropuerto

def step_2():
    """
    2) A continuación se mostrarán por pantalla todos los destinos
    Barajas.
    """
    path_output="." 
    ReadCapitales=pd.read_csv(path_output+'/CAPITALES_CHINGONAS.csv')
    ReadCapitales = ReadCapitales.drop(columns='Unnamed: 0')

    print("\nA continuación se le mostrarán 20 de los destinos más destacables que hemos encontrado desde Adolfo Suárez Madrid-Barajas (MAD).")

    print(ReadCapitales.head(20))

    """
    3)  Por último se muestran los 5 destinos más baratos con los 
    planes de TripAdvisor 
    """
    destinos_opt = input("¿Desea ver qué destinos son los más recomendables?")
    if destinos_opt.lower() == "si" or destinos_opt.lower() == "sí":
       
        Precios=getPRECIOS(ReadCapitales,"w",path_output)
        LISTA_5Destinos=MejoresDESTINOS(Precios)
        print(LISTA_5Destinos)

        # for ciudades in LISTA_5Destinos['Recomendaciones']:
        #     (a,b,c)=PablitoPlanes(ciudades.replace(' ',''),5)
        #     print("Ciudad: ",ciudades)
        #     print(b,"\n")
        #     print(c,"\n")
        #     print("Lista de planes: \n")
        #     print(*a, sep="\n")
        #     print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        # print("Esto termina")

    
    else:
        final_opt = input("¿Desea salir de la aplicación?")
        if  final_opt.lower() == "si" or final_opt.lower() == "sí":
            return

        else:
            pass

    cinco_destinos = LISTA_5Destinos['Recomendaciones'].str.split("/")
    lista_dropdown = [(cinco_destinos[i][0], i) for i in range(len(cinco_destinos))]
    # lista_dropdown = [cinco_destinos[i][0] for i in range(len(cinco_destinos))]
    return lista_dropdown, LISTA_5Destinos['Recomendaciones'].str.replace(" ", "");


def step_3(ciudad, destinos):
    """
    el input es lo que introducimos con el desplegable
    destinos es el data frame de antes
    """

    lista_planes, b, c = PablitoPlanes(destinos[ciudad],5)
    print("Ciudad: ", destinos[ciudad])
    print(b,"\n")
    print(c,"\n")
    print("Lista de planes: \n")
    print(*lista_planes, sep="\n")

    mapa_sitios = location.dibujar_mapa(lista_planes, destinos.str.split("/")[ciudad][0])
    display(mapa_sitios)


    return

def step_4(mapa):
    print("La ruta hacia el aeropuerto es la siguiente:")
    display(mapa)
    return
