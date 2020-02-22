
import datetime as dt

one_semester = dt.timedelta(weeks=15)
one_year = dt.timedelta(weeks=52)
this_class = dt.timedelta(hours=1, minutes=15)
finger_snap = dt.timedelta(seconds=.1)

print(one_semester - this_class)
print(this_class + finger_snap)
print(one_semester - one_year)

election_day = dt.date(year=2020, month=11, day=3)
primary_day = dt.date(year=2020, month=3, day=4)
here_we_are = dt.date.today()

# manually do this
here_we_are = dt.date(year=2020, month=3, day=10)

print(type(election_day - primary_day))
print(election_day - primary_day)
print(type(primary_day + one_semester))
print(primary_day + one_semester)

if dt.date.today() == dt.date.today() + finger_snap:
    print("It'll still be the same day a finger snap from now.")
if dt.date.today() == dt.date.today() + this_class:
    print("It'll still be the same day one lecture from now.")
if dt.date.today() == dt.date.today() + one_semester:
    print("It'll still be the same day one semester from now.")

if primary_day < election_day:
    print("The primary occurs before the election, duh!")
else:
    print("Wuuuut??")

start_of_class = dt.time(hour=12, minute=30)
dinner_time = dt.time(hour=18, minute=0)

this_exact_moment = dt.datetime.now()
# manually do this
this_exact_moment = dt.datetime(year=2020, month=3, day=10, hour=9, minute=33,
second=57, microsecond=15432)

terrorist_attack = dt.datetime(year=2001, month=9, day=11, hour=10, minute=33)
todays_class = dt.datetime.combine(here_we_are, start_of_class)
print(this_exact_moment)
print(terrorist_attack)
print(todays_class)
print("Right now it's: {}".format(this_exact_moment))
print("A horrible thing occurred at: {}".format(terrorist_attack))
print("Today's lecture is at: {}".format(todays_class))
