import requests, threading, random, string, randominfo
#We will use randominfom package to generate random names, to install run following command -> $ pip install randominfo
#Coded by: Fabian Stevens Varon V.
#Credits - Youtube: https://www.youtube.com/watch?v=StmNWzHbQJU

def randomPhoneNumber():

    phoneNumber = []
    finalNumber=""
    phoneNumber.append(random.randint(3, 3)) # the first number should be in the range of 3 to 3
    phoneNumber.append(random.randint(0, 2)) # the second number should be in the range of 0 to 2

    for i in range(1, 10): # the for loop is used to append the other 8 numbers.
        phoneNumber.append(random.randint(0, 8)) # the other 9 numbers can be in the range of 0 to 8.
    # fill the finalNumber variable
    for i in phoneNumber:
        finalNumber+=str(i)
    return finalNumber

#Generate the first part of a fake email
def randomEmailName(gender):
    emailName = randominfo.get_first_name(gender)
    return emailName

#Generate random password could have special Characters and Numbers
def randomPassword(length,special_chars,digits):
    password = randominfo.random_password(length,special_chars,digits)
    return password

#Send first request i.e: {'myData': '5277'}
def doRequestTest2(dataTest2):
    url= 'https://blitloginnpersons.com/test2.php'
    response = requests.post(url, dataTest2).status_code
    return response

#Send second request i.e: {'myData': 'Nilam@yahoo.com xD7Cs*!ax | 32842082767'}
def doRequestTest3(dataTest3):
    url= 'https://blitloginnpersons.com/test3.php'
    response = requests.post(url, dataTest3).status_code
    return response

#To create a dynamic 4 digits key --> required by doRequestTest2()
def randomWithNDigits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


if __name__ == "__main__":
    def bulkAttack():
        successAttacks=0 #To accumulate successfully attacks
        while True:
            gender = ("male", "female") #To pick between Male & Female
            emailLastPart = ("@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com") #To create dynamic fake email providers
            dynamicKey = randomWithNDigits(4) #To generete 4 digits key
            #Creates a fake email calling randomEmailName and adding emailLastPart
            email= randomEmailName(gender= random.choice(gender))+random.choice(emailLastPart)
            #Creates dynmic password with random "security" levels
            password = randomPassword(length=random.randint(8,9), special_chars=bool(random.getrandbits(1)), digits=bool(random.getrandbits(1)))
            tel= '| ' + str(randomPhoneNumber()) #Creates a fake Mobile number
            dataTest2 = {'myData': f'{dynamicKey}'} #Create dict with Attack2 info
            dataTest3 = {'myData': f'{email} {password} {tel}'} #Create dict with Attack3 nfo
            print(f"Attack2 info: {dataTest2}") #Control Print
            print(f"Attack3 info: {dataTest3}") #Control Print
            attackT2= doRequestTest2(dataTest2=dataTest2) #Call attackT2 fun
            attackT3= doRequestTest3(dataTest3=dataTest3) #Call attackT2 fun
            #If responses are 200 increase the successAttacks count +1
            if attackT2 == 200 and attackT3 == 200:
                successAttacks+=1
                print(f"Successfully Attacks: {successAttacks}") #Control Print
            else:
                print(f"Error: {attackT2} - {attackT3}")

#Create 50 Threads to send multiple and different request at time.
threads = []

for i in range(50):
    t = threading.Thread(target=bulkAttack)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()