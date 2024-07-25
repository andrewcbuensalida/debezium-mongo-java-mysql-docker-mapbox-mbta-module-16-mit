import urllib.request, json
import mysqldb

def callMBTAApi():
    '''This function fetches bus data for route 1 from the MBTA api, selects certain fields and puts it in a list of dictionaries, saves it to the MySQL database, and returns the list of dictionaries'''
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        trips = data['included']
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
    mysqldb.insertMBTARecord(mbtaDictList) 

    return mbtaDictList  