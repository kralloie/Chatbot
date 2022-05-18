import re
from tokenize import String
from xml.etree.ElementTree import tostring
import differentResponses

def messageProbs(userMessage,recognisedWords,isSingleResponse=False,requiredWords=[]):
    messageAcc = 0
    hasRequiredWords = True

    for word in userMessage:
        if word in recognisedWords:
            messageAcc += 1

    percentage = float(messageAcc) / float(len(recognisedWords))
    
    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWords = False
            break
    
    if hasRequiredWords or isSingleResponse:
        return int(percentage*100)
    else:
        return 0

# Paremeters guide:
# recognisedWords = listofWords
# message = userMessage
# isSingleResponse = singleResponse

def checkAllMessages(message):
    highestProbabilityList = {}

    def response(botResponse,listofWords,singleResponse=False,requiredWords=[]):
        nonlocal highestProbabilityList
        highestProbabilityList[botResponse] = messageProbs(message,listofWords,singleResponse,requiredWords)

    response(differentResponses.greetingResponses(),['hola','holita','holiwis','ola'],singleResponse=True)
    response(differentResponses.statusResponses(),['como','estas','andas'],requiredWords=['como'])
    response(differentResponses.gladToHearResponses(),['bien','perfecto','alegre','espectacular'],singleResponse=True)
    response(differentResponses.godResponses(),['que','es','dios'],requiredWords=['que','es','dios'])
    response(differentResponses.birthdayResponses(),['hoy','es','fue','mi','cumpleaños'],requiredWords=['hoy', 'mi','cumpleaños'])

    bestMatch = max(highestProbabilityList, key=highestProbabilityList.get)
    
    if(highestProbabilityList[bestMatch] != 0):
        print(highestProbabilityList)
        return bestMatch
    else:
        print(highestProbabilityList)
        return differentResponses.unknownSentence()

def getResponse(userInput):
    splitMessage = re.split(r'\s+|[,;?!.-]\s*', userInput.lower())
    response = checkAllMessages(splitMessage)
    return response

while True:
    print('Bot: ' + getResponse(input('You: ')))