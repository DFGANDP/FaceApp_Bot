# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:55:38 2021


▒█▀▀▀ █▀▀█ █▀▀ █▀▀ ░█▀▀█ █▀▀█ █▀▀█ ▒█▀▀█ █▀▀█ ▀▀█▀▀ █▀█ ░ █▀▀█ 
▒█▀▀▀ █▄▄█ █░░ █▀▀ ▒█▄▄█ █░░█ █░░█ ▒█▀▀▄ █░░█ ░░█░░ ░▄▀ ▄ █▄▀█ 
▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ▒█░▒█ █▀▀▀ █▀▀▀ ▒█▄▄█ ▀▀▀▀ ░░▀░░ █▄▄ █ █▄▄█

@author: Wojtek

Akcje





SORTOWANIE SIE ZMIENILO TRZEBA PRZEROBIC BOTA

"""

# przycisk scroll to cofnij
# ustawic twoj telefon galaxys10 w gornym lewym roku i powiekszyc na maksa
# w telefonie w galerii sortowac po nazwie rosnaco

# zmieniac nazwe po kazdym wykonaniu zeby wiadomo bylo
# ktore zdjecie jest ktore a potem usuwac
# na wypadek zablokowania i niewiadomych system STOP


from python_imagesearch.imagesearch import imagesearch_loop
from python_imagesearch.imagesearch import imagesearch_region_loop, region_grabber, imagesearch_numLoop
import pyautogui
import time
import cv2
import numpy as np

### PHONE REGION
x1 =  0
y1 = 0
x2 = 470
y2 = 1040
is_retina = False


def move(ikona):
    '''
    Move mouse on given icon
    '''

    pos = imagesearch_region_loop(ikona, 1, x1,y1,x2,y2)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])


def action(ikona,click=True):
    '''
    wymyslic cos lepszego do czekania jak mi wkurw zejdzie
    '''
    
    move(ikona)
    if click ==True:
        pyautogui.click()

def action_hundred(ikona,click=True):
    '''
    wymyslic cos lepszego do czekania jak mi wkurw zejdzie
    '''
    pos = imagesearch_region_loop_colour(ikona, 1, x1,y1,x2,y2,0.91)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    if click ==True:
        pyautogui.click()

def niewykryto():
    '''
    jesli niewykryto twarzy to:
    cofnij do menu
    usun zdjecie
    
    '''
    for i in range(3):
        cofnij()
    algorytm_galeria()
    
def algorytm_faceswap():
    action("Thumbnail_FaceApp.jpg")
    action("FaceApp_galeria.jpg")
    action("All_media.jpg")
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    time.sleep(0.15)
    action('Azdjecia.jpg')
    move("X.jpg")
    pyautogui.move(0, 50)
    pyautogui.click()
    # !!!!!!!!!!!!!!!tutaj dodac jesli nie wykryto to pomin i usuwaj odrazu
    # IF niewyktyrto cofnij do galerii i usun
    time.sleep(2.5)
    pos = imagesearch_numLoop("niewykryto.jpg", 1, 2)
    if pos[0] != -1:
        niewykryto()
    else:
        print("Zdjecie działa")
        pyautogui.click(x=1155, y=167) # w tym miejscu musi byc play z macro recordera
        pyautogui.click()
        time.sleep(4)
        action("Zamiana_twarzy.jpg")
        action("Zamiana_twarzy_wew.jpg")
        action("Wybierz_z_galerii.jpg")
        action("FaceApp_galeria.jpg")
        action("All_media.jpg")
        pyautogui.scroll(-2500)
        pyautogui.scroll(-2500)
        pyautogui.scroll(-2500)
        pyautogui.scroll(-2500)
        pyautogui.scroll(-2500)
        time.sleep(0.2)
        action("Aemixxly.jpg")
        move("X.jpg")
        pyautogui.move(0, 50)
        pyautogui.click()
        ##### TUTAJ DAC ZEBY CZEKALO AZ SIE ZALADUJE ALBO KOLOROWE ZAPISZ ALBO INNY SPOSOB 
        #action("pasek.jpg")
        time.sleep(10)
        action("zapisz(ready).jpg")
        time.sleep(1)
        for i in range (4):
            cofnij()

    
def cofnij():
    pyautogui.moveTo(412, 1005)
    pyautogui.dragTo(412, 900, button='left')
    time.sleep(0.2)

def imagesearcharea_colour(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        # im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    template = cv2.imread(image)
    
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

def imagesearch_region_loop_colour(image, timesample, x1, y1, x2, y2, precision=0.8):
    pos = imagesearcharea_colour(image, x1, y1, x2, y2, precision)

    while pos[0] == -1:
        time.sleep(timesample)
        pos = imagesearcharea_colour(image, x1, y1, x2, y2, precision)
    return pos

def algorytm_galeria():
    action("Thumbnail_Galeria.jpg")
    move("aparat.jpg")
    pyautogui.move(0, 100)
    pyautogui.click()
    move("Azdjecia_galeria.jpg")
    pyautogui.move(0, 100)
    pyautogui.click(clicks=1)
    time.sleep(1)
    action("kosz_g_bez_drag.jpg")
    action("kosz_galeria.jpg")
    time.sleep(0.5)
    for i in range (4):
        cofnij()

def main():
    for i in range(100):
        algorytm_faceswap()
        algorytm_galeria()
     

    

main()
