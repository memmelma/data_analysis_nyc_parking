
# coding: utf-8

# In[3]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

apikey = "AIzaSyApj3xGPGx1naRs2DZiUlJ6moRftzWzTJU"


# In[7]:


#json = pd.read_json(path_or_buf='https://data.cityofnewyork.us/resource/avxe-2nrn.json')
import os
filepath = 'file://localhost/' + str(os.getcwd()) + '/avxe-2nrn.json'

json = pd.read_json(path_or_buf=filepath)

#bars.head()
print('Dataset loaded')


# In[8]:


data = np.array(json[['street_name', 'house_number']])
    
datasetCount = 1000

data = [[x[0], x[1]] for x in data]
data = data[:datasetCount]
#print(data)


# In[9]:


from ipywidgets import FloatProgress
from IPython.display import display

f = FloatProgress(min=0, max=datasetCount) #Successful
#e = 0 #Errors


# In[10]:


import googlemaps
import json

gmapsAPI = googlemaps.Client(key=apikey)

def geocode( x ):
    geocode = gmapsAPI.geocode(str(x) + 'New York' + 'USA')
    geocode = np.array(geocode)

    global e
    try:
        x[0] = geocode[0].get('geometry').get('location').get('lat')
        x[1] = geocode[0].get('geometry').get('location').get('lng')
    except IndexError:
        x[0] = 0
        x[1] = 0
        e+=1
    f.value += 1
    print('Successful: ' + str(f.value) + '/' + str(datasetCount) + ' Errors: ' + str(e), end='\r')
    return x


# In[11]:


f.value = 0
display(f)
e = 0
print('Successful: ' + str(f.value) + '/' + str(datasetCount) + ' Errors: ' + str(e), end='\r')

data = [geocode(x) for x in data]

print(' Finished!')


# In[13]:


#write data.csv
import csv

with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)


# In[36]:


#print(geocode(['MACDOUNGH ST', '142']))


# In[247]:


#data = [[geocode(x)[0], geocode(x)[1]] for x in data]
#print(data)


# In[ ]:


#data = data[~np.isnan(data).any(axis=1)]


# In[19]:


#read data.csv
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    data = list(reader)
#print(data)

