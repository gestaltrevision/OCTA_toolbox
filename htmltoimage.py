# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:53:19 2021

@author: u0090621
"""

from html2image import Html2Image
hti = Html2Image(size=(1920, 1080))

# url to image
hti.screenshot(url='https://www.python.org', save_as='python.png')

# html & css strings to image
html = """<h1> An interesting title </h1> This page will be red"""
css = "body {background: red;}"

hti.screenshot(html_str=html, css_str=css, save_as='red_page.png')

# html & css files to image
hti.screenshot(
    html_file='testclassesids_example.html', # css_file='blue_background.css',
    save_as='testclasseshtml.png'
)

# svg to image
hti.screenshot(other_file='testgradientellipse.svg', size=(324,324))