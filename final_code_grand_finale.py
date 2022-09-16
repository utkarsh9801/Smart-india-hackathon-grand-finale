"""
Author:  Utkarsh Gupta
Date:    11 August 2022
"""
import datetime  # for timestamp
import pyttsx3  # pip install pyttsx3
import requests  # for api's
import speech_recognition as sr  # pip install speechRecognition
from colorama import Fore, Back
from constants import *
from twilioSetup import *

MaxIter = 5  # max number of iterations in loop

engine = pyttsx3.init()  # object creation

voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id)  # setting up voice

def speak(audio: str) -> None:
    """
    This function takes a string as input and speaks it out
    :param audio:  string
    :return:       None
    """
    print(Fore.LIGHTYELLOW_EX + audio)  # print the string
    engine.say(audio)  # speak the string
    engine.runAndWait()  # run the engine
    print(Fore.RESET)  # reset the color


def wishMe() -> None:
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


def takeCommand() -> str:
    """
    This function takes microphone input from the user and returns string output
    :return:    string
    """
    # It takes microphone input from the user and returns string output
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


def ask_language() -> None:
    """
    This function is used to ask the user to select the language
    :param: None
    """
    global language
    iterate = 0
    while iterate < MaxIter:
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
            iterate += 1
    speak("Sorry, we are unable to understand your language selection")
    speak("please try again later or contact our customer care")


def Take_Aadhar():
    """
    This function is used to take the user input for the aadhar card.
    :param: None
    :return: adhaar number and Validation  (string)
    """
    iterate = 0
    while iterate < MaxIter:
        speak("Please enter your aadhar number")
        adhaar = takeCommand()
        adhaar.replace(" ", "")
        speak("Aadhar number entered is: " + adhaar)
        speak("speak yes to proceed else no if aadhar is wrong")
        query = takeCommand().lower()
        if query in yes:
            return adhaar
        elif query in no:
            speak("Please repeat your valid aadhar number")
            iterate += 1
            continue
        else:
            speak("Please enter a valid aadhar number once again")
            iterate += 1
    speak("Sorry, Your aadhar number is not valid, something went wrong")
    endCall()


def endCall():
    """
    This function is used to end the call.
    :param: None
    :return: None
    """
    speak("Thank you for using our services")
    speak("We are Ending call")
    exit()


def generate_uniq_code() :
    """
    This function is used to generate a unique code
    :param: None
    """
    from random import randint
    return randint(1000, 9999)


def generateSMS(code):
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
    """
    This function is used to generate a random phone number
    :param: None
    """
    from random import randint
    return "+91" + str(randint(10000000000, 99999999999))


def create_payment(roll_number, user_certificate_choice, name, aadhaar_Number):
    iterate = 0
    global yes
    api_url = "https://bexbph1r7b.execute-api.us-west-2.amazonaws.com/default/insert_payment_details?roll_number={roll_number}&certificate={user_certificate_choice}&name={name}&amount={amount}&code={code}&adhaar={aadhaar_Number}"
    while iterate < MaxIter:
        try:
            # generate unique code
            amount = price[user_certificate_choice]
            speak("How many copies do you need")
            copies = takeCommand()

            copies.replace(" ", "")
            # if copies.isalpha():
            #     raise(Exception)
            if 'ee' in copies:
                copies = 3
            elif 'ne' in copies:
                copies = 1
            elif copies in ['two', 'Tu', 'tu', 2, '2'] or 't' in copies:
                copies = 2
            copies = int(copies)
            speak(f"Do you need {copies} copies")
            take_command = takeCommand()
            if take_command in yes:
                pass
            else:
                continue
            prices = amount * copies
            speak(f"You need to pay rupees {prices} ")
            code = generate_uniq_code()
            speak("pay on UPI 1 2 3 pay on your phone using number pad to pay on the portal by clicking *99#")
            speak("We are also sending this code on your SMS ")
            # generate phone number
            # phone = random_phone_number()
            # generate sms code
            # todo: uncomment the below line
            # generateSMS(code, phone)

            response = requests.get(
                api_url.format(roll_number=roll_number, user_certificate_choice=user_certificate_choice, name=name,
                               amount=prices, code=code, aadhaar_Number=aadhaar_Number))
            print(response.text)
            return True
        except Exception as e:
            speak("Sorry I didn't get please try again")
            print(e)
            iterate += 1
    speak("You have crossed maximum reattempts, please try again later")
    endCall()


# print(create_payment('********12', 'twelth', 'important', '9283983'))


def authenticateDB(adhaar):
    """
    This function is used to authenticate the user with new Document.
    :param: None
    :return: True or False(boolean)
    """
    iterate = 0
    url = "https://566ey9bxy2.execute-api.us-west-2.amazonaws.com/Working-1/check_adhaar_send_otp?adhaar={adhaar}"
    response = requests.get(url.format(adhaar=adhaar))
    data = response.json()
    print("data = ", data)
    SystemResponse = response.json()['auth_status']
    print("System Response is: ", SystemResponse)
    if SystemResponse:
        SystemOTP = response.json()['otp']
        print("System OTP is: ", SystemOTP)
        while iterate < 3:
            speak("Please enter your OTP")
            otp = takeCommand()
            # remove non number digit
            temp = ""
            for i in otp:
                if i.isdigit():
                    temp += i
            otp = temp

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
    """
    This function is used to ask the user for the certificate.
    :param: None
    """
    # case 1: if both are true
    iters = 0
    if not tenth and not twelth:
        speak("There are no certificates associated with your account")
        speak("Please contact our customer care for further assistance")
        endCall()

    while iters < MaxIter:
        if tenth and twelth:
            speak("Which certificate do you want to verify")
            speak("Availible Documents for you are tenth or twelth, Please speak tenth or twelth")
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
            speak("Only available document is tenth in our database")
            speak("Do you want to verify tenth")
            query = takeCommand().lower()
            print("You said: ", query)
            if query in yes:
                return 'tenth'
            elif query in no:
                speak("Please contact our customer care for further assistance")
                endCall()
            else:
                speak("Please speak tenth or twelth")
                iters += 1
        elif twelth:
            speak("Only available document is twelth in our database")
            speak("Do you want to verify twelth")
            query = takeCommand().lower()
            print("You said: ", query)
            if query in yes:
                return 'twelth'
            elif query in no:
                speak("Please contact our customer care for further assistance")
                endCall()
            else:
                speak("Please speak tenth or twelth")
                iters += 1
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
    year = 0
    customer_roll_number = 0
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
        customer_roll_number = takeCommand()
        customer_roll_number = customer_roll_number.replace(" ", "")
        print("You said: ", customer_roll_number)
        if customer_roll_number.isdigit():
            speak("Your entered roll number is: " + customer_roll_number)
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
            if int(customer_roll_number) == int(roll_number):
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
        speak(f" Enter your respective board")
        board = takeCommand()
        speak(f" Enter your School code")
        school_code = takeCommand()

        user_certificate_choice = ask_certificate(tenth=tenth, twelth=twelth)
        # asking school code

        roll_number = search_certificate_in_db(user_certificate_choice, aadhaar_Number)
        print(f"Roll Number is {roll_number}")
        if create_payment(roll_number, user_certificate_choice, name, aadhaar_Number):
            speak("You have been successfully registered")
            speak("You will shortly receive a sms regarding your details post payment")
            # speak("Thank you for using our services")
            endCall()
        else:
            speak("unknown error")
            endCall()


if __name__ == '__main__':
    main()
