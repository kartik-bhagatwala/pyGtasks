#KARTIK BHAGATWALA 1/7

from icalendar import Calendar, vDatetime
from dateutil.parser import parse
from datetime import datetime
from datetime import date


def getcurrentdate():
    date=input("enter the date and time rn (in this format: 2018-03-09 10:55:00")
    return date

def parsetime(date_to_parse):
    return datetime.strptime(date_to_parse, '%Y%m%dT%H%M%S%z')
    # return date.today()



time_now=getcurrentdate()
# date_to_check=datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
date_to_check=parsetime(time_now)
print(date_to_check)
# datetime=(time)
assign=open("CalExport.ics","rb")
assigncal=Calendar.from_ical(assign.read())
for component in assigncal.walk():
    if component.name == "VEVENT": 
        start=component.get('dtstart').dt
        # print("start time "+str(start))
        end=component.get('dtend').dt
        # print(type(start))
        # print(type(date_to_check))
        if(len(str(start))>11):
            # print("working")
            if component.name == "VEVENT" and start<date_to_check and end>date_to_check:
                print(component.get('summary'))
                print("this is start "+str(start)+'\n')
                print(component.get('dtend').dt)

assign.close()



