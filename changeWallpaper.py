from google_images_download import google_images_download
import os
import ctypes
import random
def changewallpaper():  
    
    try:
        response = google_images_download.googleimagesdownload()
        w=input('Enter the Keyword to set your wallpaper: ')
        arguments = {"keywords":"%s wallpaper"%w,"limit":1,"size":"large","print_urls":False}   #creating list of arguments
        paths = response.download(arguments)   #passing the arguments to the function
        #print(paths) #printing absolute paths of the downloaded images
        dir = r'downloads\%s wallpaper'%w
        file=random.choice(os.listdir(dir))
        wpp=(os.getcwd())
        temp=('%s\%s'%(wpp,dir))
        wpp=('%s\%s\%s'%(wpp,dir,file))
        #typo(file)
        #typo(wpp)
        f=('%s\%s'%(dir,file))
        #print('No files found')
        ctypes.windll.user32.SystemParametersInfoW(20, 0,r"%s "%wpp , 0)
    except:
        print("Sorry No wallpaper found try some other keywords")

changewallpaper()
