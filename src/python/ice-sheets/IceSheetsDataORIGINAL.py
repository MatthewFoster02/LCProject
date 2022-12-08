# LCCS Climate Change Project
# Examination Number: 153686

from firebase import firebase #Import firebase.

iceSheets=open('iceSheets.csv', 'r') #Open ice sheets excel file.
iceSheetsData=iceSheets.read() #Extract the data in the excel file.
iceSheets.close() #Close the file.

iceSheetsData=iceSheetsData.replace('\n', ',') #Replace the new line at the end of each row with a coma, in order to make one long row.
iceSheetsData=iceSheetsData.split(',') #Split the data by coma and turn it into a list.
#print(iceSheetsData) #Testing and Debugging.

years=[] #Create empty lists.
iceSheetsValue=[]

index=3 #Create two index counters
index2=4
while(index<len(iceSheetsData) and index2<len(iceSheetsData)): #While both counters are less than the length of the 'iceSheetsData', run code inside loop.
    years.append(iceSheetsData[index]) #Add year values to the year list.
    iceSheetsValue.append(iceSheetsData[index2]) #Add the ice sheets values to the list.
    index+=3 #Increase the counters by 3 in order to move to the next index that has a year/ice sheets value in it.
    index2+=3
    
#print(years, '\n\n', iceSheetsValue) #Testing and Debugging

connection=firebase.FirebaseApplication('https://lccsproject-climate-change.firebaseio.com/', None) #Make the connection to firebase.

counter=0 #Set counter to zero
while(counter<len(years)): #Whilst the counter is less than the length of the years list, run code inside the loop.
    iceSheetsPost={ #Variable equal to the data I am going to post to firebase.
        'Year' : years[counter], #Year value.
        'Average mass of Ice Sheets' : iceSheetsValue[counter] #The ice sheets value.
        }

    connection.post('/Ice Sheets Mass/', iceSheetsPost) #Upload the data.
    counter+=1 #Increase the counter by one.
