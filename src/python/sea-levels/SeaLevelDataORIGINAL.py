# LCCS Climate Change Project
# Examination Number: 153686

from firebase import firebase #Import firebase.

seaLevel=open("seaLevelexcel.csv", "r") #Open sea level excel file.
seaData=seaLevel.read() #Extract the data from the excel file.
seaLevel.close() #Close the file!

seaData=seaData.replace("\n", ",") #Replace the new line at the end of each row with a coma to change it into one long row.
seaData=seaData.split(",") #Split the data by the coma and make it into a list.
#print(seaData) Testing and Debugging.

sea_values=[] #Create empty list.

indexValue=1 #Index counter.
while(indexValue<len(seaData)): #Whilst the value of the index counter is less than the length of the Data list, run the code inside the loop.
    sea_values.append(seaData[indexValue]) #Append to the sea_values list the value at the index of the seaData List.
    indexValue+=4 #Increase the index counter by 4, this moves to the next index with a value to be added to the sea_values list.
    
connection=firebase.FirebaseApplication('https://lccsproject-climate-change.firebaseio.com/', None) #Connect to the Firebase database.
index=1 #Set index counter.
year=1920 #Set the year value to 1920, the first year with data.
while(year<=2013): #While the year value is less than 2013, the final year with data, run the code inside the loop.
    seaLevels={ #Variable is equal to the data I want to send to firebase.
        'Year' : year, #Year value.
        'Sea Level' : sea_values[index] #Sea level data.
        
        }
    
    connection.post('/SeaLevels/', seaLevels) #Send the data to Firebase under the heading 'SeaLevels'.
    index+=1 #Increase the index counter.
    year+=1 #Increase the year value.
    
