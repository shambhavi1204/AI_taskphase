import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    
def isCollide(data):
    for i in range(200,230):
       for j in range(480,570):
           if data[i, j] < 100:
               hit("down")
               return True 
           
    for i in range(200, 230):
        for j in range(570, 665):
            if data[i, j] < 100:
                hit("up")
                return True 
    return False 



print("Dino game about to start!")
time.sleep(2)
#hit('up')

while True:
#image = takeScreenshot()
   image = ImageGrab.grab().convert('L')
   data = image.load()
   isCollide(data)
   '''    
   for i in range(200,230):
       for j in range(570,665):
           data[i, j] = 0

   
   for i in range(200,230):
       for j in range(480,570):
           data[i, j] = 171

           
   image.show()
   break
   '''
