# ToxicTuesday
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
