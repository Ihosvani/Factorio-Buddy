import math

def convertFloatsIntoDecimals(iTimes):

    minNumber = min(iTimes)
    minNumbeSTR = str(minNumber)
    numberToMultiply = 1

    while not minNumbeSTR.endswith('0') and numberToMultiply < 1000000:
        minNumber *= 10
        numberToMultiply *= 10
        minNumbeSTR = str(minNumber)

    for index in range(len(iTimes)):
        iTimes[index] *= numberToMultiply
        iTimes[index] = int(iTimes[index])

    return numberToMultiply, iTimes

def balancedProduction(oTime, iTimes):

    #Calculate raw ratio
    for index in range(len(iTimes)):
        iTimes[index] = oTime / iTimes[index]
    
    listOfValues = convertFloatsIntoDecimals(iTimes)

    numberToDivide = listOfValues[0]
    iTimes = listOfValues[1]

    #find the LCM of all of the ratios
    numberOfOutputsMachines = math.lcm(*iTimes)

    #Dividing the LCM to all of the ratios.
    for index in range(len(iTimes)):
        iTimes[index] = numberOfOutputsMachines / iTimes[index]

    numberOfOutputsMachines/= int(numberToDivide)
    
    minNumber = min(iTimes)
    numberToDivide = 1.0

    while minNumber > 10 :
        minNumber /= 10
        numberToDivide *= 10

    for index in range(len(iTimes)):
        iTimes[index] = iTimes[index] / numberToDivide
        iTimes[index] = int(math.ceil(iTimes[index]))
    
    for index in range(position):
        print("\n" + nameAndTime[index][0] + " takes " + str(int(iTimes[index])) + " machines.") 

    print("\n" + nameOutput + " takes " + str(int(numberOfOutputsMachines / int(numberToDivide))) + " machines.")


while True: 
    nameAndTime = {}
    position = 0
    print()
    numberOfInput = input("How many input items? ")

    for item in range(int(numberOfInput)):

        name = input("Name of the item: ")
        time = float(input("Time to finish item: "))
        amount = float(input("Amount of items that it produces: "))
        amoountItNeeds = float(input("How many items does the output machine needs? "))
        nameAndTime[position] = (name, time/amount*amoountItNeeds)
        position += 1

    nameOutput = input("Name of the output item: ")
    timeOutput = float(input("Time to finish the output item: "))

    iTimes = []

    for cell in range(position):
        iTimes.append(nameAndTime[cell][1])

    balancedProduction(timeOutput, iTimes)





