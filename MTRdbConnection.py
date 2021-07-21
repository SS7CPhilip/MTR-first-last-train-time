import pyodbc
import os

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ='+os.path.join(os.getcwd(),'MTR.accdb')+';'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()

'''
for table_info in crsr.tables(tableType='TABLE'):
    print(table_info.table_name)
'''

def printLineMenu():
    cursor = cnxn.cursor()
    cursor.execute('select * from LineMenu')
    #LineMenu = cursor.fetchall()
    for row in cursor.fetchall():
        print(row)

def getLineName(linenumber):
    cursor = cnxn.cursor()
    cursor.execute('select * from LineMenu WHERE LineID = '+str(linenumber))
    LineName = cursor.fetchone()
    #print(LineName)
    return LineName

def getStationsList(linenumber):
    cursor = cnxn.cursor()
    cursor.execute('select * from Line WHERE LineID = '+str(linenumber))
    StationTable = cursor.fetchall()
    StationList = []
    for element in StationTable:
        StationList.append(element[-1])
    #print(StationList)
    return StationList

def getStationName(stationId):
    cursor = cnxn.cursor()
    cursor.execute('select * from Station WHERE StationID = '+str(stationId))
    stationname = cursor.fetchone()
    stationname = stationname[-1]
    return stationname

def getStationNames(stationIDlist):
    stationnamelist = []
    for stationID in stationIDlist:
        cursor = cnxn.cursor()
        cursor.execute('select * from Station WHERE StationID = '+str(stationID))
        stationnamelist.append(cursor.fetchone())
    return stationnamelist
