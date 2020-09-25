import pyrebase
from getpass import getpass


firebaseConfig = {

    "apiKey": "AIzaSyCJYc_UnQLgUGL61TSDWkYmUAiB5r7FTKA",
    "authDomain": "logintokawsay.firebaseapp.com",
    "databaseURL": "https://logintokawsay.firebaseio.com",
    "projectId": "logintokawsay",
    "storageBucket": "logintokawsay.appspot.com",
    "messagingSenderId": "1078824372628",
    "appId": "1:1078824372628:web:6e780d4e097852238c6781",
    "measurementId": "G-771DYQDBX4"



}






firebase = pyrebase.initialize_app(firebaseConfig)


auth=firebase.auth()


email = input("Email : \n")
password = getpass("Password : \n")


user = auth.create_user_with_email_and_password(email, password)


login = auth.sign_in_with_email_and_password(email, password)

auth.send_email_verification(login['idToken'])


auth.send_password_reset_email(email)
print("Successful")
