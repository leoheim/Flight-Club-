# Flight-Club-
Cheap Flights Tracker in python, using APIs!

Project in which the user enters the city of origin, and the cities they want to visit, 
setting a minimum ticket price, using several APIs, this code sends you an email when a ticket appears below the price you entered!

APIs Required:
Google Sheet Data Management - https://sheety.co/

Kiwi Partners Flight Search API (Free Signup, Credit Card not required) - https://partners.kiwi.com/

Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

Twilio SMS API - https://www.twilio.com/docs/sms


Program Requirements:
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code.

Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

If the price is lower than the lowest price listed in the Google Sheet then send an email to all Users.

Avoid making too many unnecessary requests with the Sheety API while testing your code. The free tier for the Sheety API only allows 200 requests per month.

Also, enable the PUT option so that you can write to your Google sheet,

Register with the Kiwi Partners Flight Search API,

Your account name should be the same as what you used later in "First name" and "Last name".

There is no need to provide a credit card or billing information (you can skip that section) when you create your "Solution" (previously called "Application").

