from bs4 import BeautifulSoup
import requests
import lxml
import re
import pandas as pd
import numpy as np
from funciones_capitales import getCapitales, setCapitales 

Aena='/FinalDataFrame.csv'
Capitales='/Capitales.csv'
path_output="/home/vant/Documentos/Master/DatosMasivos/Scripts/Final/SubirDrive/"

getCapitales(path_output)
setCapitales(Aena,Capitales,path_output) 