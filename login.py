import os 
import re

"""
    Regex for User Input
"""
nric_regex = re.compile(r"(?i)^[STFG]\d{7}[A-Z]$")


"""
    Function to get NRIC input and check 
"""
def checkNric():
    while True:
        nric = input("Enter NRIC: ").upper()
        if re.match(nric_regex, nric):
            return nric
        else:
            print("Invalid NRIC, please verify")


def client_login():
    while True:
        try: 
            ans = int(input("\nAre u a MOH Officer? \n 1. Yes \n 2. No \nInput: "))

            # Simple Login Authentication for MOH Officer and open client_moh.py file to assess its functions
            if (ans == 1):
                password = input("Enter MOH ID: ")
                if (password == "12345" ):
                    os.system('python client_moh.py')
                else:
                    print("Invalid MOH ID. Please try again.")

            # Login using NRIC and open client.py file, passing users' nric along into the file
            elif (ans == 2):
                nric = checkNric()
                # Open client.py file and pass in nric as argument 
                os.system('python {0} {1}'.format("client.py", nric))

            else: 
                print("Invalid Value, please try again")
                continue
            
        except ValueError:
            print("Invalid Value, please try again")
            continue


if __name__ == '__main__':
    client_login()
