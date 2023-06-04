from datetime import date, datetime, time, timedelta
from colorama import Fore, Style
import pytz
from pytz import timezone

today = date.today()                    # this method creates an object with today's date
print(f"Today     : {Fore.RED} {today} {Style.RESET_ALL}")
print(f"The day   : {Fore.RED} {today.day} {Style.RESET_ALL}")          # .day method returns the day
print(f"The month : {Fore.RED} {today.month} {Style.RESET_ALL}")        # .month method returns the month
print(f"The Year  : {Fore.RED} {today.year} {Style.RESET_ALL}")         # .year method returns the year

# String formatting
print(today.strftime("%A / %d / %B / %Y"))                # strftime formatting is case sensitive
                                                          # %A - Returns the day of the week(Thursday)
                                                          # %d - Returns the day zero padded(05) when < 10
                                                          # %B - Returns the month in a stirng
                                                          # %Y - Returns the year
                                                          # %a - Abbreviate's and return the day of the week(Thu)

# next_year = today.year + 1        # you can do addition with date time

next_year = today.replace(year= today.year + 1 )
print("the date of next year: " , next_year)

difference = abs(next_year - today)
print(f"Only {Fore.RED}{difference.days}{Style.RESET_ALL}  days until next year")
# .days != .day days

Zaphon_birth = date(2000, 11, 10)           # create a date with the date function
#print( Fore.RED + Zaphon_birth.strftime("%A / %d / %B / %Y"), Style.RESET_ALL)
print("The legned was born on: ", Fore.RED + Zaphon_birth.strftime("%A / %d / %B / %Y"), Style.RESET_ALL)

# monday = 0 - sunday = 6 the day of the weeks are represented by integers
print(Zaphon_birth.weekday())               # the .weekday method returns a integer of the weekday

now = datetime.now()
print()
print(now.month)
print(now.hour)
print(now.minute)
print(now.day)

#my_time = time(5, 45, 0)                            # creates a time object
#my_time = time.fromisoformat("17:48:08-07:00")      # time formatter
#print(my_time)
                # %I returns ours in 12 hour clock
                                                    # %M returns the minutes
                                                    # %p returns the PM

#my_girl = date(2023, 5, 27)
#my_girlbday = datetime.combine(my_girl, my_time)                # combines the date and time
#print(my_girlbday.date(), my_girlbday.strftime("%I:%M%p"))      # prints the format

tdelta = timedelta(days=7)
#print(today + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

date2 = date(2023, 11, 10)
til_bday = date2 - today
print(til_bday, "Until my birthday")

dt = datetime(2023, 5, 25, 12, 30, 45, 100000)
print()
print(dt)

print(dt + tdelta)                          # the timedelta object makes a arithmatic fucntion to dates
                                            # timedelta is the difference between two dates

dt_today = datetime.today()                 # tdoay's date
dt_now = datetime.now(tz=pytz.UTC)          # Current date time
dt_utcnow = datetime.utcnow().replace(tzinfo=pytz.UTC)
dt_Hawaii = dt_utcnow.astimezone(pytz.timezone('US/Hawaii'))  # aware time object for Hawaii

print()
print(dt_today)
print(dt_now)
print(dt_utcnow)
print()
print(dt_Hawaii)

#for times in pytz.all_timezones:           # All timezones are in a list in pytz.all_timezones method
    #if times.startswith('US'):             # iterating through the list
        #print(times)

dt_mtn = datetime.now()
print()

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(Fore.MAGENTA + "this is dt_east: ", dt_east.strftime("%I:%M%p"), Style.RESET_ALL)

dtr_string = 'November 10 ,2000'
dtp = datetime.strptime(dtr_string, "%B %d ,%Y")    # format has to be in exact position
                                                    # First argument is the string variable of the date second argument is the new format
print(dtp)

# strftime converts date to a string
# strptime converts string to a date

#print(time.time())                              # returns seconds

#print(time.ctime(1685102481.3980215))           # returns the date in with the seconds as the argument

b1 = timedelta(days=20, minutes=30)
b2 = timedelta(days=30)
b3 = b2 - b1
print()
print(type(b3))
print(b3)

some_date = datetime.fromisoformat('2023-05-26T14:05:13')
utc = timezone('UTC')
loc = utc.localize(some_date)
print(loc)

sydney = timezone("Australia/Sydney")
print()
print(loc.astimezone(sydney))

dt1 = datetime.now()
dt2 = datetime.now(pytz.utc)                             # returns the utc of local area
dt3 = datetime.now(pytz.timezone("Europe/Vienna"))       # .timezone method returns the datetime utc of a region
                                                         # Aware time ^
print()
print(dt1)
print(dt2)
print(dt3)
print()

print(Fore.RED + "pytz example")

date_string = "2023-01-01 12:21:33"
datetime_NY = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

current_timezone = pytz.timezone("US/Eastern")
target_timezone = pytz.timezone("Europe/Paris")
localized_newyork = current_timezone.localize(datetime_NY)
datetime_vienna = localized_newyork.astimezone(target_timezone)

#print(datetime_NY)
#print(localized_newyork)
#print(datetime_vienna)
#print(datetime_vienna.replace(tzinfo=None))
#print(pytz.country_timezones["US"])
#print(localized_newyork.utcoffset())

# get current time utc
current_utc = datetime.now(pytz.timezone("utc"))    # Assigning an object as the utc time
print("UTC: " , current_utc)

# converting utc time
now_east = current_utc.astimezone(timezone("US/Eastern"))
print("EST: ", now_east)

now_paris = current_utc.astimezone(timezone("Europe/Paris"))
print("Paris: ", now_paris)

now_tokyo = current_utc.astimezone(timezone("Asia/Tokyo"))
print("Tokyo: ", now_tokyo)

