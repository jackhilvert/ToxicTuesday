from __future__ import print_function
import pandas as pd
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from oauth2client.service_account import ServiceAccountCredentials



class Sheet():
    def __init__(self, toxicID : str = "1qzzFNkNsQWtg3WbiN9ehDowAPGF_fKQ7Itk6GsBe6u8",wholesomeID: str = "1qzzFNkNsQWtg3WbiN9ehDowAPGF_fKQ7Itk6GsBe6u8" ):
        # self.key = 'AIzaSyCRDxZbrIR9MFD92NfLV1mEU6rh2S6rS8o'
        self.toxicID = toxicID
        self.wholesomeID = wholesomeID
        #initializes the google api:
        SCOPES = ['https://www.googleapis.com/auth/drive']
        tokenPath = "my-discord-bot-317803-2e0d440462ec.json"
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret_138338250270-l5a7r0aaeviqurllcb9bpqhq1oebkisa.apps.googleusercontent.com (1).json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.service = build('sheets', 'v4', credentials=creds)


        #vars that can be accesssed
        self.sheet = self.service.spreadsheets()
        self.tt = self.service.spreadsheets().values().get(spreadsheetId = toxicID, range = "ToxicTuesday!A2:B200").execute().get('values')
        #takes a list of lists and turns it into a dictionary
        self.ToxicTuesdays = {}
        for row in self.tt:
            self.ToxicTuesdays[row[0]] = row[1]
        self.ww= self.service.spreadsheets().values().get(spreadsheetId = wholesomeID, range = "WholesomeWednesday!A2:B200").execute().get('values')
        self.WholesomeWednesdays = {}
        for row in self.ww:
            self.WholesomeWednesdays[row[0]] = row[1]

        #a dictionary with key = username value = row # 
        self.indexedTT = {}
        for row in range(len(self.tt)): 
            self.indexedTT[self.tt[row][0]] = row
        
        self.indexedWW = {}
        for row in range(len(self.ww)): 
            self.indexedWW[self.ww[row][0]] = row
        


    def refresh(self): 
        self.__init__()


    def printToxic(self): 
        currentList = self.tt
        newL = '\n'.join([str(elem).strip("\[\]").replace("\'","") for elem in currentList])
        return newL
    def printWholesome(self):
        currentList = self.ww
        newL = '\n'.join([str(elem).strip("\[\]").replace("\'","") for elem in currentList])
        return newL
    def getToxicList(self):
        return self.tt
    def getWholesomeList(self):
        return self.ww
    def getToxicDict(self): 
        return self.ToxicTuesdays
    def getWholesomeDict(self):
        return self.WholesomeWednesdays


    def updateToxic(self, username: str): 
        try:
            if username in self.ToxicTuesdays: 
                votes = int(self.ToxicTuesdays[username])
                newVotes = votes + 1
                rowNum = int(self.indexedTT[username]) + 2
            else: 
                totalRows = len(self.tt)
                rowNum = totalRows + 2
                newVotes = 1
            values = [
                    [       
                    # Cell values ...
                    username, newVotes
                    ],
            # Additional rows ...
            ]
            body = {
                'values': values
            }   
            NEW_RANGE = "ToxicTuesday!A" + str(rowNum) + ":B" + str(rowNum)
            self.service.spreadsheets().values().update(spreadsheetId = self.toxicID, range = NEW_RANGE, valueInputOption= "RAW", body = body).execute()
            self.refresh()
            return True

        except Exception as e: 
            return False

            
    def updateWholesome(self, username: str): 
        try:
            if username in self.WholesomeWednesdays: 
                votes = int(self.WholesomeWednesdays[username])
                newVotes = votes + 1
                rowNum = int(self.indexedWW[username]) + 2
            else: 
                totalRows = len(self.ww)
                rowNum = totalRows + 2
                newVotes = 1
            values = [
                    [       
                    # Cell values ...
                    username, newVotes
                    ],
            # Additional rows ...
            ]
            body = {
                'values': values
            }   
            NEW_RANGE = "WholesomeWednesday!A" + str(rowNum) + ":B" + str(rowNum)
            self.service.spreadsheets().values().update(spreadsheetId = self.wholesomeID, range = NEW_RANGE, valueInputOption= "RAW", body = body).execute()
            self.refresh()
            return True

        except Exception as e: 
            return False
        

        

if __name__ == '__main__':
    test = Sheet()
    print(test.getToxicDict())
    print(test.getToxicList())
    currentList = test.getToxicList()
    newL = '\n'.join([str(elem).strip("\[\]") for elem in currentList])
    print(newL)
    # print(test.updateToxic("hilvertjack"))
    # print(test.updateToxic("test"))
    # print(test.getToxicDict())

