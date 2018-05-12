# pyGtasks
This is a very simple python script that uses the Google Tasks API to update, create, and maintain your google tasks list. 

# Usage

On first usage, simply run the script in python 3 and follow the link in terminal to authenticate your google account, and allow the app to manage your task list.

Commands:
* `gTasksClient.py <id> done`
* `gTasksClient.py <id> add <task description>`
* `gTasksClient.py <id> delete` - deletes task instead of completing it.


# Installation

To install dependencies via pip:

`pip install oauth2client httplib2`
