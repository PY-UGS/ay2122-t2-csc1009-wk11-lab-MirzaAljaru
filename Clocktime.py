class ClockTime:
    #Constructor
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def setHours(self,hours):
        self.hours = hours
    
    def setMinutes(self,minutes):
        self.minutes = minutes
    
    def setSeconds(self,seconds):
        self.seconds = seconds
    
    def setTime(self,hours,minutes,seconds):
        self.hours= hours
        self.minutes = minutes
        self.seconds = seconds
    
    def showTime(self):
        print("Time is " + self.hours + ":" + self.minutes + ":" + self.seconds)


hours = input("Enter Hours: ")
minutes = input("Enter Minutes: ")
seconds = input("Enter seconds: ")

ClockTime = ClockTime(hours,minutes,seconds)
ClockTime.showTime()