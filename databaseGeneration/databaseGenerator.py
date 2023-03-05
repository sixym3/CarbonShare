import random
import string
import datetime
from pymongo import MongoClient
from config import DB_NAME, CONNECTION_URL
from faker import Faker
from eth_account import Account
import secrets

fake = Faker()

# connect to MongoDB
client = MongoClient(CONNECTION_URL)
db = client[DB_NAME]

# define ride and account collections
ride_col = db['rides']
account_col = db['accounts']

# generate random account objects
def create_account():
    is_driver = random.choice([True] + [False] * 2) 
    name = fake.name()
    password = fake.password(length=12)
    private_key = "0x" + secrets.token_hex(32)
    public_key = Account.from_key(private_key).address
    messages = [fake.sentence() for _ in range(random.randint(0, 10))]
    return {
        'name': name,
        'password': password,
        'publicKey': public_key,
        'privateKey': private_key,
        'messages': messages,
        'isDriver': is_driver
    }

# generate random time object
def create_time():
    start_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 364))
    start_hour = random.randint(0, 23)
    start_minute = random.randint(0, 59)
    start_second = random.randint(0, 59)
    start_time = datetime.datetime(start_date.year, start_date.month, start_date.day, start_hour, start_minute, start_second)
    duration = datetime.timedelta(minutes=random.randint(15, 120))
    end_time = start_time + duration
    return start_time.isoformat(), end_time.isoformat() #TODO Check to see format of isoformat is "YYYY-MM-DDTHH:mm:ss"

# generate random distance in meters
def create_distance(start_time, end_time):
    start_datetime = datetime.datetime.fromisoformat(start_time)
    end_datetime = datetime.datetime.fromisoformat(end_time)
    duration = (end_datetime - start_datetime).total_seconds()
    speed_in_mps = random.uniform(5, 20)
    return int(duration * speed_in_mps)

def create_ride(driver):
    # select a random number of riders between 1 and 3
    num_riders = random.randint(1, 3)

    # select random riders from accounts, excluding the driver
    riders = random.sample([acc for acc in accounts if not acc['isDriver']], num_riders)

    # generate start time and end time based on random duration
    start_time, end_time = create_time()

    # generate distance based on start time and end time
    distance = create_distance(start_time, end_time)

    # create ride object
    ride_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return {
        'rideId': ride_id,
        'driver': driver,
        'riders': riders,
        'startTime': start_time,
        'endTime': end_time,
        'distance': distance,
        'rewarded': False,
    }


accounts = [create_account() for _ in range(150)]

# insert accounts into account_col
account_col.insert_many(accounts)

# select drivers from accounts
drivers = [acc for acc in accounts if acc['isDriver']]

# generate rides
rides = []
for driver in drivers:
    for i in range(random.randint(0, 15)):
        rides.append(create_ride(driver))

# insert rides into ride_col
ride_col.insert_many(rides)

