import time
import winsound
import plyer


message = "You need to drink water please"
title = 'Drinking water reminder'
sound = (500,1000)


try:
    interval = float(input("Enter the interval in seconds: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()
    
# Import the datetime module
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time
date = now.strftime("%d/%m/%Y")
time2 = now.strftime("%H:%M:%S")

# Print the date and time
print(f"Today is {date} and the time is {time2}.")



while True:
    time.sleep(interval)
    winsound.Beep(*sound)
    plyer.notification.notify(title = title,message = message)