import urllib.request, json
import mysqldb

def callMBTAApi():
    '''This function fetches bus data for route 1 from the MBTA api, selects certain fields and puts it in a list of dictionaries, saves it to the MySQL database, and returns the list of dictionaries'''
    mbtaDictList = []

    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    try:
      with urllib.request.urlopen(mbtaUrl) as url: # TODO maybe could get the error here instead of wrapping in try/except
        data = json.loads(url.read().decode())
        print('''*********Example data: ''', data)
        trips = data['included'] if 'included' in data else []
        for bus in data['data']:
          busDict = dict()
          # complete the fields below based on the entries of your SQL table
          busDict['id'] = bus['id']
          busDict['longitude'] = bus['attributes']['longitude']
          busDict['latitude'] = bus['attributes']['latitude']
          busDict['occupancy_status'] = bus['attributes']['occupancy_status']
          busDict['current_status'] = bus['attributes']['current_status']
          trip = next((trip for trip in trips if bus['relationships']['trip']['data']['id'] == trip['id']),None) 
          if trip:
            busDict['bikes_allowed'] = trip['attributes']['bikes_allowed']
            busDict['headsign'] = trip['attributes']['headsign']
          busDict['bearing'] = bus['attributes']['bearing']
          busDict['current_stop_sequence'] = bus['attributes']['current_stop_sequence']
          busDict['updated_at'] = bus['attributes']['updated_at']
          
          mbtaDictList.append(busDict)
    except urllib.error.URLError as e:
      print("Error occurred while fetching data from MBTA API:", e)
    mysqldb.insertMBTARecord(mbtaDictList) 

    return mbtaDictList  