import pyautogui as ac
import time
import keyboard


def upar():
    count = 0
    print("Clicke no jogo em até 2 segundos.")
    time.sleep(2)
    while (count < 49):
        ac.press('t')
        time.sleep(0.6)
        ac.write('/rankup')
        ac.press('enter')
        time.sleep(0.6)
        ac.moveTo(892,428)
        ac.click()
        time.sleep(1)
        count += 1

def sair():
    exit()

print("Pressione R para upar ou S para sair.")

while True:
    try:
        if keyboard.is_pressed('r'):
            upar()
        if keyboard.is_pressed('s'):
            sair()
    except:
        break
