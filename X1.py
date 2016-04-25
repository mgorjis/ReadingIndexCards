#This program is written in python 3.5.1
#What is yours?!

import sys
sys.version


#path="/Users/mgorjise/Documents/new/reading/CMU/Model elements and connections April 2016.xlsx"
path="/Users/mgorjise/Documents/new/reading/CMU/New.xlsx"
import pandas as pd
xl = pd.ExcelFile(path,sep='\s*,\s*',encoding='ascii')
xl.sheet_names

df = xl.parse('Sheet1')
df.head()
df.columns

# Create a list of participant in this dictionary form: (graph name: unique id )


ListOfParticipant=[]
ListOfLocation=[]
ListOfUniqueid=[]
ElementType=[]
ListOfInfluence_positive=[]
ListOfInfluence_negative=[]
ParticipantsDict={}
ListOfEvents=[]

def isNaN(num):
    return num != num


import math
import re
nan=float("nan")

for i in range(2,171):
    
    name=df['Graph model variable name'][i].replace(' ','')
    ListOfParticipant.append(name)
    
    #ListOfLocation.append(df['Location'][i])
    
    
    ID=df['Unique ID'][i]
   
    if (':' in ID) == False:
        ID='uniprot:'+ID
    ParticipantsDict.update({name:ID})
    ListOfUniqueid.append(ID)
    
    #ElementType.append(df['Element type'][i])
    
    IP=df['Influence set'][i]  #Influence_positive
    if type(IP)==str:
        IP=IP.replace(';',' ').replace(',',' ').replace('or',' ').replace('and',' ').replace('{',' ').replace('}',' ').replace('[',' ').replace(']',' ').replace('(',' ').replace(')',' ').split()
        ListOfInfluence_positive.append(IP)
        
    IN=df['Unnamed: 28'][i]    #Influence_negative
    if type(IN)==str:
        IN=IN.replace(';',' ').replace(',',' ').replace('or',' ').replace('and',' ').replace('{',' ').replace('}',' ').replace('[',' ').replace(']',' ').replace('(',' ').replace(')',' ').split()
        ListOfInfluence_negative.append(IN)
        
    ET=df['Unnamed: 26'][i]  #Event Type
    ET=str(ET).replace(',',' ').split()
    
    if not isNaN(IP):
        for j in range(0,len(IP)):      
            ListOfEvents.append((IP[j],name,'Positive',ET))
            
    if not isNaN(IN): 
        for j in range(0,len(IN)):
            ListOfEvents.append((IN[j],name,'Negative',ET))
    
 
   #k=0
    #if not isNaN(IP):
        #for j in range(0,len(IP)):
            #if ET[0]=='nan': 
                #ET1='nan' 
            #else:
                #ET1=ET[k]
                
            #ListOfEvents.append((IP[j],name,'Positive',ET1))
            #k=k+1
    #if not isNaN(IN):
        #for j in range(0,len(IN)):
            #if ET[0]=='nan': 
                #ET1='nan' 
            #else:
                #ET1=ET[k]
                
            #ListOfEvents.append((IN[j],name,'Negative',ET1))
            #k=k+1
            
            
print(ListOfEvents)



####################


import networkx as nx
G=nx.DiGraph()

nodes=G.add_nodes_from(ListOfParticipant)

for i in range(0,len(ListOfEvents)):
    if ListOfEvents[i][2]=='Positive':
        G.add_edge(ListOfEvents[i][0],ListOfEvents[i][1],color='red')
    if ListOfEvents[i][2]=='Negative':
        G.add_edge(ListOfEvents[i][0],ListOfEvents[i][1],color='cyan')
        


import matplotlib.pyplot as plt
nx.draw(G,with_labels=True)
plt.show()
           

