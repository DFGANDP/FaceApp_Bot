# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:55:38 2021


▒█▀▀▀ █▀▀█ █▀▀ █▀▀ ░█▀▀█ █▀▀█ █▀▀█ ▒█▀▀█ █▀▀█ ▀▀█▀▀ █▀█ ░ █▀▀█
▒█▀▀▀ █▄▄█ █░░ █▀▀ ▒█▄▄█ █░░█ █░░█ ▒█▀▀▄ █░░█ ░░█░░ ░▄▀ ▄ █▄▀█
▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ▒█░▒█ █▀▀▀ █▀▀▀ ▒█▄▄█ ▀▀▀▀ ░░▀░░ █▄▄ █ █▄▄█

@author: Wojtek

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

    move(ikona)
    if click ==True:
        pyautogui.click()

def action_hundred(ikona,click=True):
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
    for i in range(2):
        cofnij()
    algorytm_galeria()

def algorytm_faceswap():


    move("jpegs/cofacz.jpg")
    pyautogui.move(0, 80)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(0.4)
    action("jpegs/Udostepnij.jpg")
    time.sleep(2.3)
    #pyautogui.dragRel(0, -670, button='left')
    #time.sleep(1)
    #pyautogui.dragRel(0, -670,2, button='left')
    #move("WszystkieAplikacje.jpg")
    #time.sleep(1)
    #pyautogui.dragRel(0, -250,2, button='left')
    action("jpegs/FaceApp_thumbnail_galeria.jpg")
    time.sleep(2.5) # czas na wczytanie
    pos = imagesearch_numLoop("niewykryto.jpg", 1, 2)
    if pos[0] != -1:
        niewykryto()
        return True
    else:
        print("Zdjecie działa")
        pyautogui.click(x=1155, y=167) # w tym miejscu musi byc play z macro recordera
        pyautogui.click()
        time.sleep(4.5)
        action("jpegs/Zamiana_twarzy.jpg")
        time.sleep(0.2)
        action("jpegs/Zamiana_twarzy_wew.jpg")
        action("jpegs/Wybierz_z_galerii.jpg")
        action("jpegs/FaceApp_galeria.jpg")
        action("jpegs/All_media.jpg")
        pyautogui.scroll(-2500)
        pyautogui.scroll(-2500)
        pyautogui.scroll(-2500)
        pyautogui.scroll(-2500)
        pyautogui.scroll(-2500)
        time.sleep(0.2)
        action("jpegs/Aemixxly.jpg")
        move("X.jpg")
        pyautogui.move(0, 50)
        pyautogui.click()
        ##### TUTAJ DAC ZEBY CZEKALO AZ SIE ZALADUJE ALBO KOLOROWE ZAPISZ ALBO INNY SPOSOB
        #action("jpegs/pasek.jpg")
        time.sleep(10)
        action("jpegs/zapisz(ready).jpg")
        time.sleep(1)
        for i in range (4):
            cofnij()
        return False

def cofnij():
    pyautogui.moveTo(412, 1005)
    pyautogui.dragTo(412, 880, button='left')
    time.sleep(0.4)

def algorytm_galeria():

    move("cofacz.jpg")
    pyautogui.move(0, 130)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(0.2)
    action("jpegs/kosz_g_bez_drag.jpg")
    pyautogui.moveRel(0, -80)
    time.sleep(0.5)
    action("jpegs/kosz_galeria.jpg")
    time.sleep(3.5)


def main():
    for i in range(500):
        boolean = algorytm_faceswap()
        if boolean == False:
            algorytm_galeria()
            time.sleep(2)
        else:
            pass



main()
