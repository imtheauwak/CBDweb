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
SERVICE_ACCOUNT_FILE = 'C:\\CBDweb\\keys.json'

# The ID of the Google Sheets file
SAMPLE_SPREADSHEET_ID = "1l0ZdWTDwgqWAgT8xP6BUtVfvm3XLl37W5pGvSsSpTfs"

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
        range="Sheet1!A2",  # The starting point for appending
        valueInputOption='USER_ENTERED',
        insertDataOption='INSERT_ROWS',  # Automatically finds the next empty row
        body=body
    ).execute()

    print(f"{append_result.get('updates').get('updatedCells')} cells appended.")


except HttpError as err:
    print(f"An error occurred: {err}")
