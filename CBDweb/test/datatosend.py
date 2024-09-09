import os.path
import numpy as np

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'C:\\CBDweb\\test\\keys.json'

# The ID of the Google Sheets file
SAMPLE_SPREADSHEET_ID = "1bHpieEI56Q01x63a3zpEUrPnXfQ7YJJM5v4fOnBPOAY"

# Authenticate using the service account file
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

try:
    # Create the Sheets API service
    service = build("sheets", "v4", credentials=creds)

    # Step 1: Append Data to the Sheet
    new_values = np.array([0 for i in range(371)])
    new_values_list = [new_values.tolist()]

    body = {
        'values': new_values_list
    }

    append_result = service.spreadsheets().values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="Sheet1!A1",  # The starting point for appending
        valueInputOption='USER_ENTERED',
        insertDataOption='INSERT_ROWS',  # Automatically finds the next empty row
        body=body
    ).execute()

    print(f"{append_result.get('updates').get('updatedCells')} cells appended.")

    # Step 2: Read Data from the Sheet
    # Reading data from a specific range
    read_result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="Sheet1!A1:NG5"  # Adjust the range as needed
    ).execute()

    read_values = read_result.get('values', [])

    if not read_values:
        print("No data found.")
    else:
        print("Data retrieved from the sheet:")
        for row in read_values:
            print(row)

except HttpError as err:
    print(f"An error occurred: {err}")
