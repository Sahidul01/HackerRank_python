"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains
, the number of testcases.
Each testcase contains lines, representing time and time

.

Constraints

    Input contains only valid timestamps

    .

Output Format

Print the absolute difference
in seconds. 

______CODES_____
"""

from datetime import datetime,timedelta

def stringToTime(time_string):
    _,day,month,year,time,_=time_string.split(" ")
    hour,minute,second=time.split(":")
    month = datetime.strptime(month, "%b").month
    return datetime(int(year),int(month),int(day),int(hour),int(minute),int(second))
    
def timeZoneConvert(time_zone):
    sign=time_zone[0:1]
    hour=int(time_zone[1:3])
    minutes=int(time_zone[3:])
    time_zone_converted=hour*60 + minutes
    if sign=="+":
        return (-1)*time_zone_converted
    if sign=="-":
        return time_zone_converted
    
    
    
def timeDifference(t1,t2):
    time1=stringToTime(t1)
    time2=stringToTime(t2)
    _,_,_,_,_,timeZone1=t1.split(" ")
    _,_,_,_,_,timeZone2=t2.split(" ")
    timeZone1=timeZoneConvert(timeZone1)
    timeZone2=timeZoneConvert(timeZone2)
    time1+=timedelta(minutes=timeZone1)
    time2+=timedelta(minutes=timeZone2)
    if time1>= time2:
        return((time1-time2).total_seconds())
    if time1<time2:
        return((time2-time1).total_seconds())


n=int(input())
for _ in range(n):
    time1=input().strip()
    time2=input().strip()
    print(int(timeDifference(time1,time2)))
