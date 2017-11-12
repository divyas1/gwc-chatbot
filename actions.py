import datetime
from random import *

def choose_action(action, params):
    text = "Looking for action..."

    if action == "hello":
        given_name = params.get("given-name")
        text = hello(given_name)
    elif action == "time":
        text = get_time()
    elif action == "date":
        text = get_date()
    elif action == "funfact":
        text = get_funfact() 
    else:
        text = "No action matched!"

    return text


def hello(given_name):
    """
    Says "Hello World" to the user
    """
    print('hello action')

    text = "Hello " + str(given_name)
    return text


def get_time():
    """
    Tells the user the current time
    """
    print('time action')

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    text = "The time is %d:%d" % (hour, minute)
    return text


def get_date():
    """
   Tells user the current date
   """
    print('date action') 
    
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
    text = "The date is %d/%d/%d" % (month, day, year) 
    return text


def get_funfact():
    """
    Tells user a fun fact
    """
    print('funfact action') 
    
    text = ["funfact1", "funfact2"]
  
    num = randint(1, len(text))
    
    return text[num-1]
