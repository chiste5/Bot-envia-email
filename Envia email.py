#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pyautogui
import pyperclip
import time


pyautogui.hotkey("ctrl","t")
pyperclip.copy(r'https://mail.google.com/mail/u/0/#inbox')
texto = pyperclip.paste()
pyautogui.typewrite(texto)
pyautogui.hotkey("Enter")
time.sleep(4)
pyautogui.click(x = 121,y = 221)
time.sleep(6)
pyautogui.write('guichiste@gmail.com')
pyautogui.hotkey("Enter")
time.sleep(3)
pyautogui.hotkey("Enter")
time.sleep(3)
pyautogui.hotkey("tab")
pyautogui.write('Noticias Diarias')
pyautogui.hotkey("tab")
texto = """Bom dia/tarde,
            A Somando Conhecimento traz notícias fresquinhas 📰 pra você ficar por dentro de tudo o que está acontecendo no mundo do empreendedorismo e tecnologia💰📈📱. 
            Além disso, temos também indicações de filmes e um cursinho para dar aquele upgrade no conhecimento."""
pyautogui.write(texto)
time.sleep(5)
pyautogui.hotkey("ctrl","Enter")


# In[7]:


import pyautogui
import time
x, y = pyautogui.position()
print ("Posicao atual do mouse:")
time.sleep(6)
print ("x = "+str(x)+" y = "+str(y))


# In[ ]:




