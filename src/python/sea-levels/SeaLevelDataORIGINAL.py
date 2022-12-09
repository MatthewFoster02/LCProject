# LCCS Climate Change Project
# Examination Number: 000000

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore #Import firebase.

seaLevel=open("src/data/seaLevelexcel.csv", "r") #Open sea level excel file.
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
    
cred = credentials.Certificate('C:/Users/mattf/OneDrive/Documents/ComputerScience2020LeavingCertProject/lccsproject-climate-change-firebase-adminsdk-gpt1q-4de2329405.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client() #Connect to the Firebase database.

index=1 #Set index counter.
year=1920 #Set the year value to 1920, the first year with data.
while(year<=2013): #While the year value is less than 2013, the final year with data, run the code inside the loop.
    seaLevels={ #Variable is equal to the data I want to send to firebase.
        'Year' : year, #Year value.
        'SeaLevel' : sea_values[index] #Sea level data.
        
        }
    doc_ref = db.collection(u'SeaLevels').document(str(year))
    doc_ref.set(seaLevels) #Send the data to Firebase under the heading 'SeaLevels'.
    index+=1 #Increase the index counter.
    year+=1 #Increase the year value.
    
