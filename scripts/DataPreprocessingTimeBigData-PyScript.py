
# coding: utf-8

# DataPreprocessing extract data from a specific date out of a dataset

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

apikey = "AIzaSyApj3xGPGx1naRs2DZiUlJ6moRftzWzTJU"

datadir = '../data/nyc_parking_tickets/'
file = 'Parking_Violations_Issued_-_Fiscal_Year_2016.csv'
path = datadir + file


# In[4]:


#Load n lines of dataset
n = 1000000
data = pd.read_csv(path, nrows=n)
#print(data['Issue Date'])
#print(data)
print('First ' + str(n) + ' rows loaded!')


# In[5]:


#data = np.array(json[['street_name', 'house_number', 'issue_date']]) ->for json
data = np.array(data[['Street Name','House Number','Issue Date']])

#date = '2015-08-09'#date of the ticket records ->for json
#dateformat = date + 'T00:00:00.000'#for equals ->for json

dateformat = '07/09/2015'#date you want to extract

count = 0
delTuple = []#array of not needed tuples
for x in data:
    
    if dateformat not in x[2]: 
        #print(x[2] + ' ' + dateformat)
        delTuple.append(count)
        
    count+=1
    continue
    
print('Tuples deleted: ' + str(len(delTuple)))

#print(delTuple)#print Tuples to be deleted

dataTime = np.delete(data, (delTuple), axis=0)#delete not needed tuples

#print(dataTime)#print new array

data = np.delete(dataTime, ([2]), axis=1)#delete date row

data = [[x[0], x[1]] for x in data] #prepare data for maps
datasetCount = len(data)
#datasetCount = 100 #optional: reduce dataset to n rows
data = data[:datasetCount]
print('Data has ' + str(datasetCount) + ' rows')
#print(data)


# In[6]:


from ipywidgets import FloatProgress
from IPython.display import display

f = FloatProgress(min=0, max=datasetCount) #Successful
#e = 0 #Errors


# In[7]:


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


# In[ ]:


f.value = 0
display(f)
e = 0
print('Successful: ' + str(f.value) + '/' + str(datasetCount) + ' Errors: ' + str(e), end='\r')

data = [geocode(x) for x in data]

print(' Finished!')


# In[8]:


#write data.csv
import csv

extractdate = dateformat.replace('/', '-')
with open(datadir + 'geodata_' + extractdate + '_' + str(len(data)) + '_' + file, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
print('Writing Finished!')

