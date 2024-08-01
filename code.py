import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time
import sys
import requests 
import os
import pyperclip
import re
def get_direct_download_link(shareable_link):
    file_id = shareable_link.split('/')[-2]
    return f"https://drive.google.com/uc?export=download&id={file_id}"
def download_image_from_drive(shareable_link, save_location, save_name):
    direct_download_link = get_direct_download_link(shareable_link)
    response = requests.get(direct_download_link)
    if response.status_code == 200:
        with open(os.path.join(save_location, save_name), 'wb') as file:
            file.write(response.content)
        print(f"Image saved as {os.path.join(save_location, save_name)}")
    else:
        print("Failed to download the image")
def save_image():
    shareable_link = pyperclip.paste()
    save_location = "C:\\images"
    save_name = "picture.jpg"
    if not os.path.exists(save_location):
        os.makedirs(save_location)
    download_image_from_drive(shareable_link, save_location, save_name)
    print("Success", "Image saved successfully!")
run = False
def bot_function():
    global running
    try:
        indicator_label.config(text="Bot is running...", fg="green")
        def sleep_check(interval):
            for _ in range(interval):
                if not running:
                    return False
                time.sleep(2)
            return True
        def check_running():
            if not running:
                indicator_label.config(text="Bot has stopped.", fg="red")
                return False
            return True
        # Bot actions
        
        pyautogui.hotkey('win', '1')
        if not check_running(): return
        indicator_label.config(text="Opening Chrome.", fg="blue")
        pyautogui.hotkey('winleft', 'r')
        if not check_running(): return
        time.sleep(1)   
        pyautogui.write('chrome.exe')
        pyautogui.press('enter')  # Open Chrome
        indicator_label.config(text="Adding Chrome Profile.", fg="blue")
        if not sleep_check(1): return
        if not check_running(): return
        pyautogui.hotkey('winleft', 'up')
        time.sleep(1)   
        pyautogui.hotkey('shift', 'tab')
        time.sleep(1)   
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        indicator_label.config(text="Renaming Profile.", fg="blue")
        time.sleep(1)  # Replaced sleep_check(2) with time.sleep
        if not check_running(): return
        pyautogui.hotkey('win', '1')                        
        time.sleep(1)   
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)   
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)   
        indicator_label.config(text="Opening Facebook.", fg="blue")
        
        time.sleep(1)   
        if not check_running(): return
        pyautogui.write('facebook.com')
        pyautogui.press('enter')  
###########################################################################             Facebook page Loading Check start
        if not check_running(): return
        search_image = 'C:\\facebookBot\\clickImages\\login_page_image.png'
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        if not check_running(): return
        i = 0
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i), fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        if not check_running(): return
        time.sleep(1)  
###########################################################################             Loading Check end
###########################################################################             Copying user name and passsword
        indicator_label.config(text="Opening Account list.", fg="blue")
        if not check_running(): return
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.hotkey('ctrl', 'c')
        indicator_label.config(text="Username Copied.", fg="blue")
        time.sleep(1)   
        if not check_running(): return
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)   
        indicator_label.config(text="Pasting Username.", fg="blue")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')
        time.sleep(1)   
        if not check_running(): return
        indicator_label.config(text="Opeing Account list.", fg="blue")
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)   
        indicator_label.config(text="Password Copied.", fg="blue")
        pyautogui.press('right')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)   
        indicator_label.config(text="Pasting Password.", fg="blue")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')  # login
        indicator_label.config(text="Login.... Please Wait", fg="blue")
###########################################################################             Copying user name and passsword
###########################################################################             dashboard Loading Check start
        search_image = 'C:\\facebookBot\\clickImages\\dashboard_fb_logo.png'
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i), fg="blue")
            time.sleep(1)  
        
        time.sleep(1)  
        indicator_label.config(text="Login Successful in "+ str(i)+"s", fg="blue")
        time.sleep(3)  
###########################################################################             Loading Check end
        def find_and_click_image(image_path):
            try:
                # Locate the image on the screen
                location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
                if location is not None:
                    # Click on the image
                    pyautogui.click(location)
                    print(f"Clicked on {image_path}")
                    return True
                else:
                    print(f"{image_path} not found on the screen.")
                    return False
            except Exception as e:
                print(f"An error occurred: {e}")
                return False

        # Paths to the images you want to search for
        image1_path = 'C:\\facebookBot\\clickImages\\never_save_image.png'
        image2_path = 'C:\\facebookBot\\clickImages\\never_save_image_light.png'

        # Check for the images and click if found
        image_found = False
        while not image_found:
            if find_and_click_image(image1_path) or find_and_click_image(image2_path):
                image_found = True
            else:
                # Wait for a short period before checking again
                time.sleep(2)

###########################################################################             check if suspended
        try:
            indicator_label.config(text="check account ", fg="blue")
            # Locate the textbox on the screen using an image
            textbox_location = pyautogui.locateOnScreen('C:\\facebookBot\\clickImages\\suspended_account.png')
            if textbox_location is not None:
                indicator_label.config(text="This Account is Suspended.... Closing", fg="red")
                time.sleep(2)   
                indicator_label.config(text="Closing This Profile", fg="red")
                time.sleep(2)   
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)   
                pyautogui.press('right')
                pyautogui.press('right')
                pyautogui.press('right')
                time.sleep(2)   
                pyautogui.write('This Account is Suspended !!!')
                indicator_label.config(text="Tyring Another Account.", fg="blue")
                time.sleep(2)   
                pyautogui.press('enter')
                pyautogui.press('home')
                bot_function()
                sys.exit()
            time.sleep(3)  
        except Exception as e:
            print('Suspended Account not found!!!')
        if not check_running(): return
###########################################################################             check if suspended end
###########################################################################             check if asking mobile number
        try:
            indicator_label.config(text="check account ", fg="blue")
            # Locate the textbox on the screen using an image
            textbox_location = pyautogui.locateOnScreen('C:\\facebookBot\\clickImages\\enter_mobile_number.png')
            if textbox_location is not None:
                indicator_label.config(text="Mobile Number Requierd.... Closing", fg="red")
                time.sleep(2)   
                indicator_label.config(text="Closing This Profile", fg="red")
                time.sleep(2)   
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)   
                pyautogui.press('right')
                pyautogui.press('right')
                pyautogui.press('right')
                time.sleep(2)   
                pyautogui.write('Asking Mobile Number !!!')
                indicator_label.config(text="Tyring Another Account.", fg="blue")
                time.sleep(2)   
                pyautogui.press('enter')
                pyautogui.press('home')
                bot_function()
                sys.exit()
            time.sleep(3)  
        except Exception as e:
            print('Suspended Account not found!!!')
        if not check_running(): return
###########################################################################             check if asking mobile number end


###########################################################################             check if ACCOUNT LOCKED
        try:
            indicator_label.config(text="check account ", fg="blue")
            # Locate the textbox on the screen using an image
            textbox_location = pyautogui.locateOnScreen('C:\\facebookBot\\clickImages\\account_locked.png')
            if textbox_location is not None:
                indicator_label.config(text="Account Locked.... Closing", fg="red")
                time.sleep(2)   
                indicator_label.config(text="Closing This Profile", fg="red")
                time.sleep(2)   
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)   
                pyautogui.press('right')
                pyautogui.press('right')
                pyautogui.press('right')
                time.sleep(2)   
                pyautogui.write('Account Locked !!!')
                indicator_label.config(text="Tyring Another Account.", fg="blue")
                time.sleep(2)   
                pyautogui.press('enter')
                pyautogui.press('home')
                bot_function()
                sys.exit()
            time.sleep(3)  
        except Exception as e:
            print('Suspended Account not found!!!')
        if not check_running(): return
###########################################################################             check if ACCOUNT LOCKED end

        indicator_label.config(text="Warming Up Account", fg="blue")
        pyautogui.hotkey('win', '1')
        ##############################################top search
        if not check_running(): return
        time.sleep(2)   
        pyautogui.press('right')
        pyautogui.press('right')
        if not check_running(): return
        time.sleep(2)   
        pyautogui.hotkey('ctrl', 'c')
        if not check_running(): return
        time.sleep(2)   
        pyautogui.hotkey('alt', 'tab')
        search_text = pyperclip.paste();
        pyautogui.write('https://web.facebook.com/search/people/?q=' + search_text)  
        if not check_running(): return
        time.sleep(2)  
        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.write('https://web.facebook.com/search/top?q=' + search_text)  
        if not check_running(): return
        pyautogui.press('enter')
        for _ in range(100):
            pyautogui.press('down')
        ##############################################People
        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.press('enter')
        for _ in range(100):
            pyautogui.press('down')
        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.write('https://web.facebook.com/reel/')  
        pyautogui.press('enter')
        if not check_running(): return
###########################################################################             reel page Loading Check start
        search_image = 'C:\\facebookBot\\clickImages\\reel.png'
        if not check_running(): return
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i),  fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        time.sleep(5)  
        search_image = 'C:\\facebookBot\\clickImages\\reel_like.png'
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                time.sleep(3)  
                neverrrtextbox_center = pyautogui.center(location)
                pyautogui.click(neverrrtextbox_center)
                time.sleep(3)  
                pyautogui.press('right')
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i),  fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        time.sleep(5)  
        search_image = 'C:\\facebookBot\\clickImages\\reel_like.png'
        if not check_running(): return
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                time.sleep(3)  
                neverrrtextbox_center = pyautogui.center(location)
                pyautogui.click(neverrrtextbox_center)
                time.sleep(3)  
                pyautogui.press('right')
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i),  fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        time.sleep(5)  
        if not check_running(): return
        search_image = 'C:\\facebookBot\\clickImages\\reel_like.png'
        if not check_running(): return
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                time.sleep(3)  
                neverrrtextbox_center = pyautogui.center(location)
                pyautogui.click(neverrrtextbox_center)
                time.sleep(3)  
                pyautogui.press('right')
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i),  fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        time.sleep(5)  
###########################################################################              reel page Loading Check end
        if not check_running(): return
#################################################################################################################
        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.write('https://web.facebook.com/marketplace/')
        if not check_running(): return
        pyautogui.press('enter')
###########################################################################             marketplace page Loading Check  before location changing start
        search_image = 'C:\\facebookBot\\clickImages\\marketplace_logo.png'
        if not check_running(): return
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i), fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        time.sleep(5)  
        if not check_running(): return
###########################################################################             marketplace Loading Check end  
        for _ in range(39):
            pyautogui.press('tab')
            if not check_running(): return
        #################### 1 view
        if not check_running(): return
        pyautogui.press('tab')
        pyautogui.press('enter')
        if not check_running(): return
        time.sleep(2) 
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('esc')
        time.sleep(2)   
        if not check_running(): return
        #################### 2 view
        pyautogui.press('tab')
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(2)  # Replaced sleep_check(2) with time.sleep
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   

        if not check_running(): return
        pyautogui.press('esc')
        time.sleep(2)   
        if not check_running(): return
        #################### 3 view
        pyautogui.press('tab')
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(2)  # Replaced sleep_check(2) with time.sleep
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('esc')
        time.sleep(2)   
        if not check_running(): return
        #########################################################################################
        #####################################################REfering by city
        if not check_running(): return
        pyautogui.hotkey('alt', 'd')
        pyautogui.write('https://web.facebook.com/marketplace/')
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(5) 
        if not check_running(): return
        for _ in range(19):
            pyautogui.press('tab')
        if not check_running(): return
        time.sleep(1)   
        pyautogui.press('enter')   
        if not check_running(): return
        time.sleep(2)   
        pyautogui.press('tab')
        if not check_running(): return
        time.sleep(2)   
        pyautogui.press('tab')
        if not check_running(): return
        time.sleep(2)   
        pyautogui.hotkey('win', '1')
        if not check_running(): return
        time.sleep(2)   
        pyautogui.press('left')
        if not check_running(): return
        time.sleep(2)   
        pyautogui.hotkey('ctrl', 'c')
        if not check_running(): return
        time.sleep(2)   
        pyautogui.hotkey('alt', 'tab')
        if not check_running(): return
        time.sleep(2)   
        pyautogui.hotkey('ctrl', 'v')
        if not check_running(): return
        time.sleep(5)
        pyautogui.keyDown('down')
        if not check_running(): return
        pyautogui.keyUp('down')
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('tab')
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('4')
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('4')
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('tab')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('tab')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('tab')
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('enter')
        #####################################################REfering by city
        if not check_running(): return
        
        
        
        
        
        
        
        #################################################################################################################
        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.write('https://web.facebook.com/marketplace/')
        if not check_running(): return
        pyautogui.press('enter')
###########################################################################             marketplace page Loading Check  after location changing start
        search_image = 'C:\\facebookBot\\clickImages\\marketplace_logo.png'
        if not check_running(): return
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i), fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        time.sleep(5)  
        if not check_running(): return
###########################################################################             marketplace Loading Check end  
        for _ in range(39):
            pyautogui.press('tab')
            if not check_running(): return
        #################### 1 view
        if not check_running(): return
        pyautogui.press('tab')
        pyautogui.press('enter')
        if not check_running(): return
        time.sleep(2) 
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('esc')
        time.sleep(2)   
        if not check_running(): return
        #################### 2 view
        pyautogui.press('tab')
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(2)  # Replaced sleep_check(2) with time.sleep
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   

        if not check_running(): return
        pyautogui.press('esc')
        time.sleep(2)   
        if not check_running(): return
        #################### 3 view
        pyautogui.press('tab')
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(2)  # Replaced sleep_check(2) with time.sleep
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(2)   
        if not check_running(): return
        pyautogui.press('esc')
        time.sleep(2)   
        if not check_running(): return
        #########################################################################################
        
        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.write('https://web.facebook.com/marketplace/category/vehicles')
        time.sleep(5)   
        if not check_running(): return
        pyautogui.press('enter')
        i = 0
        for _ in range(30):
            i+=1
            indicator_label.config(text="Warming Up Page : "+ str(i)+"s", fg="blue")
            pyautogui.press('pagedown')
            if not check_running(): return
            time.sleep(1)   
            
        for _ in range(10):
            pyautogui.hotkey('shift','tab')
            if not check_running(): return
        pyautogui.press('enter')
        time.sleep(3)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('right')
        
            
        
          

        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.write('https://web.facebook.com/marketplace/category/classifieds')
        time.sleep(5)   
        if not check_running(): return
        pyautogui.press('enter')
        i = 0
        for _ in range(30):
            i+=1
            indicator_label.config(text="Warming Up Page : "+ str(i)+"s", fg="blue")
            pyautogui.press('pagedown')
            if not check_running(): return
            time.sleep(1)  
        for _ in range(10):
            pyautogui.hotkey('shift','tab')
            if not check_running(): return
        pyautogui.press('enter')
        time.sleep(3)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('right') 
        
        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.write('https://web.facebook.com/marketplace/category/electronics')
        time.sleep(5)   
        if not check_running(): return
        pyautogui.press('enter')
        i = 0
        for _ in range(30):
            i+=1
            indicator_label.config(text="Warming Up Page : "+ str(i)+"s", fg="blue")
            pyautogui.press('pagedown')
            if not check_running(): return
            time.sleep(1)  
        for _ in range(10):
            pyautogui.hotkey('shift','tab')
            if not check_running(): return
        pyautogui.press('enter')
        time.sleep(3)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('right')
        time.sleep(1)   
        if not check_running(): return
        pyautogui.press('right')           
        
        if not check_running(): return
        pyautogui.hotkey('alt', 'd')
        if not check_running(): return
        pyautogui.write('facebook.com ')
        time.sleep(5)   
        if not check_running(): return
        pyautogui.press('enter')
        i = 0
        for _ in range(30):
            i+=1
            indicator_label.config(text="Warming Up Page : "+ str(i)+"s", fg="blue")
            pyautogui.press('pagedown')
            if not check_running(): return
            time.sleep(1)  
        time.sleep(5)           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #########################################################################################
        time.sleep(1)
        if not check_running(): return
        indicator_label.config(text="Opening Create Item Page.", fg="blue")
        time.sleep(1)
        if not check_running(): return
        pyautogui.hotkey('alt', 'd')
        time.sleep(1)
        if not check_running(): return
        pyautogui.write('https://web.facebook.com/marketplace/create/item')
        time.sleep(1)
        if not check_running(): return
        pyautogui.press('enter')                
###########################################################################             marketplace page Loading Check start
        if not check_running(): return
        search_image = 'C:\\facebookBot\\clickImages\\listing_preview.png'
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i),  fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        time.sleep(5)  
        if not check_running(): return
###########################################################################             Loading Check end
###########################################################################             limit reached Check start
        try:
            indicator_label.config(text="check account ", fg="blue")
            # Locate the textbox on the screen using an image
            textbox_location = pyautogui.locateOnScreen('C:\\facebookBot\\clickImages\\listing_limit_reached.png')
            if textbox_location is not None:
                time.sleep(3)
                indicator_label.config(text="Listing Limit reached.... Closing", fg="red")
                time.sleep(2)   
                indicator_label.config(text="Closing This Profile", fg="red")
                time.sleep(2)   
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)   
                pyautogui.hotkey('win', 'm')
                time.sleep(2)   
                pyautogui.hotkey('win', '1')
                time.sleep(2)   
                pyautogui.press('right')
                time.sleep(0.5)   
                pyautogui.press('right')
                time.sleep(2)   
                pyautogui.write('Listing Limit reached!!!')
                sys.exit()
            indicator_label.config(text="Ready to List New Item!", fg="blue")
            time.sleep(5) 
        except Exception as e:
            print('List limit Reached!!!')
        if not check_running(): return
###########################################################################             limit reached Check end  
        if not check_running(): return
        indicator_label.config(text="Opening Account List.", fg="blue")
        pyautogui.hotkey('win', '1')
        if not check_running(): return
        time.sleep(2) 
        indicator_label.config(text="Changing Tab.", fg="blue")
        if not check_running(): return
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(2)
        if not check_running(): return
        indicator_label.config(text="Copying Image Link.", fg="blue")
        pyautogui.hotkey('ctrl', 'c')
        if not check_running(): return
        indicator_label.config(text="Saving Image Please Wait.", fg="blue")
        save_image()
        if not check_running(): return
        indicator_label.config(text="Image Saved.", fg="blue")
        time.sleep(5)
        if not check_running(): return
        pyautogui.hotkey('win', '1')
        indicator_label.config(text="Opeing Picture", fg="blue")
        if not check_running(): return
        time.sleep(2)
        for _ in range(10):
            pyautogui.press('tab')
            if not check_running(): return
        time.sleep(2) 
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(2) 
        if not check_running(): return
        indicator_label.config(text="Uploading Picture" , fg="blue")
        pyautogui.write('C:\images\picture.jpg')
        if not check_running(): return
        time.sleep(2) 
        pyautogui.press('enter')
        if not check_running(): return
        time.sleep(10) 
        for _ in range(5):
            if not check_running(): return
            pyautogui.press('tab')
        if not check_running(): return
        indicator_label.config(text="Copy Item Name" , fg="blue")
        pyautogui.hotkey('alt', 'tab')
        if not check_running(): return
        time.sleep(2)
        pyautogui.press('right')
        if not check_running(): return
        time.sleep(2) 
        pyautogui.hotkey('ctrl', 'c')
        if not check_running(): return
        indicator_label.config(text="Paste Item Name" , fg="blue")
        time.sleep(2) 
        if not check_running(): return
        pyautogui.hotkey('alt', 'tab')
        time.sleep(2)
        if not check_running(): return
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2) 
        if not check_running(): return
        pyautogui.press('tab')  
        time.sleep(2) 
        if not check_running(): return
        indicator_label.config(text="Copy Item Price" , fg="blue")
        pyautogui.hotkey('alt', 'tab')
        if not check_running(): return
        time.sleep(2)
        pyautogui.press('right')
        if not check_running(): return
        time.sleep(2) 
        pyautogui.hotkey('ctrl', 'c')
        if not check_running(): return
        time.sleep(2) 
        indicator_label.config(text="Paste Item Price" , fg="blue")
        if not check_running(): return
        pyautogui.hotkey('alt', 'tab')
        time.sleep(2)
        if not check_running(): return
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2) 
        if not check_running(): return
        pyautogui.press('tab')  
        indicator_label.config(text="Selecting Category" , fg="blue")
        if not check_running(): return
        time.sleep(2)  
        pyautogui.press('space')  
        if not check_running(): return
        for _ in range(24):
            pyautogui.press('tab')
            if not check_running(): return
        pyautogui.press('space')  
        time.sleep(2)  
        if not check_running(): return
        pyautogui.press('tab')  
        time.sleep(2)  
        if not check_running(): return
        indicator_label.config(text="Selecting Condition" , fg="blue")
        time.sleep(2) 
        pyautogui.press('space')  
        time.sleep(1)
        pyautogui.press('down')  
        
        
        
        if not check_running(): return
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('space')   
        time.sleep(2)  
        if not check_running(): return
        indicator_label.config(text="Copy Description" , fg="blue")
        pyautogui.press('tab') 
        if not check_running(): return
        time.sleep(1)  
        pyautogui.hotkey('ctrl', 'a')
        if not check_running(): return
        time.sleep(1)  
        pyautogui.hotkey('ctrl', 'c')
        if not check_running(): return
        time.sleep(1)  
        value = pyperclip.paste()
        if not check_running(): return
        if(value != ''):
            pyautogui.press('tab') 
            if not check_running(): return
        time.sleep(2)
        pyautogui.hotkey('win', '1')
        if not check_running(): return
        time.sleep(2)
        pyautogui.press('right')
        if not check_running(): return
        time.sleep(2) 
        pyautogui.press('right')
        if not check_running(): return
        time.sleep(2) 
        pyautogui.press('right')
        if not check_running(): return
        time.sleep(2) 
        pyautogui.hotkey('ctrl', 'c')
        if not check_running(): return
        time.sleep(2) 
        if not check_running(): return
        indicator_label.config(text="Paste Description" , fg="blue")
        pyautogui.hotkey('alt', 'tab')
        if not check_running(): return
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        if not check_running(): return
        time.sleep(3) 
###########################################################################             click next button
        if not check_running(): return
        try:
            indicator_label.config(text="Clicking Next Button ", fg="blue")
            time.sleep(2)
            # Locate the textbox on the screen using an image
            neverlocation = pyautogui.locateOnScreen('C:\\facebookBot\\clickImages\\listing_next_button.png')
            if neverlocation is not None:
                nevertextbox_center = pyautogui.center(neverlocation)
                pyautogui.click(nevertextbox_center)
            else:
                indicator_label.config(text="Invalid or Incomplete Details.... Closing", fg="red")
                time.sleep(2)   
                indicator_label.config(text="Closing This Profile", fg="red")
                time.sleep(2)   
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)   
                pyautogui.hotkey('win', 'm')
                time.sleep(2)   
                pyautogui.hotkey('win', '1')
                time.sleep(2)   
                pyautogui.press('right')    
                pyautogui.press('right')
                time.sleep(2)               
                pyautogui.write('Invalid or Incomplete Details !!!')
                indicator_label.config(text="Bot Stopped.", fg="red")
                time.sleep(2)   
                pyautogui.press('enter')
                pyautogui.press('home')
                sys.exit()
            time.sleep(3)  
        except Exception as e:
            indicator_label.config(text="Invalid or Incomplete Details or Corrupted Image.", fg="red")
        time.sleep(2)        
        if not check_running(): return
###########################################################################             click next button   end     
###########################################################################             publish button check
        if not check_running(): return
        search_image = 'C:\\facebookBot\\clickImages\\listing_publish_button.png'
        if not check_running(): return
        def is_page_loaded():
            try:  
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                time.sleep(2)  
                neverrrtextbox_center = pyautogui.center(location)
                pyautogui.click(neverrrtextbox_center)
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i),  fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        if not check_running(): return
        time.sleep(5)  
###########################################################################             publish button check end



        time.sleep(15) 

###########################################################################             boost close button Check start
        if not check_running(): return
        search_image = 'C:\\facebookBot\\clickImages\\close_button.png'
        if not check_running(): return
        def is_page_loaded():
            try:  
                if not check_running(): return
                location = pyautogui.locateOnScreen(search_image, confidence=0.7)
                time.sleep(2)  
                neverrrtextbox_center = pyautogui.center(location)
                pyautogui.click(neverrrtextbox_center)
                return location is not None
            except pyautogui.ImageNotFoundException:
                return False
        i = 0
        if not check_running(): return
        while not is_page_loaded():
            i+=1
            indicator_label.config(text="Waiting for the page to load.... "+ str(i),  fg="blue")
            time.sleep(1)  
        indicator_label.config(text="Page has loaded!", fg="blue")
        time.sleep(5)  
        if not check_running(): return
###########################################################################             boost close button Check end
        if not check_running(): return
        pyautogui.hotkey('alt', 'd')
        pyautogui.write('facebook.com ')
        if not check_running(): return
        pyautogui.press('enter')
        time.sleep(3) 
        if not check_running(): return
        for _ in range(200):
            pyautogui.press('down')
            if not check_running(): return
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        pyautogui.hotkey('win', '1')
        if not check_running(): return
        time.sleep(2)
        pyautogui.press('right')   
        if not check_running(): return
        time.sleep(2)
        pyautogui.write('Item Listed Successfully')
        if not check_running(): return
        time.sleep(2)
        pyautogui.press('enter')   
        if not check_running(): return
        time.sleep(2)
        pyautogui.press('home')      
        if not check_running(): return
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'tab')
        if not check_running(): return
        time.sleep(2)
        pyautogui.press('right')   
        if not check_running(): return
        time.sleep(2)
        pyautogui.press('right')   
        if not check_running(): return
        time.sleep(2)
        pyautogui.write('Item Listed Successfully on this Account')
        if not check_running(): return
        indicator_label.config(text="Item Listed Successfully on this Account.", fg="green")
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('enter')   
        time.sleep(2)
        if not check_running(): return
        pyautogui.press('home')   
        time.sleep(2)
        if not check_running(): return
        sys.exit()
    except Exception as e:
        indicator_label.config(text="Bot has Been Crashed.", fg="red")
        messagebox.showerror("Error", str(e))
    # End the program when bot stops
    sys.exit()
def start_bot():
    global running, bot_thread
    if not running:
        running = True
        bot_thread = threading.Thread(target=bot_function)
        bot_thread.start()
def stop_bot():
    global running
    running = False
    indicator_label.config(text="Bot has stopped.", fg="red")
def restart_bot():
    stop_bot()
    root.after(1000, start_bot)  # Restart the bot after 1 second
# Create GUI application
root = tk.Tk()
root.title("Facebook Automation Bot")
root.geometry("400x200")
def set_window_position_at_top_right(window, width, height):
    screen_width = window.winfo_screenwidth()
    x_offset = screen_width - width
    y_offset = 0  # Top of the screen
    window.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
set_window_position_at_top_right(root, 400, 160)
# Indicator
indicator_label = tk.Label(root, text="Bot is not running.", font=("Bahnschrift Condensed", 12),bg='white',fg='white',width='100')
indicator_label.pack(pady=0.1)
# Bot control buttons
start_button = tk.Button(root, text="Start Bot", command=start_bot,bg='green',fg='white',width=15,height=2,border=0)
start_button.pack(pady=3)
stop_button = tk.Button(root, text="Stop Bot", command=stop_bot,bg='red',fg='white',width=15,height=2,border=0)
stop_button.pack(pady=5)
# Footer text
footer_label = tk.Label(root, text="https://www.fiverr.com/users/mkamranskd/", font=("Dosis", 14))
footer_label.pack(side="bottom", pady=5)
# Ensure the window is always on top
root.attributes('-topmost', True)
# Start the Tkinter event loop
root.mainloop()