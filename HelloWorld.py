#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:47:25 2020

@author: eric
"""

import thorpy

application = thorpy.Application(size = [300,300], caption = 'Hello World!')

my_button = thorpy.make_button('Hello World!')
#my_button.center()


quit_button = thorpy.make_button('Quit', func = thorpy.functions.quit_menu_func)
background = thorpy.Background(color= [200,200,255], elements = [my_button, quit_button])
thorpy.store(background)


#menu = thorpy.Menu(my_button)
menu = thorpy.Menu(background)


menu.play()

application.quit()