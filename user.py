import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/179b7cfaddeeb283bb7a1f8f8b3bfc07/copiaDeFlightDeals/users"


class User():
    def __init__(self):
        print("Welcome to Leonardo Flight Club.")
        print("We find the best flight deals and email you.")

        self.first_name = input("What is your first name?\n").title()
        self.last_name = input("What is your last name?\n").title()

        self.user_email_1 = input("What is your email?\n")
        self.user_email_2 = input("Type your email again.\n")

        while self.user_email_2 != self.user_email_1:
            self.user_email_2 = input("Emails don't match. Please type your email again.\n")

        print("You're in the club!")

        self.response = requests.get(url=SHEETY_USERS_ENDPOINT)
        self.data = self.response.json()["users"]

        body = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.user_email_1
            }
        }

        update_response = requests.post(url=SHEETY_USERS_ENDPOINT, json=body)
        print(update_response.text)
