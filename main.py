# Gets the countries or their time zones, the length of the flight and the take off or landing hour and
# returns the other hour (or gets the take off and landing hours and returns the flight length)
# 13/07/2022

#TODO
#find the time zones in the internet instead of asking

def main():
    question = input("What are you looking for? the length of the flight, the take off hour or the landing hour? ")
    if not("off" in question or "land" in question or "length" in question):
        print("Didn't understand your answer. Pay attention to the spelling")
        main()
        return
    country1 = input("Where do you fly from? ")
    timezone1 = timezone(country1)
    country2 = input("Where do you fly to? ")
    timezone2 = timezone(country2)
    if "off" in question:
        h = takeoff(timezone1, timezone2)
        h = hourDescription(h)
        print("The take off is at", h)
    elif "land" in question:
        h = landing(timezone1, timezone2)
        h = hourDescription(h)
        print("The landing is at", h)
    else:
        h = length(timezone1, timezone2)
        h = minute(h)
        print("The length of the flight is", h[0], ":", int(h[1]))

# Find the time zone of a country
def timezone(country):
    timezone0 = int(input("What time zone is there? ")) # make it look for the time zones in the internet
    return timezone0

# Gets a string hour and returns it as a number
def hour(str):
    num = int(str[0]) * 10 + int(str[1])
    num = num + (int(str[3]) * 10 + int(str[4])) / 60
    return num

# Computes the take off hour
def takeoff(timezone1, timezone2):
    length = hour(input("How long is the flight? (HH:MM) "))
    landing = hour(input("When do you land? (HH:MM) As am/pm " ))
    landing = hourToNum(landing)
    h = landing - length
    h = h + timezone1 - timezone2
    return h

# Computes the landing hour
def landing(timezone1, timezone2):
    length = hour(input("How long is the flight? (HH:MM) "))
    takeoff = hour(input("When do you take off? (HH:MM) As am/pm "))
    takeoff = hourToNum(takeoff)
    h = takeoff + length
    h = h + timezone2 - timezone1
    return h

# Computes the length of the flight
def length(timezone1, timezone2):
    takeoff = hour(input("When do you take off? (HH:MM) As am/pm "))
    takeoff = hourToNum(takeoff)
    landing = hour(input("When do you land? "))
    landing = hourToNum(landing)
    landing = landing + timezone1 - timezone2
    h = landing - takeoff
    return h

# Gets a number representing a hour and returns the hour with number of minutes
def minute(hour):
    hours = int(hour // 1)
    minutes = int((hour % 1) * 60)
    return [hours, minutes]

def hourToNum(hour):
    am = input("Is it am or pm? ")

# Gets a number representing a hour and returns a valid hour with am/pm
# Returns the hour, the number of days passed (a day before/a day after/other), and whether it is am (or pm)
def hourDescription(h):
    days = 0
    am = True
    while h > 24:
        days = days + 1
        h = h - 24
    while h < 0:
        h = h + 24
        days = days - 1
    if h > 12:
        h = h -12
        am = False
    h = minute(h)
    h = str(h[0]) + ":" + str(h[1])
    if am == True:
        h = h + "am"
    else:
        h = h + "pm"
    if days > 0:
        h = h + "," + str(days) + "days after"
    elif days < 0:
        h = h + "," + str(days) + "days after"
    return h

main()