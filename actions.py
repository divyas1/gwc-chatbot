import datetime


def choose_action(action):
    text = "Looking for action..."

    if action == "hello":
        text = hello()
    elif action == "time":
        text = get_time()
    elif action == "date":
        text = get_date()
    else:
        text = "No action matched!"

    return text


def hello():
    """
    Says "Hello World" to the user
    """
    print('hello action')

    text = "Hello World"
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
