import sys
import datetime
import copy
import os


def main():
  while True:
    try:
      user_name = str(input("Hi,whats your name :\n").strip())
    except valueError as error:
      print(f"Typing Error", {error})
      sys.exit(1)
    first_name, second_name = user_name.split(" ")
    print(
      f"""First name , {first_name}
      second_name, {second_name}"""
    )
    
    
    #days of the week and the time schedules and reminders
    days_of_the_week = [sunday, monday, tuesday,wendesday,thursday,friday,saturday]
    days = list(map(lambda x: x.capitalize(),days_of_the_week)) 
    date = datetime.datetime.now()
    week_number = date.strftime("%V")
    day_of_the_week = date.strftime("%A")
    date_of_the_year = date.strftime("%x")

    print(f"Hi {user_name}, today is {day_of_the_week} week {week_number} of {date_of_the_year}\n")
    number_of_attempts = 0
    while plan_question_answer == yes  
    plan_question_anser = input("yes or no \n")

    number_of_attempts += 1

    
    break
  


  
if __name__ == "__main__": 
  main()
