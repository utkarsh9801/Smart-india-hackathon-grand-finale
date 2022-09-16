"""
Author:  Utkarsh Gupta
Date:    20th July 2022
"""


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

