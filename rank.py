import pyautogui as ac
import time
import keyboard


def upar():
    count = 0
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
keyboard.add_hotkey('r', upar)
keyboard.add_hotkey('s', sair)
keyboard.wait()
