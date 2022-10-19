#!/usr/bin/env python
# coding: utf-8

 


import requests
import pandas as pd 
import bs4
import shutil
from PIL import Image
import pandas as pd
from IPython.core.display import HTML

 


url="https://en.wikipedia.org/wiki/List_of_current_defence_ministers"
 

 


c_head = requests.get(url).content
 

 


c_soup = bs4.BeautifulSoup(c_head,'html.parser')
 

 


tables = c_soup.find('table',{'class': 'sortable wikitable'})
 

 


tab = tables.findAll('tr')
#print(tab)


csv_file = pd.read_csv("C:\\Users\\Jairam\\Python Test Programs\\DataFiles - Copy\\country_iso_code.csv",na_filter = False)

list_iso = csv_file.values.tolist()

def call_pres(pres_url):
    pres = requests.get(pres_url).content
    
    #print(pres)
    pres_soup = bs4.BeautifulSoup(pres,'html.parser')
    imagee = pres_soup.find("table",class_="infobox")
    
    
    try:
        images = imagee.find('img')
    except AttributeError as error:    
        images ='--'
    
    base_url='https:'
    
    #print('\n\n Check here',images)
    try:
        ext_url = images.attrs['src']
    except AttributeError as error:
        ext_url='--'
    
    #ext_url = images.attrs['src']
    #print('External URL\n\n',ext_url)
    return ext_url
    
#List_With_Links = {'ISO_CODE':[],'COUNTRY_NAME':[],'OFFICIAL_NAME':[],'OFFICIAL_NAME_URL':[]}
List_With_Links = {'ISO_CODE':[],'COUNTRY_NAME':[],'OFFICIAL_NAME':[],'OFFICIAL_URL':[]}
for tr_row in {122} : #{92}/range(1,len(tab))
    #print(tr_row)
    columns = tab[tr_row].findAll('td')
    #print(columns)
    
        
    
    try:
        name_url = columns[2].find('a').get('href')
        #print(name_url)
        if name_url.find('redlink')>=0:
            name_url='--'
    except AttributeError:
        name_url='--'
    
    #print('\n\n Check name url',name_url)
    
    base_pres='https://en.wikipedia.org'
    
    if name_url !='--':
    
        pres_url = base_pres + name_url
    
    else:
        
        pres_url = '--'
    #print(pres_url)
    
    #print('It is coming here \n\n')
    
    if pres_url !='--':
        
        ext_url = call_pres(pres_url)
        
    else:
        
        ext_url = '--'
     
    
    
    if ext_url != '--':
        
        final_url = base_url + ext_url
    else:
        final_url = '--'
    
    
    try:
        if columns[0].find('a').getText()=='':
            country_name_find=columns[0].findAll('a')[-1].getText()
        else:
            country_name_find=columns[0].find('a').getText()
    except AttributeError:
        country_name_find='--'
        
    #print(country_name_find)
    
    for i in range(len(list_iso)):
        if country_name_find == list_iso[i][0]:
            country_iso_code = list_iso[i][1]
            break
        else:
            country_iso_code = country_name_find
    
    #print(country_iso_code)
    
    try:
        if columns[0].find('a').getText()=='':
            List_With_Links['COUNTRY_NAME'].append(columns[0].findAll('a')[-1].getText())
        else:
            List_With_Links['COUNTRY_NAME'].append(columns[0].find('a').getText())
    except AttributeError:
        List_With_Links['COUNTRY_NAME'].append('--')
        
        
    try:
        List_With_Links['OFFICIAL_NAME'].append(columns[2].find('a').getText())
    except AttributeError:
        List_With_Links['OFFICIAL_NAME'].append('--') 
            
    List_With_Links['OFFICIAL_URL'].append(final_url)
    
    List_With_Links['ISO_CODE'].append(country_iso_code)

 

 

CH_DF = pd.DataFrame(List_With_Links) 
#print(CH_DF)


file_path='C:\\Users\\Jairam\\Python Test Programs\\DataFiles - Copy\\'
file_name=file_path+'List_of_Defense_Minister'+'.csv'
CH_DF.to_csv(file_name, index=False,encoding='utf-8-sig')


 
