# Gets the countries or their time zones, the length of the flight and the take off or landing hour and
# returns the other hour (or gets the take off and landing hours and returns the flight length)
# 13/07/2022

#TODO find the time zones in the internet instead of asking

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
        print("The take off is at", h)
    elif "land" in question:
        h = landing(timezone1, timezone2)
        print("The landing is at", h)
    else:
        h = length(timezone1, timezone2)
        print("The length of the flight is", h)

# Find the time zone of a country
def timezone(country):
    timezone0 = int(input("What time zone is there? ")) # TODO: make it look for the time zones in the internet
    return timezone0

# Computes the take off hour
def takeoff(timezone1, timezone2):
    flightLength = int(input("How many hours is the flight? "))
    min = int(input("And how many minutes (excluding the full hours)? "))
    flightLength += min / 60
    print("When do you land according to the second timezone (", timezone2, ")? (HH:MM) the hour is between 00:00 to 23:59")
    landingHour = hourToNum(input(""))
    takeoffHour = landingHour - timezone2 - flightLength + timezone1
    takeoffHour = numToValidHour(takeoffHour)
    return takeoffHour

# Computes the landing hour
def landing(timezone1, timezone2):
    flightLength = int(input("How many hours is the flight? "))
    min = int(input("And how many minutes (excluding the full hours)? "))
    flightLength += min / 60
    print("When do you take off according to the first timezone (", timezone1, ")? (HH:MM) the hour is between 00:00 to 23:59")
    takeoffHour = hourToNum(input(""))
    landingHour = takeoffHour - timezone1 + flightLength + timezone2
    landingHour = numToValidHour(landingHour)
    return landingHour

# Computes the length of the flight
def length(timezone1, timezone2):
    print("When do you take off according to the first timezone (", timezone1, ")? (HH:MM) the hour is between 00:00 to 23:59")
    takeoffHour = hourToNum(input(""))
    print("When do you land according to the second timezone (", timezone2, ")? (HH:MM) the hour is between 00:00 to 23:59")
    landingHour = hourToNum(input(""))
    sameDay = input("Do you land on the same day you take off according to the date? ")
    if not("es" in sameDay):
        sameDay = input("Do you land on the day after you take off? ")
        if "es" in sameDay:
            landingHour += 24
        else:
            landingHour -= 24
    flightLength = landingHour - timezone2 - takeoffHour + timezone1
    flightLength = numToHour(flightLength)
    return flightLength


# Gets a string hour and returns it as a number
def hourToNum(str):
    num = int(str[0]) * 10 + int(str[1])
    num = num + (int(str[3]) * 10 + int(str[4])) / 60
    return num

# Gets a number hour and returns it as a string hour between 00:00 and 23:59
def numToValidHour(num):
    while num < 0:
        num += 24
    while num >= 24:
        num -= 24
    return numToHour(num)

# Gets a number hour and returns it as a string
def numToHour(num):
    stri = ""
    stri += str(int(num))
    stri += ":"
    stri += str(int((num - int(num)) * 60))
    return stri

main()
