# LCCS Climate Change Project
# Examination Number: 000000

import emissions #Import the emissions program for CORGIs.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore #Import firebase.

emissions = emissions.get_emissions() #Set the list of emissions to variable called emissions.

years=set() #Create set for the years of data collected, set doesn't allow duplicate years.
z=0 #Counter to run through the emissions list.
while(z<len(emissions)): #Whilst the counter is less than the length of emissions do what is inside the loop.
    years.add(emissions[z]['Year']) #Add each unique year to the set.
    z+=1 #Increase the counter.

years=list(years) #Convert set into list.

co2Emissions=[] #Create empty lists.
ch4Emissions=[]
n2oEmissions=[]

x=0 #Set counter to zero.
for index in years: #For each of the indexes in years.
    carbonYear=[] #Create empty lists.
    methaneYear=[]
    nitrousYear=[]
    while(x<len(emissions)): #Do what is inside the loop while the counter is less than length of emissions.
        if emissions[x]['Year']==index: #If the year value in the dictionary at the specified index is the same as the value of the index in years do what is inside the if statement.
            carbon=(emissions[x]['Emissions']['Type']['CO2']) #Set carbon equal to the carbon value for that year. 
            methane=(emissions[x]['Emissions']['Type']['CH4']) #Set methane equal to the methane value for that year.
            nitrous=(emissions[x]['Emissions']['Type']['N2O']) #Set nitrous equal to the nitrous value for that year.
            carbonYear.append(carbon) #All the carbon values from the different countries are added to the list
            methaneYear.append(methane) #Same for the methane values,
            nitrousYear.append(nitrous) #and the nitrous values.
        x+=1 #The counter is increased by 1.
    carbonYearCombined=(round(sum(carbonYear))) #Variable set to the rounded sum of all the carbon values in the carbon List. 
    methaneYearCombined=(round(sum(methaneYear))) #Same with methane,
    nitrousYearCombined=(round(sum(nitrousYear))) #and nitrous.
    co2Emissions.append(carbonYearCombined) #The sum of the carbon values for that year is added to carbon emissions list.
    ch4Emissions.append(methaneYearCombined) #Same with methane,
    n2oEmissions.append(nitrousYearCombined) #and nitrous.
    x=0 #Reset the counter in order to search through the values for the next year.

year=1970 #Set the year variable to 1970, first year.
index=0 #Set index counter to zero.

cred = credentials.Certificate('C:/Users/mattf/OneDrive/Documents/ComputerScience2020LeavingCertProject/lccsproject-climate-change-firebase-adminsdk-gpt1q-4de2329405.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client() #Connect to the Firebase database.

while(year<=2012): #When the year is less than/equal to 2012 do what is inside the while statement.
    emissionsData={ #Variable equal to what I want to send to database.
        'Year' : year, #The year.
        'CO2' : ch4Emissions[index], #Carbon Emissions value for that year.
        'N2O' : co2Emissions[index], #Same with nitrous,
        'CH4' : n2oEmissions[index] #and methane.
        } 

    doc_ref = db.collection(u'Emissions').document(str(year))
    doc_ref.set(emissionsData) #Send the data to the database.
    #print(emissionsData) #Debugging.
    year+=1 #Increase the year.
    index+=1 #Increase the index counter.

#Data from CORGIs is slightly wrong when compared to other data researched on the same topic, the Methane Value
#is the actual data for Carbon Dioxide, Carbon Dioxide value for Nitrous Oxide and the Nitrous Oxide value for Methane.
#This explains why the key 'CO2' is linked to ch4emissions list and so on with the others.
    