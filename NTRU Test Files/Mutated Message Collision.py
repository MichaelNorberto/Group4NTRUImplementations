import time
import secrets

emptyString = ""
spaceString = " "

overallTime = 0.0
overallList = []
for i in range(1,101):

    #Getting User Input
    plaintext = "Hi"
    #Initalizing Timing
    t0 = time.time()

    print("The Message is: ", plaintext, "\n")
    #ASCII Conversion
    asciiString = []
    for character in plaintext:
        asciiString.append((ord(character)))
        
    #Binary Conversion
    binString = []
    for integer in asciiString:
        binString.append(bin(integer).replace("0b", ""))
    ###########################################################################
    #Printing Output 
    binaryStr = []
    testStr = emptyString.join(binString)
    binaryStr.append(int(emptyString.join(binString)))
    print("The binary is: ", spaceString.join(binString))
    print("The length of the binary is: ", len(emptyString.join(binString)))


    mutatedList = []
    mutationRate = 0.325
    binaryStr = list(map(int, str(binaryStr[0])))
    for integer in binaryStr:
        if secrets.SystemRandom().uniform(0.0000,1.0000) < mutationRate:
            integer = integer - (integer * 2)
            mutatedList.append(integer)
        else:
            mutatedList.append(integer)
    s = ''.join(str(mutatedList))
    overallList.append(s)
    t1 = time.time()
    total  = t1 - t0
    overallTime = overallTime + total
    average = overallTime / i
    print(mutatedList)
    print ("The total time to convert the message was: ", total, "s")
    print("The average mapping time was: ", average, "s")

setList = set(overallList)
duplicate = len(overallList) != len(setList)
if duplicate == True:
    print("There were duplicates in the set, duplicates  = ", duplicate)
else:
    print("There were no duplicates in the set, duplicates = ", duplicate)

