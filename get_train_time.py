import requests
from bs4 import BeautifulSoup
import re
import MTRdbConnection

# This function is used to slice a list every n elements
def chunks(list_in, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(list_in), n):
        # Create an index range for l of n elements:
        yield list_in[i:i+n]

'''
#Create a list of station you're going to get
stationId_input = list(range(1,12))
'''
def gets_train_time_sta(stationId_input):
  try:
    print("The stations are:",MTRdbConnection.getStationNames(stationId_input),"\nSearching, Please wait a moment...")
    train_time_sta = {}
    for id in stationId_input:
      url = 'http://www.mtr.com.hk/ch/customer/services/service_hours_search.php?query_type=search&station='+str(id)
      #print(url)
      webcode = requests.get(url)
      soup = BeautifulSoup(webcode.text,features="html.parser")

      #Find the result table
      soup = soup.find('div',class_= "resultWrap")
      #print(soup)
      #soup = soup.prettify()

      # Find all elements in time table
      soup = soup.find_all('td')
      # Get direction station from time table
      bound_for_sta = soup[0::3]
      #print(bound_for_sta)

      # Get the station ID
      stations = []
      for sta in bound_for_sta:
        staId = re.sub('\D', '', str(sta))
        staname = MTRdbConnection.getStationName(staId)
        #print(staname)
        stations.append(staname)

      # Use a list to store first last train time per direction (per bound for station)
      first_last_train=[]
      for txt in soup:
        train_time = txt.text
        first_last_train.append(train_time)
      #print(first_last_train)

      # Remove unnecessary '-' in the table
      first_last_train = [txt for txt in first_last_train if txt != '-']
      #print(first_last_train)

      # Split the first last train time table to each direction here
      first_last_train_list = list(chunks(first_last_train, 2))
      #print(first_last_train_list)

      train_time = dict(zip(stations,first_last_train_list))
      #print(train_time)

      train_time_sta[id] = train_time
    return train_time_sta
  except:
    print("Please check if all station ID are valid!")

'''
train_time_sta = gets_train_time_sta([2,3,4,5])
print(train_time_sta)
'''

#Sort the bound for station in dict?