import mysql.connector


def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="MyNewPass", database="MBTAdb", port=3307
    )

    mycursor = mydb.cursor()
    # complete the following line to add all the fields from the table
    sql = """INSERT INTO mbta_buses (
      id, latitude, longitude, occupancy_status, current_status, 
      bikes_allowed, headsign, bearing, current_stop_sequence, updated_at
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    for mbtaDict in mbtaList:
        # complete the following line to add all the fields from the table
        val = (
            mbtaDict["id"],
            mbtaDict["latitude"],
            mbtaDict["longitude"],
            mbtaDict["occupancy_status"],
            mbtaDict["current_status"],
            mbtaDict["bikes_allowed"],
            mbtaDict["headsign"],
            mbtaDict["bearing"],
            mbtaDict["current_stop_sequence"],
            mbtaDict["updated_at"]
        )
        mycursor.execute(sql, val)

    mydb.commit()
