# pyGtasks
This is a very simple python script that uses the Google Tasks API to update, create, and maintain your google tasks list. 

# Usage

On first usage, simply run the script in python 3 and follow the link in terminal to authenticate your google account, and allow the app to manage your task list.

Commands:
* `gTasksClient.py <id> done`
* `gTasksClient.py <id> add <task description>`
* `gTasksClient.py <id> delete` - deletes task instead of completing it.


# Installation

You will need to have pip3 and python3 installed on your system.

First, create a google API key by following these instructions:

* Follow [this link](https://console.developers.google.com/start/api?id=tasks) to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
* On the Add credentials to your project page, click the Cancel button.
* At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
* Select the Credentials tab, click the Create credentials button and select OAuth client ID.
* Select the application type Other, enter a name ", and click the Create button.
* Click OK to dismiss the resulting dialog.
* Click the file_download (Download JSON) button to the right of the client ID.
* Move this file to the same directory as pyGtasks.py and rename it client_secret.json.
* `python3 gTasksClient.py`, and sign in to your google account via the resulting pop up


To install dependencies via pip:

`pip3 install oauth2client httplib2 google-api-python-client`

