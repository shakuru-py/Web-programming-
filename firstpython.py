import sys
import datetime
import copy
import os


def main():
  while True:
    days_of_the_week = [sunday, monday, tuesday,wendesday,thursday,friday,saturday]
    days = list(map(lambda x: x.capitalize(),days_of_the_week)) 
    date = datetime.datetime.now()
    week_number = date.strftime("%V")
    day_of_the_week = date.strftime("%A")
    date_of_the_year = date.strftime("%x")
    break
  


  
if __name__ == "__main__": 
  main()
