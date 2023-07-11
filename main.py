import pyautogui
import time
import cv2
import subprocess 

def focus_window(window_title):
    try:
        # wmctrl-Befehl, um Fenster mit dem angegebenen Titel zu fokussieren
        subprocess.run(["wmctrl", "-a", window_title])
        return True
    except Exception as e:
        print(f"Fehler beim Fokussieren des Fensters: {e}")
        return False

# Den Titel des Fensters, das den Fokus erhalten soll
window_title = "NoMachine - HPLC_BlackLady" 

# Fenster fokussieren
if focus_window(window_title):
    # Warten, damit das Fenster fokussiert wird
    time.sleep(1)
    def locate_on_screen(image_path, confidence=0.9):
        return pyautogui.locateOnScreen(image_path, confidence=confidence)
    
    def click_image(image_path):
        location = locate_on_screen(image_path)
        if location:
            x, y = pyautogui.center(location)
            pyautogui.click(x, y)
            return True
        return False

    # Stellen Sie sicher, dass die Anwendung geöffnet ist und warten Sie kurz
    time.sleep(10)
    
    # Navigiere zum "File" Dropdown-Menü (Screenshot des "File" Textes)
    click_image("File_Dropdown.png")
    
    # Wartezeit, damit das Menü aufklappt
    time.sleep(10)
    
    # Klicke auf den "Load Method Parameter" Button (Screenshot des Buttons)
    click_image("Load_Parameter.png")
    
    # Wartezeit, damit das Eingabefenster erscheint
    time.sleep(10)
    
    # Eingabe des Pfades im "File name" Inputfeld
    pyautogui.write("C:\\LabSolutions\\Data\\Shimadzu\\Labor MBT\\Messdaten\\Aminosäuren\\T1D_GABA\\Auswertung\\220810_GABA_OPA_Auswertung_Großversuch")

    # Klicke auf den "Open" Button (Screenshot des Buttons)
    click_image("Open_Button.png")
else:
    print(f'Fenster mit dem Titel "{window_title}" nicht gefunden.')
