#!/usr/bin/env python
import datetime

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))

now = datetime.datetime.now()
current_year = now.year
birth_year = current_year - age
in_100_years = birth_year + 100

msg = "You will be 100 years old in " + str(in_100_years)
times = int(raw_input("How many times would you like to see the msg? "))
print (msg + "\n") * times
