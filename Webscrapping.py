# Practica 5 Webscrapping.py
# Yahir Alejandro Navarro Amador    1874451

import requests
from bs4 import *
import os
from PIL import TAGS, GPSTAGS
from PIL import Image

# Este scrip nos permite descargar imagenes de algun sitio web
# Es nesesario ejecutarlo en la consola de la siguiente forma
# >python Webscrapping -link 'Link de la pagina'

def Images(url):
    r = requests.get('http://www.'+url)
    soup = BeautifulSoup(r.text, 'html.parser')
    urls = list()
    images = soup.select(img['src'])
    for img in images:
        urls.append(img['src'])
    global ruta
    ruta = input('Introduce la ruta y seleccionada el nombre del directorio a crear: ')
    os.mkdir(ruta)
    i = 1
    for index, img_link in enumerate(urls):
        if i <= len(urls):
            img_data = request.get(img_link).content
            with open(ruta+'\\'+str(index+1)+'.jpg','wb+') as f:
                f.write(img_data)
            i += 1
        else:
            f.close()
            break
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArguentParser(description = 'Este script descarga las imagenes del sitio que indiques e imprime la metada de cada una')
    parser.add_argument('-link', '-url', help='El url de donde quieras descargar las iimagenes')
    args = parser.parse_args()
    url = args.url
    get_images(url)
    
