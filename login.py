import os 

def client_login():
    while True:
        try: 
            ans = int(input("\nAre u a MOH Officer? \n 1. Yes \n 2. No \nInput: "))
            if (ans == 1):
                os.system('python client_moh.py')
            elif (ans == 2):
                os.system('python client.py')
            else: 
                print("Invalid Value, please try again")
                continue
        except ValueError:
            print("Invalid Value, please try again")
            continue

if __name__ == '__main__':
    client_login()
