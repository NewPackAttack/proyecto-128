from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas

START_URL="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
USE_URL=webdriver.Chrome("C:/Users/paczi/Downloads/clase 127/chromedriver.exe")
USE_URL.get(START_URL)
time.sleep(10)
planetario=[]

def espacio():
    for e in range(0,10):
        print(f'extraendo pagina {e+1} ...')
        soup=BeautifulSoup(USE_URL.page_source, "html.parser") 

        for ultag in soup.find_all("ul", attrs={"class","exoplanet"}):
            etiquetali=ultag.find_all("li")
            tetris=[]
            
            for index,litag in enumerate(etiquetali):
                if index==0:
                    tetris.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        tetris.append(litag.contents[0])
                    except:
                        tetris.append("")

            planetario.append(tetris)

    print(planetario[1])

espacio()
encabezado=["nombre","año luz", "masa planeta", "magnitud","fecha de descubrimiento"]
planetadataframe=pandas.DataFrame(planetario,columns=encabezado)

planetadataframe.to_csv('datosplaneta.csv',index=True,index_label="id")