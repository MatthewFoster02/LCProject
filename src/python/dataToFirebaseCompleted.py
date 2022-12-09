# LCCS Climate Change Project
# Examination Number: 000000

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore #Import firebase.

#---------Emissions Function-------------------------------------------------------------------------------------

def emissions():
    import emissions #Import the emissions program for CORGIs.
    emissions = emissions.get_emissions() #Set the list of emissions to variable called emissions.

    years=set() #Create set for the years of data collected, set doesn't allow duplicate years.
    counter=0 #Counter to run through the emissions list.
    while(counter<len(emissions)): #Whilst the counter is less than the length of emissions do what is inside the loop.
        years.add(emissions[counter]['Year']) #Add each unique year to the set.
        counter+=1 #Increase the counter.

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
    # connection=firebase.FirebaseApplication('https://lccs-proje.firebaseio.com/', None) #Connect to firebase database.
    # while(year<=2012): #When the year is less than/equal to 2012 do what is inside the while statement.
    #     emissionsData={ #Variable equal to what I want to send to database.
    #         'Year' : year, #The year.
    #         'CO2' : ch4Emissions[index], #Carbon Emissions value for that year.
    #         'N2O' : co2Emissions[index], #Same with nitrous,
    #         'CH4' : n2oEmissions[index] #and methane.
    #         } 

    #     connection.post('/EmissionsData/', emissionsData) #Send the data to the database.
    #     #print(emissionsData) #Debugging.
    #     year+=1 #Increase the year.
    #     index+=1 #Increase the index counter.
    # print('\n\n\nData Sent!') #Notify the end user that the data has been posted.
    
    totalEmissions=[] #Empty list for all three emissions combined.
    index=0 #Set index position to zero.
    for i in(co2Emissions): #For the indexes in one of the 3 lists.
        totalEmissions.append(ch4Emissions[index]+co2Emissions[index]+n2oEmissions[index]) #Append the total value for that index to the combined list.
        #print(totalEmissions)
        index+=1 #Increase the index position.
    return totalEmissions #Return this list for later analysis.

    #Data from CORGIs is slightly wrong when compared to other data researched on the same topic, the Methane Value
    #is the actual data for Carbon Dioxide, Carbon Dioxide value for Nitrous Oxide and the Nitrous Oxide value for Methane.
    #This explains why the key 'CO2' is linked to ch4emissions list and so on with the others.
    
#----------Sea Levels Function-----------------------------------------------------------------------------------------------------------
    
def seaLevels():
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
    
    # connection=firebase.FirebaseApplication('https://lccs-proje.firebaseio.com/', None) #Connect to the Firebase database.
    # index=1 #Set index counter.
    # year=1920 #Set the year value to 1920, the first year with data.
    # while(year<=2013): #While the year value is less than 2013, the final year with data, run the code inside the loop.
    #     seaLevels={ #Variable is equal to the data I want to send to firebase.
    #         'Year' : year, #Year value.
    #         'Sea Level' : sea_values[index] #Sea level data.
    #         }
    
    #     connection.post('/SeaLevels/', seaLevels) #Send the data to Firebase under the heading 'SeaLevels'.
    #     index+=1 #Increase the index counter.
    #     year+=1 #Increase the year value.
    # print('\n\n\nData Sent!') #Notify the end user that the data has been posted.
    return sea_values #Return this list for later analysis.
        
#-------------Ice Sheets Function----------------------------------------------------------------------------------------------
        
def iceSheets():
    iceSheets=open('src/data/iceSheets.csv', 'r') #Open ice sheets excel file.
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

    # connection=firebase.FirebaseApplication('https://lccs-proje.firebaseio.com/', None) #Make the connection to firebase.

    # counter=0 #Set counter to zero
    # while(counter<len(years)): #Whilst the counter is less than the length of the years list, run code inside the loop.
    #     iceSheetsPost={ #Variable equal to the data I am going to post to firebase.
    #         'Year' : years[counter], #Year value.
    #         'Average mass of Ice Sheets' : iceSheetsValue[counter] #The ice sheets value.
    #         }

    #     connection.post('/Ice Sheets Mass/', iceSheetsPost) #Upload the data.
    #     counter+=1 #Increase the counter by one.
    # print('\n\n\nData Sent!') #Notify the end user that the data has been posted.
    return iceSheetsValue #Return this list for later analysis.
        
#---------------Deforestation Function--------------------------------------------------------------------------------
        
def deforestation():
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

    # connection=firebase.FirebaseApplication('https://lccs-proje.firebaseio.com/', None) #Connect to firebase.

    # year=1990 # Set Year value.
    # counter=0 #Set Index counter value.
    # while(year<=2016): #Whilst year value less than 2016, final year. Run code.
    #     forestPercentValue={ #The variable we are going to post to firebase.
    #         'Year' : year, #Year value is equal to the variable 'year'.
    #         'Forest Percent' : worldValues[counter] #Deforestation value to post is the value in the list 'worldValues', at the index of the counter.
    #         }
    
    #     connection.post('/Deforestation/', forestPercentValue) #Send the data to firebase.
    #     counter+=1 #Increase counter 1.
    #     year+=1 #Increase year variable by 1.
    # print('\n\n\nData Sent!') #Notify the end user that the data has been posted.
    return worldValues #Return this list for later analysis.
    
#----------------------Analysis of Data----------------------------------------------------------------

returnedValues=[emissions(), seaLevels(), iceSheets(), deforestation()] #List of all the lists from the above functions, needed for analysis.

def calculatingAverage(inputList): #Definition to get Average and Maximum values.
    emiList=inputList[0] #Splitting the input list into the individual lists.
    seaList=inputList[1] #"
    iceList=inputList[2] #"
    defList=inputList[3] #"
    
    #Emissions Average---------------------------------------------------------------------------------
    emissionsAverage=[] #Create empty list.
    index=0 #Set index position to zero.
    for i in(emiList): #For the lenth of the list run the code.
        if(index<(len(emiList)-1)): #Only if the index position is less than the length of the whole list(minus one), will the code run. Reason for minus one, needs to be able to acess index position plus one!
            emissionsAverage.append(emiList[index+1]-emiList[index]) #Append the differences between each value to the list.
        index+=1 #Increase index position.
    maxEmissionsValue=max(emissionsAverage) #Max value is equal to the maximum of the list.
    emissionsAverage=sum(emissionsAverage)/len(emissionsAverage) #Average rate of change is equal to the sum divided by the length.
    
    #Sea Levels Average--------------------------------------------------------------------------------
    seaLevelsAverage=[] #Create empty list.
    index=1 #Set index position to one, index 0 is text in this list, the text is not needed.
    for i in(seaList): #For the lenth of the list run the code.
        if(index<(len(seaList)-1)): #Only if the index position is less than the length of the whole list(minus one), will the code run. Reason for minus one, needs to be able to acess index position plus one!
            seaLevelsAverage.append(float(seaList[index+1])-float(seaList[index])) #Append the differences between each value to the list.
        index+=1 #Increase index position.
    maxSeaLevelsValue=round(max(seaLevelsAverage), 3) #Max value is equal to the maximum of the list, rounded to 3 decimal places.
    seaLevelsAverage=round(sum(seaLevelsAverage)/len(seaLevelsAverage), 3) #Average rate of change is equal to the sum divided by the length, rounded to 3 decimal places.
    
    #Ice Sheets Average--------------------------------------------------------------------------------
    iceSheetsAverage=[] #Create empty list.
    index=0 #Set index position to zero.
    for i in(iceList): #For the lenth of the list run the code.
        if(index<(len(iceList)-1)): #Only if the index position is less than the length of the whole list(minus one), will the code run. Reason for minus one, needs to be able to acess index position plus one!
            iceSheetsAverage.append(float(iceList[index+1])-float(iceList[index])) #Append the differences between each value to the list.
        index+=1 #Increase index position.
    maxIceSheetsValue=round(min(iceSheetsAverage), 3) #Max value is equal to the minimum of the list(dealing with the biggest minus number), rounded to 3 decimal places.
    iceSheetsAverage=round(sum(iceSheetsAverage)/len(iceSheetsAverage), 3) #Average rate of change is equal to the sum divided by the length, rounded to 3 decimal places.
    
    #Deforestation Average-----------------------------------------------------------------------------
    deforestationAverage=[] #Create empty list.
    index=0 #Set index position to zero.
    for i in(defList): #For the lenth of the list run the code.
        if(index<(len(defList)-1)): #Only if the index position is less than the length of the whole list(minus one), will the code run. Reason for minus one, needs to be able to acess index position plus one!
            deforestationAverage.append(defList[index+1]-defList[index]) #Append the differences between each value to the list.
        index+=1 #Increase index position.
    maxDeforestationValue=round(min(deforestationAverage), 3) #Max value is equal to the minimum of the list(dealing with the biggest minus number), rounded to 3 decimal places.
    deforestationAverage=round(sum(deforestationAverage)/len(deforestationAverage), 3) #Average rate of change is equal to the sum divided by the length, rounded to 3 decimal places.
    
    #Send code to firebase-----------------------------------------------------------------------------
    cred = credentials.Certificate('C:/Users/mattf/OneDrive/Documents/ComputerScience2020LeavingCertProject/lccsproject-climate-change-firebase-adminsdk-gpt1q-4de2329405.json')

    app = firebase_admin.initialize_app(cred)

    db = firestore.client() #Connect to the Firebase database.

    sendAverages={ #Compile the data.
        'AverageEmissionsChange' : emissionsAverage,
        'AverageSeaLevelsChange' : seaLevelsAverage,
        'AverageIceSheetsChange' : iceSheetsAverage,
        'AverageDeforestationChange' : deforestationAverage,
        'MaxEmissionsValue' : maxEmissionsValue,
        'MaxSeaLevelsValue' : maxSeaLevelsValue,
        'MaxIceSheetsValue' : maxIceSheetsValue,
        'MaxDeforestationValue' : maxDeforestationValue
        }
    
    doc_ref = db.collection(u'AnalysisOfGraph').document('averageAndMax')
    doc_ref.set(sendAverages) #Send to firebase.
    print('\n\n\nData Sent!') #Notify the end user that the data has been posted.

calculatingAverage(returnedValues) #Call the analysis function.

#FYI- The firebase linked is not the one originaly used. This is because if this code was run again it would skew the live graphs on the website!!

