## Code in Place
## Ron Lee
## _Time/Date and Weather Dashboard_

Git Hub URL:
https://github.com/ronwlee/cip_dashboard/tree/master

This project produces a simple graphical dashboard in a window on the desktop. 

Code development uses VS Code on a Macbook.
Extended python libraries used:
 - Json
 - requests
 - tkinter
 - datetime
 - time
 - 
 
Screenshot of current version:
![image](images/DashboardScreenshot.png)

# Structure of Code
main file: dashboard_v1.py

## Main challenges
There were three main challenges:
1) use of VScode on a Mac
2) collecting weather data from web site
3) user of Tkinter for graphics 

The first challenge was use of VScode on a Macbook. This was necessary because I needed to add additioal Python libraries and the Code in Place IDE does not support installing and importing additional libraries

Collection of weather data was an interesting challenge. A search in Google turned up several sites with API to get weather data. I found a site called "wttr.in" that return weather in text format and also provided JSON output. Here is a screenshot of the output from wttr.in:
![Alt](images/wttr_in_screenshot.png "Title")
I was able to use the JSON output from wttr.in and it returned a JSON structure that looks like:
![Alt](/JSONviewer.png "Title")
Using the JSON libary I was able to import the JSON structure into a dictionary and quickly reference each element. The JSON view I used was very helpful in browsing and finding the data I was looking for. 

Since I was not using the Code in Place IDE I had to find a graphics libary. A recomendation from the Project forum pointed me to Tkinter. After reading several tutorials I was able to put together the dashboard.

## Comments on code structure



