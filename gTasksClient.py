# 🥝🍉🥝 Made by Kartik Bhagatwala 🥝🍉🥝
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time
import datetime
import sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def getUnits(seconds):
    if(seconds<60):
        return str(round(seconds))+"s"
    elif(seconds<3600):
        return str(round(seconds/60))+"min"
    elif(seconds<86400):
        return str(round(seconds/3600))+"hr"
    else:
        return str(round(seconds/86400))+"d"
def getTasks(id):
    tasks = service.tasks().list(tasklist=id).execute()
    print(color.PURPLE+color.UNDERLINE+"\nID  Age\t\tDescription",color.END)
    i=0
    idList=[0]
    for task in tasks['items']:
        if(task['status']=="needsAction"):
            i=i+1
            t1 = datetime.datetime.strptime(task['updated'][:-1], '%Y-%m-%dT%H:%M:%S.%f') #TODO figure this shit out
            t2=datetime.datetime.now()
            c = t2 - t1
            if(i%2==0):
                print (color.GREEN+str(i)+"   "+getUnits(abs(c.total_seconds()))+"\t\t"+task['title']+color.END)
            else:
                print (str(i)+"   "+getUnits(abs(c.total_seconds()))+"\t\t"+task['title'])
            idList.append(task['id'])
    return idList

# Setup the Tasks API
SCOPES = 'https://www.googleapis.com/auth/tasks'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('tasks', 'v1', http=creds.authorize(Http()))

# Call the Tasks API
results = service.tasklists().list(maxResults=10).execute()
items = results.get('items', [])
id=" "

listOfTasks=[]
if not items:
    print('No task lists found.')
else:
    for item in items:
        id=(item['id'])
        print(color.YELLOW+color.BOLD+item['title']+color.END)
        listOfTasks=getTasks(item['id'])
        print("")
if(len(sys.argv)>1 and sys.argv[1]=="add"):
    taskStr=' '.join(sys.argv[2:])
    d = datetime.datetime.now()
    task = {
        'updated': (d.isoformat("T") + "Z"),
        'title': taskStr
    }
    result = service.tasks().insert(tasklist=id, body=task).execute()
    print("added task: "+taskStr)

elif(len(sys.argv)>2 and sys.argv[2]=="done"):
    taskId=listOfTasks[int(sys.argv[1])]
    task = service.tasks().get(tasklist=id, task=taskId).execute()
    task['status'] = 'completed'
    result = service.tasks().update(tasklist=id, task=taskId, body=task).execute()
    # Print the completed date.
    print("task "+sys.argv[1]+" done\n")


elif(len(sys.argv)>2 and sys.argv[2]=="delete"):
    print("delete")
    taskId=listOfTasks[int(sys.argv[1])]
    confirm=" "
    while(confirm!="no"):
        confirm=input("Are you sure? (yes/no) ")
        if(confirm=="yes"):
            service.tasks().delete(tasklist=id, task=taskId).execute()
            confirm="no"
    print("\ndeleted task "+sys.argv[1])
