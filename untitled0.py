#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:54:39 2020

@author: sanjanasrinivasareddy
"""

import requests 
URL = "https://www.bechtle.com/de-en/shop/hardware/mobile-computing/mobile-computing-warranties-services--10007008--c/lenovo"
r = requests.get(URL) 
print(r.content) 
import requests 
from bs4 import BeautifulSoup 
  
URL = "https://www.bechtle.com/de-en/shop/hardware/mobile-computing/mobile-computing-warranties-services--10007008--c/lenovo"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify())