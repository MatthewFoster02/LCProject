# LCCS Climate Change Project
# Examination Number: 000000

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore #Import firebase.

deforestData=open('src/data/ForestPercentageData.csv', 'r') #Open deforestation excel file.
deforestationData=deforestData.read() #Extract the data from the file.
deforestData.close() #Close the file!

deforestationData=deforestationData.replace('\n', ',') #Make one row by replacing the 'new line', with a coma after each row in the excel file.
deforestationData=deforestationData.replace('\"', '') #Replace the unecassary double quotes with nothing, basically remove them.
deforestationData=deforestationData.split(',') #Change data into a list by splitting on the coma.
#print(len(deforestationData)) #Testing and Debugging 

worldValues=[] #Create empty list.
for i in(deforestationData): #In each index,
    if(deforestationData.index(i)==deforestationData.index('World')): #check if the value of the index 'i' is equal to 'World', if so do what is inside the statement.
        #print('WORKING') #Debugging and Testing.
        #print(deforestationData.index(i))
        indexValue=int(deforestationData.index(i)) #IndexValue is equal to the index at which 'i' is.
        #print(indexValue)
        indexValue=indexValue+34 #Index value is increased to where the first index with deforestation values are found.
        #print(indexValue)
        terminate=int(deforestationData.index(i)) #Terminate variable is equal to the index of 'i' aswell.
        while(indexValue<(terminate+61)): #While the 'indexValue' is less than 'terminate + 61', which is the last index containing deforestation values, run the loop.
            worldValues.append(float(deforestationData[indexValue])) #Append the value, which is a float to the list 'worldValues'.
            indexValue+=1 #Increase the 'indexValue' counter.
            #print(worldValues, indexValue) # Testing and Debugging
            
#print(worldValues)

cred = credentials.Certificate('C:/Users/mattf/OneDrive/Documents/ComputerScience2020LeavingCertProject/lccsproject-climate-change-firebase-adminsdk-gpt1q-4de2329405.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client() #Connect to the Firebase database.

year=1990 # Set Year value.
counter=0 #Set Index counter value.
while(year<=2016): #Whilst year value less than 2016, final year. Run code.
    forestPercentValue={ #The variable we are going to post to firebase.
        'Year' : year, #Year value is equal to the variable 'year'.
        'ForestPercent' : worldValues[counter] #Deforestation value to post is the value in the list 'worldValues', at the index of the counter.
        }
    
    doc_ref = db.collection(u'Deforestation').document(str(year))
    doc_ref.set(forestPercentValue) #Send the data to firebase.
    counter+=1 #Increase counter 1.
    year+=1 #Increase year variable by 1.

    