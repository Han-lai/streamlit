# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:31:16 2022

@author: AlbeeSHLai
"""

import streamlit as st
import requests
from bs4 import BeautifulSoup



def St_Cfg():
    st.set_page_config(
         page_title="AIDI DEFECT App",
         page_icon="🧊",
         layout="wide",
    
     )
    st.sidebar.header("AIDI Image")
    st.sidebar.subheader("依序選擇")
  
 

def AIDIdefect():
    #-------GET TOOL ------------------
    data_colums = ['A2MOR30', 'A2MOR50', 'A2MOR60', 'A2MOR70', 'A2MOR80','A2MOR90']
    TOOLS_tag = st.sidebar.selectbox('Tool_info', data_colums)
    url = f"http://10.88.112.5/AIDI/db_images/{TOOLS_tag}/"
    
    #-------GET RECIPE ------------------
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text,"html.parser")
    recipe_colums  = [(i['href']) for i in soup.select('a')[1:]]
    recipe_tag = st.sidebar.selectbox('recipe_info', recipe_colums)
    
     #-------GET LOT ------------------    
    url = f"http://10.88.112.5/AIDI/db_images/{TOOLS_tag}/{recipe_tag}/"
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text,"html.parser")
    lot_colums  = [(i['href']) for i in soup.select('a')[1:]]
    lot_tag = st.sidebar.selectbox('lot_info', lot_colums)
    
     #-------GET SHEET ------------------  
    url = f"http://10.88.112.5/AIDI/db_images/{TOOLS_tag}/{recipe_tag}/{lot_tag}"
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text,"html.parser")
    
    sheet_colums  = [(i['href']) for i in soup.select('a')[1:]]
    sheet_tag = st.sidebar.selectbox('sheet_info', sheet_colums)
    
     #-------GET image ------------------  
    url = f"http://10.88.112.5/AIDI/db_images/{TOOLS_tag}/{recipe_tag}/{lot_tag}/{sheet_tag}"
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text,"html.parser")
    image_colums  = [ url+(i['href']) for i in soup.select('a')[1:]]
    return image_colums

 
            
def showImage(image_list):
    imageLotCount = 3
    count = 0
    cols = st.columns(imageLotCount)
    # print(cols)
    for i in range(len(image_colums)):
        option_5 = cols[count].text(image_colums[i].split('/')[-1])
        option_5 = cols[count].image(image_colums[i], use_column_width=True)
        count = count + 1
        count = count if count < imageLotCount else 0
        
        
        
if __name__ == '__main__': 
    St_Cfg()
    image_colums=AIDIdefect()
    showImage(image_colums)

              





