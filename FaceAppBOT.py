from python_imagesearch.imagesearch import imagesearcharea
import pyautogui
import time

#prawy przycisk myszy to cofnij
#ustawic twoj telefon galaxys10 w gornym lewym roku i powiekszyc na maksa
# w telefonie w galerii sortowac po nazwie rosnaco

#!!!!!!!!!!!!!!!!!!! zmieniac nazwe po kazdym wykonaniu zeby wiadomo bylo
#!!!!!!!!!!!! ktore zdjecie jest ktore a potem usuwac


ikona = {"gal" : "Galeria.jpg",
         "apka" : "FaceApp.jpg",
         "galfa" : "Galeria_faceapp.jpg",
         "fs": "Faceswap234.jpg",
         "am" : "allmedia.jpg",
         "az" : "azdjecia_faceswap.jpg",
         "bc" : "back.jpg", #  if nie wykryje: dac pare pixeli nizej niz to !
         "Ae" : "Aemixxly.jpg",
         "apar" : "aparat.jpg",
         "azg" : "Azdjecia_galeria.jpg",
         "kg" : "kosz_galeria.jpg",
         "rg" : "rozwin_galeria.jpg",
         "ug" : "kosz_g_bez_drag.jpg",
         "wg" : "Wybierz_z_galerii.jpg",
         "fs2" : "Zamiana_twarzy.jpg",
         "sav" : "Zapisz.jpg",
         "udd" : "niewykryto.jpg"
         }

def move(ikona):
    '''
    Move mouse on given icon
    '''
    pos = imagesearcharea(ikona,0,0,500,1050)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("image not found")


def action(ikonas,click=True,timer=2):
    '''
    wymyslic cos lepszego do czekania jak mi wkurw zejdzie
    '''
    print(ikonas)
    move(ikona[ikonas])
    if click ==True:
        pyautogui.click()
    time.sleep(timer)


### ZAMIAST ROBIC CZEKANIE NA SEKUNDY ZROBIC CZEKANIE AZ SIE NIE STANIE


def algorytm_faceswap():
    action("apka")
    action("galfa")
    action("am")
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    time.sleep(0.2)
    action('az')
    move(ikona["bc"])
    pyautogui.move(0, 50)
    pyautogui.click()
    time.sleep(10)
    # !!!!!!!!!!!!!!!tutaj dodac jesli nie wykryto to pomin i usuwaj odrazu
    action("fs")
    action("fs2")
    action("wg")
    action("galfa")
    action("am")
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    pyautogui.scroll(-2500)
    time.sleep(0.2)
    action("Ae")
    move(ikona["bc"])
    pyautogui.move(0, 50)
    pyautogui.click()
    time.sleep(10) # zamiast tego dac czekanie wbudowane
    # !!!!!!!!!! tutaj dodac dluzej czeka niz 10sek  to do menu glownego i usunac
    action("sav")
    for i in range (4):
        pyautogui.click(button="right")
        time.sleep(0.5)

def algorytm_galeria():
    action("gal")
    move(ikona["apar"])
    pyautogui.move(0, 100)
    pyautogui.click()
    move(ikona["azg"])
    pyautogui.move(0, 100)
    pyautogui.click(clicks=1)
    time.sleep(1)
    action("ug")
    action("kg")
    time.sleep(0.5)
    for i in range (3):
        pyautogui.click(button="right")
        time.sleep(0.5)

        
def zmien_nazwe():
    '''
    zmienia nazwe pliku na taka jaka mial wczesniej dodaje FA na koniec
    '''
    return

def wykonaj(ile_razy=0):
    for i in range(ile_razy):
        algorytm_faceswap()
        algorytm_galeria()
        
def main():
    wykonaj(6)

main()
