import pyautogui
import time

time.sleep(2)

def locate_on_screen(image_path, confidence=0.8):
    return pyautogui.locateOnScreen(image_path, confidence=confidence)
    
def click_image(image_path):
    location = locate_on_screen(image_path)
    if location:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        return True
    return False

# Stellen Sie sicher, dass die Anwendung geöffnet ist und warten Sie kurz
time.sleep(2)
    
# Navigiere zum "File" Dropdown-Menü (Screenshot des "File" Textes)
click_image("File_Dropdown.png")
    
# Wartezeit, damit das Menü aufklappt
time.sleep(2)
    
# Klicke auf den "Load Method Parameter" Button (Screenshot des Buttons)
click_image("Load_Parameter.png")
    
# Wartezeit, damit das Eingabefenster erscheint
time.sleep(2)
    
# Eingabe des Pfades im "File name" Inputfeld
pyautogui.write("C:\\LabSolutions\\Data\\Shimadzu\\Labor MBT\\Messdaten\\Aminosäuren\\T1D_GABA\\Auswertung\\220810_GABA_OPA_Auswertung_Großversuch")

# Klicke auf den "Open" Button (Screenshot des Buttons)
click_image("Open_Button.png")
