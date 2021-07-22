from get_train_time import gets_train_time_sta
import MTRdbConnection
import pandas as pd
import csv

print("____menu_____")
print("Please select how do you want to search.\nStation-wise, press 1; Line-wise, press 2")

# This part write time table to a csv file
def export_file(train_time_sta):
  with open('export.csv', 'w', encoding='utf-8-sig') as f:
    for key in train_time_sta.keys():
        f.write("%s,%s\n"%(MTRdbConnection.getStationName(key),train_time_sta[key]))

while True:
    try:
      selection = int(input())
      if selection == 1:
        try:
          stationId_input = []
          while True:
            stationId_input.append(int(input("Enter station ID you want to search, press Enter for each one you typed.\nIf you done, press Enter now: ")))
          # if the input is not-integer, run the next step
        except:
          print("Searching, Please wait a moment")
          train_time_sta = gets_train_time_sta(stationId_input,0)
          print("The fist last train time per station per direction are:\n",train_time_sta)
          quit()
      elif selection == 2:
        print("Please select a line from the menu below by typing in the number before the line name:")
        MTRdbConnection.printLineMenu()
        # Get user input
        line_input = input()
        print("You selected:")
        print(MTRdbConnection.getLineName(line_input))
        train_time_sta = gets_train_time_sta(MTRdbConnection.getStationsList(line_input),1)
        print("The fist last train time per station per direction are:")
        export_table = pd.DataFrame(train_time_sta.items(), columns=["station", "time"])
        print(export_table)
        export_file(train_time_sta)
        quit()
      else:
        print("Please follow the instruction and try again")
    except:
        print("Program exit. If it doesn't work as intended, please check your input and restart it")
        quit()