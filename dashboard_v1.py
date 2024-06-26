"""
Dashboard v1
Ron Lee
15 June 20254

Version 1 - get weather and date time and disolay in simple window

"""
import json
import requests

import tkinter.messagebox
import tkinter as tk
import datetime
import time 

def get_weather() :
    # request Cupertino weather data in json format
    url = "http://wttr.in/San_Jose?format=j1"

    # do a get on the url - note the .content part is the json data
    data = requests.get(url)

    # load the json data into a weather dictionary
    weather = json.loads(data.content)
    return weather

# return time string for label
def dtime() :
   now = datetime.datetime.now()
   return str(now.hour)+":"+add_zero(str(now.minute))+":"+add_zero(str(now.second))

# add leading zero to string a
def add_zero(a):
   if int(a) < 10:
      return '0'+a
   else:
      return a

# return date string for label
def ddate():
   now = datetime.datetime.now()
   return "Date: "+str(now.month)+" "+str(now.day)+" "+str(now.year)

def dtemp():
   return "Temp: "+str(weather['current_condition'][0]['temp_F'])

def dcondition():
   return "Current Weather: "+str(weather['current_condition'][0]['weatherDesc'][0]['value'])

# test get_weather
weather = get_weather()
print("The current temperature is", weather['current_condition'][0]['temp_F'])
print(dcondition())


"""
Build thw window
"""
# create root window
root = tk.Tk()
root.title("Dashboard")
root.geometry("550x225")
root.config(bg="white", highlightbackground="blue", highlightthickness=2)
root.eval('tk::PlaceWindow . top')

# create values for labels

# add timestamp label

lbl1 = tk.Label(root, text=ddate(), font=("Bell MT", 32, "bold"), bg="white",fg="black")
lbl1.place(x=15, y=70)

lbl2 = tk.Label(root, text=dtime(), font=("Bell MT", 32, "bold"), bg="white",fg="black")
lbl2.place(x=15, y=30)

lbl3 = tk.Label(root, text=dtemp(), font=("Bell MT", 32, "bold"), bg="white",fg="black")
lbl3.place(x=15, y=110)

lbl4 = tk.Label(root, text=dcondition(), font=("Bell MT", 32, "bold"), bg="white",fg="black")
lbl4.place(x=15, y=150)


"""
main loop to drive display
"""

while True:
  # update content

  # update the time
  lbl2.configure(text=dtime())

  # update the weather
  # note: we don't want to call wttr.in evey second because the weather does not change that fast

  now = datetime.datetime.now()

  # call get_weather when modulo minute is 0 and second is 0
  if now.minute%15 == 0 and now.second == 0:
     
     # log update to the console for debugging
     print("update weather", now)
     weather = get_weather()

  # refresh the screen
  root.update() # these 2 have the same function as mainloop but can be added to.
  root.update_idletasks()

  # run loop once per second so time advances each second
  time.sleep(1)

