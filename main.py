import datetime  # for timestamp
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
from twilio.rest import Client  # install twilio for sending sms
import requests  # for api's

MaxIter = 5  # max number of iterations in loop

engine = pyttsx3.init()  # object creation
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[1].id)                 # printing first voice
engine.setProperty('voice', voices[0].id)  # setting up voice
english = 'en-in'  # setting up language
hindi = 'hi-in'  # setting up language
language = 'en-in'  # setting up language
yes = ['yes', 'yeah', 'yup', 'yep', 'y', 'ok', 'okay', 'sure', 'okie', 'okie dokie', 'okie dokie', 'guess',
       'yes yes']  # yes
no = ['no', 'nope', 'nah', 'n', 'nope', 'nahi', 'nahi hua', 'nahi hua hai', 'nahi hua hai']  # no
docType = ''  # variable to store document type
account_sid = 'ACbdec4ccbe7604045ba9dae6638c76c13'  # twilio account id
auth_token = 'd5f315f94e64ccf91122ec64a9cf7742'  # twilio auth token
client = Client(account_sid, auth_token)  # twilio client object
price = {'aadhar': 100, 'pan': 200, 'ration': 300, 'tenth': 500, 'twelth': 2000}  # price of documents
aadharNumber = '794944886253'  # variable to store aadhar number


def SearchInFile(docNumber, TobeSearched):
    """
    this function matches if docnumber and to be searched are in same row
    :param docNumber: doc number of the customer
    :param TobeSearched: to be searched
    :return: True if found else False
    """
    # Todo: To be optimized
    file = open(r"C:\Users\utkar\OneDrive\Desktop\DSA Course\academic delivery\dependencies\DummyNew.csv", "r")
    docNumber = docNumber.lower()
    docNumber = docNumber.replace(" ", "")
    print(docNumber)
    for line in file:
        if docNumber in line:
            print(f"{docNumber} found in {line}")
            # check if to be searched is in list
            if TobeSearched in line:
                print(f"{TobeSearched} found in {line}")
                return True

    file.close()
    speak("Sorry we could not find your data")
    endCall()


def speak(audio: str):
    """
    This function takes a string as input and speaks it out
    :param audio:  string
    :return:       None
    """
    print(audio)  # print the string
    engine.say(audio)  # speak the string
    engine.runAndWait()  # run the engine


def wishMe():
    """
    This function wishes the user according to the time of the day
    :return:    None
    """
    hour = int(datetime.datetime.now().hour)  # get the current hour
    if language == "en-in":  # if english
        if 0 <= hour < 12:  # if the hour is between 0 and 12
            speak("Good Morning!")  # say good morning
            speak("Welcome to Digi Setu")  # say welcome to digi setu


        elif 12 <= hour < 18:  # if the hour is between 12 and 18
            speak("Good Afternoon!")  # say good afternoon
            speak("Welcome to Digi Setu")  # say welcome to digi setu

        else:  # if the hour is between 18 and 24
            speak("Good Evening!")  # say good evening
            speak("Welcome to Digi Setu")  # say welcome to digi setu

    else:  # Hindi under construction
        pass


def takeCommand():
    """
    This function takes microphone input from the user and returns string output
    :return:    string
    """
    # It takes microphone input from the user and returns string output
    import speech_recognition as recog  # speech recognition library
    r = sr.Recognizer()  # object creation
    with sr.Microphone(None, None, 2048) as source:  # microphone object creation
        print("Listening...")  # print the string
        r.pause_threshold = 1  # set the pause threshold
        r.adjust_for_ambient_noise(source, duration=1)  # adjust for ambient noise
        audio = r.listen(source)  # listen to the microphone

    try:
        print("Recognizing...")  # print the string
        # remove noise

        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    print(query)
    return query


def ask_language():
    global language
    while True:
        speak("Which language you want to use?")
        speak("Hindi or English?")
        query = takeCommand().lower()
        if "hindi" in query:
            speak("Hindi language selected")
            language = english
            break
        elif "english" in query:
            speak("English language selected")
            language = english
            break
        else:
            speak("Unable to understand your language selection")
            speak("Please select your language again")


def takePhone():
    while True:
        speak("Please enter your phone number")
        phone = takeCommand()
        p = phone.replace(" ", "")

        print(p)
        if len(p) == 10:
            speak("Phone number entered is: " + phone)
            break
        else:
            speak("Please enter a valid phone number")
    return phone


def takeName():
    while True:
        speak("Please enter your name")
        name = takeCommand()
        if name != "None":
            speak("Name entered is: " + name)
            break
        else:
            speak("Please enter a valid name")
    return name


def takeAddress():
    while True:
        speak("Please enter your address")
        address = takeCommand()
        if address != "None":
            speak("Address entered is: " + address)
            break
        else:
            speak("Please enter a valid address")
    return address


def certificateType():
    iterate = 0
    while iterate < MaxIter:
        speak("Please select the education board")
        speak("For cbse say 1")
        speak("For icse say 2")
        board = takeCommand().lower()
        if '1' in board:
            speak("cbse selected")
            board = "cbse"
            break
        elif '2' in board:
            speak("icse selected")
            board = "icse"
            break
        else:
            iterate += 1
            speak("Unable to understand your selection")
            speak("Please select your board again")

    while iterate < MaxIter:
        if iterate == 0:
            speak("Please select your department")
            speak("Available certificates are : tenth Marksheet ,twelth Marksheet, Migration certificates")
        else:
            speak("Please Select Your certificate once again")
            speak("Available certificates are: tenth Marksheet ,twelth Marksheet, Migration certificates")
        query = takeCommand().lower()
        if query in ['tenth ', 'tenth marksheet', '10', '10th', '10th marksheet', '10 marksheet']:
            speak("Tenth marksheet selected")
            return 'tenth'
        elif query in ['twelth ', 'twelth marksheet', '12', '12th', '12th marksheet', '12 marksheet']:
            speak("Twelth marksheet selected")
            return 'twelth'
        else:
            speak("Unable to understand your department selection")
            speak("Please select your department again")
            iterate += 1
            continue
    speak("oops ! Unkown error occured")
    endCall()


def searchCertificate(certificateType: str, roll: str, YoP: str):
    file = open(r"C:\Users\utkar\OneDrive\Desktop\DSA Course\academic delivery\dependencies\DummyNew.csv", "r")
    docNumber = aadharNumber.lower()
    docNumber = docNumber.replace(" ", "")
    print(docNumber)
    for line in file:
        if docNumber in line:
            print(f"(Print){docNumber} found in {line}")
            # check if to be searched is in list
            if roll in line:
                print(f"(Print)roll number {roll} found in {line}")
                address = line.split(",")[2]
                return True, address

    file.close()
    speak("Sorry we could not find your data")
    speak("Oops ! Unkown error occured")
    endCall()


def CertificateDetails(certificateType: str):
    iterate = 0
    YoP, roll = None, None
    while iterate < MaxIter:
        speak(f"Please enter your {certificateType}  roll number")
        roll = takeCommand().lower()
        roll = roll.replace(" ", "")
        if roll != "None":
            speak(f"Roll number entered is: {roll}")
            speak("speak yes if you want to continue")
            speak("speak no if you want to enter again")
            query = takeCommand().lower()
            if query in yes:
                break
            else:
                iterate += 1
                speak("Please enter your roll number again")
                continue
    iterate = 0
    while iterate < MaxIter:
        speak(f"Please enter your {certificateType} class year of passing")
        YoP = takeCommand().lower()
        if YoP != "None":
            speak(f"Year of passing entered is: {YoP}")
            speak("speak yes if you want to continue")
            speak("speak no if you want to enter again")
            query = takeCommand().lower()
            if query in yes:
                break
            else:
                iterate += 1
                speak("Please enter your YoP again")
                continue
    found, address = searchCertificate(certificateType, roll, YoP)
    if found:
        speak(f"Your Marksheet found in our database successfully")
        speak(f"Your marksheet will be delivered to {address}")
        return
    else:
        speak(f"Your Marksheet not found in our database")
        speak("Please contact us later")
    speak("Oops ! Unknown error occured")
    endCall()


def selectDepartment():
    """
    This function is used to select the department from which the user wants delivery.
    :param: None
    :return: department(string)
    """
    # Availible Departments: Revenue, aadhar, Election, ration
    iterate = 0
    while iterate < MaxIter:
        speak("Please select your department")
        query = takeCommand().lower()
        print(query)
        if query in ['pan', 'paan', "pan card", "pancard"]:
            speak("Pan card department selected")
            return "Revenue"
        elif query in ["adhaar", 'aadhaar', 'adhaar card', 'aadhar']:
            speak("adhaar department selected")
            return "aadhar"
        elif "election" in query:
            speak("Election department selected")
            return "Election"
        elif "ration" in query:
            speak("Ration department selected")
            return "Ration"
        else:
            speak("Unable to understand your department selection")
            speak("Please select your department again")
            iterate += 1
    speak("Please call again later")
    return "None"


def TypeOldOrNew(doc):
    # ask if document is a new one or old one
    """
    :param: None
    :return: "new" or "old"
    """
    iterate = 0
    while iterate < MaxIter:
        speak("Please select your document type")
        speak("Available document types are: New, Existing")
        query = takeCommand().lower()
        print(query)
        if 'new' in query:
            speak("Category selected is new")
            return "new"
        elif query in ['existing', 'old', 'old document', 'old documents', 'old documents', "already have",
                       "already existing"]:
            speak("Already existing document selected")
            return "existing"
        else:
            speak("Unable to understand your document type selection")
            speak("Please select your document type again")
            iterate += 1
    speak("Your voice is not clear, please call again later")
    endCall()


def takeDoB(docNumber):
    dob = ""
    iterate = 0
    while iterate < MaxIter:
        speak("Please enter your year of birth")
        dob = takeCommand()
        if dob != "None":
            speak("Year of birth entered is: " + dob)
            speak("Please speak yes if you want to confirm your date of birth")
            query = takeCommand().lower()
            if query in yes:
                if SearchInFile(docNumber, dob):
                    speak("Date of birth confirmed")
                    return dob
                else:
                    speak("Date of birth not matching with our records")
                    speak("Please try again later")
                    endCall()
            if query in no:
                speak("Please speak a valid date of birth")
                iterate += 1
                continue
        else:
            speak("Please enter a valid date of birth")
            iterate += 1
    return dob


def authenticate(doc):
    """
    This function is used to authenticate the user with new Document.
    :param: None
    :return: True or False(boolean)
    """
    iterate = 0
    while iterate < MaxIter:
        if doc == "aadhar":
            speak("Please enter Your enrollment number")
            enrollment = takeCommand()
            if enrollment != "None":
                speak("Enrollment number entered is: " + enrollment)
                # Check enrollment number from Customer
                speak("Do you want to confirm your enrollment number, yes or no")
                query = takeCommand().lower()
                if query in yes:
                    if SearchInFile(doc, enrollment):
                        speak("Enrollment number confirmed")
                        return True
                elif query in no:
                    speak("Please enter a valid enrollment number again")
                    iterate += 1
                    continue
            else:
                speak("Please enter a valid enrollment number")
                iterate += 1
                continue
    else:
        endCall()


def Take_Aadhar(type="existing"):
    """
    This function is used to take the user input for the aadhar card.
    :param: None
    :return: adhaar number and Validation  (string)
    """
    iterate = 0
    while iterate < MaxIter:
        speak("Please enter your aadhar number")
        aadhar = takeCommand()
        a = aadhar.replace(" ", "")
        speak("Aadhar number entered is: " + aadhar)
        speak("speak yes to proceed else no if aadhar is wrong")
        query = takeCommand().lower()
        if query in yes:
            return aadhar
        elif query in no:
            speak("Please repeat your valid aadhar number")
            iterate += 1
            continue
        else:
            speak("Please enter a valid aadhar number once again")
            iterate += 1
    speak("Sorry, Your aadhar number is not valid, something went wrong")
    endCall()


def AdhaarDob(aadhar):
    """
    This function is used to take the user input for the aadhar card.
    :return: True or False(boolean)
    """
    iterate = 0
    # check dob from database
    while iterate < MaxIter:
        speak("Please enter your year of birth")
        dob = takeCommand()
        if dob != "None":
            speak("Year of birth entered is: " + dob)
            speak("Please speak yes if you want to confirm your date of birth")
            query = takeCommand().lower()
            if query in yes:
                if SearchInFile(aadhar, dob):
                    speak("Date of birth confirmed")
                    return True
            if query in no:
                speak("Please speak a valid date of birth")
                iterate += 1
                continue
        else:
            speak("Please enter a valid date of birth")
            iterate += 1
    endCall()


def endCall():
    """
    This function is used to end the call.
    :param: None
    :return: None
    """
    speak("Thank you for using our services")
    print("We are Ending call")
    speak("We are Ending call")
    exit()


def generate_uniq_code():
    from random import randint
    return randint(1000, 9999)


def generateSMS(code, phone):
    phone = '+919717020263'
    try:
        message = client.messages.create(
            body=f'Your Unique payment code is: {code}',
            from_='+12252401634',
            to=phone
        )
        print(message.sid)
    except Exception as e:
        speak("Some error in Twilio api please call customer support")
        print(e)
        endCall()



def random_phone_number():
    from random import randint
    return "+91" + str(randint(10000000000, 99999999999))


def create_payment(roll_number, user_certificate_choice, name, aadhaar_Number):
    iterate = 0
    api_url = "https://bexbph1r7b.execute-api.us-west-2.amazonaws.com/default/insert_payment_details?roll_number={roll_number}&certificate={user_certificate_choice}&name={name}&amount={amount}&code={code}&adhaar={aadhaar_Number}"
    while iterate < MaxIter:
        try:
            # generate unique code
            amount = price[user_certificate_choice]
            speak(f"You need to pay rupees {amount} ")
            code = generate_uniq_code()
            speak("Your unique payment code is: " + str(code))
            speak("use this code to pay on UPI 1 2 3 pay on your phone using number pad to pay on the portal")
            speak("We are also sending this code on your SMS ")
            # generate phone number
            phone = random_phone_number()
            # generate sms code
            #todo: uncomment the below line
            # generateSMS(code, phone)
            response = requests.get(api_url.format(roll_number=roll_number, user_certificate_choice=user_certificate_choice, name=name, amount=amount, code=code, aadhaar_Number=aadhaar_Number))
            print(response.text)
            return True

        except Exception as e:
            print(e)
            iterate += 1

# print(create_payment('9138168','twelth', 'utkarsh2', '9283983'))
def authenticateDB(adhaar):
    """
    This function is used to authenticate the user with new Document.
    :param: None
    :return: True or False(boolean)
    """
    """
    {"auth_status": true, "otp": 3487, "name": "utkarsh"}
    """

    iterate = 0
    url = "https://566ey9bxy2.execute-api.us-west-2.amazonaws.com/Working-1/check_adhaar_send_otp?adhaar={adhaar}"
    response = requests.get(url.format(adhaar=adhaar))
    data = response.json()
    print("data = ", data)
    SystemResponse = response.json()['auth_status']
    print("System Response is: ", SystemResponse)
    if SystemResponse == True:
        SystemOTP = response.json()['otp']
        print("System OTP is: ", SystemOTP)
        while iterate < 3:
            speak("Please enter your OTP")
            otp = takeCommand()
            otp = otp.replace(" ", "")
            otp = otp.lower()
            print("OTP after replacing is: ", otp)
            if otp.isdigit():
                if int(otp) == int(SystemOTP):
                    speak("OTP confirmed Successfully")
                    print("Welcome ", response.json()['name'])
                    name = response.json()['name']
                    tenth = response.json()['tenth']
                    twelth = response.json()['twelth']
                    return True, {'data': {'name': name, 'tenth': tenth, 'twelth': twelth}}
                else:
                    speak("Please enter a valid OTP")
                    iterate += 1
                    continue
            else:
                speak("Please enter a valid OTP")
                iterate += 1
                continue
        speak("Maximum attempts reached, please try again later")
        endCall()
    else:
        speak("Sorry, your adhaar number is not verified Hence we are not able to process your request")
        endCall()


# print(authenticateDB(794944886253))

def ask_certificate(tenth=False, twelth=False):
    # case 1: if both are true
    iters = 0
    if not tenth and not twelth:
        speak("There are no certificates associated with your account")
        speak("Please contact our customer care for further assistance")
        endCall()

    while iters < MaxIter:
        if tenth and twelth:
            speak("Which certificate do you want to verify")
            speak("Please speak tenth or twelth")
            query = takeCommand().lower()
            print("You said: ", query)
            if query in ['tenth', 10, '10', 'ten', '10th', '10th']:
                return 'tenth'
            elif query in ['twelth', 12, '12', 'twelve', '12th', '12th', 'well', "none"]:
                return 'twelth'
            else:
                speak("Please speak tenth or twelth")
                iters += 1
        elif tenth:
            return 'tenth'
        elif twelth:
            return 'twelth'

    # max attempts reached
    speak("Maximum attempts reached to select certificate please try again later")
    endCall()


# print(ask_certificate(tenth=True, twelth=False))

def search_certificate_in_db(certificate, aadhaar):
    """
    This function is used to search the certificate in the database.
    :param: certificate
    """
    # Ask the year of passing
    iterate = 0
    while iterate < MaxIter:
        speak(f"Please enter the {certificate} year of passing")
        year = takeCommand()
        year = year.replace(" ", "")
        print("You said: ", year)
        if year.isdigit() and len(year) == 4:
            if 2000 < int(year) < 2020:
                print("Year of passing is: ", year)
                break
            else:
                speak("Please enter a valid year of passing")
                iterate += 1
                continue
        else:
            speak("Please enter a valid year of passing")
            iterate += 1
            continue
    # Take the roll number of the customer
    iterate = 0
    while iterate < MaxIter:
        speak(f"Please enter the {certificate} Roll number")
        cutomer_roll_number = takeCommand()
        cutomer_roll_number = cutomer_roll_number.replace(" ", "")
        print("You said: ", cutomer_roll_number)
        if cutomer_roll_number.isdigit():
            speak("Your entered roll number is: " + cutomer_roll_number)
            speak("Do you want to proceed with verification")
            query = takeCommand().lower()
            if query in yes:
                break
            else:
                iterate += 1
                continue
        else:
            speak("Please enter a valid Roll number")
            iterate += 1
    if iterate == MaxIter:
        speak("Maximum attempts reached to select certificate please try again later")
        endCall()

    # Search the certificate in the database

    api_url = "https://8qsrl7e3hl.execute-api.us-west-2.amazonaws.com/default/search_certificate_db?adhaar={aadhaar}&certificate={certificate}"
    response = requests.get(api_url.format(aadhaar=aadhaar, certificate=certificate))
    print("```SYSTEM RESPONSE``` Response is: ", response.json())
    # Authenticate the customer details
    auth = response.json()['auth_status']
    yop = response.json()['yop']
    roll_number = response.json()['roll_number']

    if auth:
        if int(year) == int(yop):
            if int(cutomer_roll_number) == int(roll_number):
                speak("Certificate verified successfully")
                return roll_number
            else:
                speak("")
    else:
        speak("Sorry, your certificate is not verified Hence we are not able to process your request")
        endCall()


# print(search_certificate_in_db('tenth', '794944886253'))


def main():
    """
    This function is used to take the user input for the aadhar card.
    :param: None
    :return: adhaar number and Validation  (string)
    """
    global language, docType
    wishMe()
    phone = random_phone_number()
    time = (datetime.datetime.now()).strftime("%H_%M_%S")
    formatted_url = "https://nrvjolxpg1.execute-api.us-west-2.amazonaws.com/default/add_call_status?phone={phone_number}&time={current_time}".format(
        phone_number=phone, current_time=time)
    print(formatted_url)
    requests.get(formatted_url)
    # ask_language()
    speak("For Authentication, please tell us your aadhaar details")
    # global adhaarNumber
    aadhaar_Number = Take_Aadhar()
    aadhaar_Number = aadhaar_Number.replace(" ", "")
    print(f"Aadhar Number is {aadhaar_Number}")

    auth = authenticateDB(aadhaar_Number)
    # Auth will receive True or False and data if True
    if auth[0]:
        auth_data = auth[1]['data']
        name = auth_data['name']
        tenth = auth_data['tenth']
        twelth = auth_data['twelth']
        speak(f"Welcome {name} you have been successfully authenticated")
        user_certificate_choice = ask_certificate(tenth=tenth, twelth=twelth)
        roll_number = search_certificate_in_db(user_certificate_choice, aadhaar_Number)
        print(f"Roll Number is {roll_number}")
        if create_payment(roll_number, user_certificate_choice, name, aadhaar_Number):
            speak("You have been successfully registered")
            speak("You will shortly receive a sms regarding your details post payment")
            speak("Thank you for using our services")
            endCall()
        else:
            speak("unknown error")
            endCall()


main()
# CertificateDetails("tenth")
