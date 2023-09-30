# IMPORTS
from datetime import date

class EMails:
    "Class that deals with all the emails that will be sent to the player (manager)"
    def __init__(self):
        self.emails = []

    def AddEMail(self, message: str, message_date: date, source: str):
        "Method that writes an emailand add it to the list of all emails"
        self.emails.append({"email_id": len(self.emails), "message": message, "date": message_date, "source": source})
        
    def DeleteEmail(self, email_id: int):
        for mail in self.emails:
            if mail["email_id"] == email_id:
                self.emails.remove(mail)

    def CheckAvailableMessages(self, current_date: date):
        todays_messages = []
        for messagedict in self.emails:
            if messagedict["date"] == current_date:
                todays_messages.append(messagedict)

