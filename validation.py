import re
def Validation(email, password):
    validEmail =  re.match(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", email)
    validPassword = re.fullmatch(r'[A-Za-z0-9!@#$%^&+=]{8,}', password)

    if(validEmail and validPassword):
        print("True")
    else:
        print("False")

        
email = input("E-Mail Adresse: ")
password = input("Passwort: ")



if __name__ == '__main__':
        
    Validation(email, password)





