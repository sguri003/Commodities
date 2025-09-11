import sqlalchemy as sq
import urllib.parse
import numpy as np 
import pandas as pd  
import xml.etree.ElementTree as ET

def read_x():
    #get source file in Tree Structure
    tree = ET.parse('test.xml')
    #get root of XML tree
    root = tree.getroot()
    my_dic = {}
    l = tuple
    print(f"{root.tag} {root.attrib}")
    for child in root.iter('movie'):
       print(f"Tag: {child.tag} Attrib: {child.attrib}")
       my_dic.update(child.attrib)
    
    for movie in root.findall("./genre/decade/movie/[year='1992']"):
        print("xpath")
        print(movie.attrib)
   
    #print(root[1].attrib)
    #for node in root.findall('./data/row/'):
        #print(node.find('Series_ID').attrib)
        #print(node.find('Dt'))
        #print(node.findall('Per_Change'))    
        #print(node.findall('Value'))
    #retrive tags from XML
def get_txt(): 
    tree = ET.parse('test.xml')
    root = tree.getroot()
    list = []
    dict = {}
    for child in root.iter():
        print(child.findtext('Series_ID'))
        if child.findtext('Series_ID') !=None:
            list.append(child.findtext('Series_ID'))
        for series in list:
            print(series)
        #for x in root.iter():
            #print(x.tag)
    #for index ,k, v in enumerate(root.items()):
    #    print(f'{k} {v} index {index}') 
#for element in root.iter():
#    print(f"Tag:{element.tag},Text: {element.text},Attr {element.attrib}\n")
def xml_dt():
    tree = ET.parse('CPI_Data.xml')
    xm_df = pd.read_xml('CPI_Data.xml')
    df = pd.DataFrame(data=xm_df, columns=['Series_ID','Dt','Value','Per_Change'])
    print(df.head(10))

def read_fl():
    #reading in regular file
    lines = []
    with open('exprt.xml', 'r') as f:
        for x in f:
            lines.append(x.strip())
            print(x.strip())

def parse_element(elem, item):
    if len(list(elem))==0:
        item[elem.tag]=elem.text 
        
    else:
        for child in list(elem):
            parse_element(child, item)   
            
tree = ET.parse('CPI_Data.xml')
root = tree.getroot()
#make array to store dictionary xml results
data= []
for child in root:
    #dictionary appended to array created abobe.
    item={}
    parse_element(child, item)
    data.append(item)
for i, x in enumerate(data):
    if i<5:
        i+=1
        print(x)
    else:
        break
df = pd.DataFrame(data=data)
#print(df)
