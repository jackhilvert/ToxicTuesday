# ToxicTuesday
My friends host both "Toxic Tuesday" where we are mean to each other and "Wholesome Wednesday" where we lift each other up.
This bot allows us to keep a record of who has caused the most pain, and the most uplifting in the server.
This is accomplished by allowing users to add points for another user by using the command in discord.  

Utilizes many features: 

- GoogleSheets API
- Discord Bot API in python
- created a package that allows for interfacing with the google api, this package is used in the bot.py file as an object
-- This creates a little bit more readability in the code and just allowed me to follow what was going on a bit easier. 
## Bot.py   
Required the main bot and all commands and functions

## googleInterface.py
The required oauth and getters and updaters for the google sheets

## Vulnerabilities
Passing a non-real user-id, will result in a non-real user being added.

|Input  | Display on discord | stored in sheet|
| :---  | :---               | :---           |
|@hilvertjack|@hilvertjack| <@5832930.....>|
|@<1111>| Unkown-user| <@1111> |

This would essentially allow the database to be overfilled with fake values should
an attacker choose to do this. It doesn't create much risk for user data, simply a risk of destroying the program by surpassing the range that the GoogleAPI checks for on the Google Sheet. 
