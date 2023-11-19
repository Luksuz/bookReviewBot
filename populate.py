import time
import requests
import random

nicknames1 = [
    'Ace', 'Sparky', 'Luna', 'Maverick', 'Shadow',
    'Bella', 'Captain', 'Rocky', 'Daisy', 'Gizmo',
    'Lucky', 'Scooter', 'Max', 'Cookie', 'Rosie',
    'Duke', 'Peanut', 'Princess', 'Bear', 'Honey',
    'Oliver', 'Daisy', 'Buddy', 'Willow', 'Tiger',
    'Luna', 'Charlie', 'Lucy', 'Rocky', 'Daisy',
    'Teddy', 'Roxy', 'Jack', 'Bella', 'Gizmo',
    'Sophie', 'Oreo', 'Jasper', 'Daisy', 'Daisy',
    'Luna', 'Rocky', 'Max', 'Daisy', 'Dexter',
    'Sadie', 'Rusty', 'Mocha', 'Bailey', 'Lily'
]

nicknames2 = [
    'Rex', 'Bella', 'Cooper', 'Ruby', 'Chloe',
    'Simba', 'Mia', 'Leo', 'Lily', 'Oscar',
    'Zoey', 'Rocky', 'Luna', 'Teddy', 'Daisy',
    'Milo', 'Lily', 'Oliver', 'Rosie', 'Bear',
    'Zoe', 'Max', 'Mia', 'Luna', 'Jasper',
    'Lucy', 'Bella', 'Buddy', 'Daisy', 'Dexter',
    'Daisy', 'Rocky', 'Daisy', 'Sadie', 'Gizmo',
    'Luna', 'Luna', 'Daisy', 'Daisy', 'Sophie',
    'Lucky', 'Daisy', 'Charlie', 'Peanut', 'Daisy',
    'Ruby', 'Daisy', 'Luna', 'Bear', 'Daisy'
]
last_names = [
    'Smith', 'Johnson', 'Brown', 'Lee', 'Kim',
    'Garcia', 'Chen', 'Müller', 'Patel', 'Lopez',
    'Wang', 'Jones', 'Hernandez', 'Nguyen', 'Smithson',
    'Gomez', "O'Connor", 'Sato', 'Anderson', 'Santos',
    'Ferrari', 'Brownlee', 'Ivanov', 'González', 'Taylor',
    'Yamamoto', 'Kowalski', 'Silva', 'Li', 'Singh',
    'Wilson', 'Kumar', 'Smithfield', 'Gutierrez', 'Bianchi',
    'Morgan', 'Choi', 'Müller', 'Thompson', 'Gupta',
    'Martinez', 'Matsui', 'Robinson', 'Andersen', 'Khan',
    'Cheney', 'Rossi', 'Walker', 'Yilmaz', 'Jansen'
]

"""created = 0
for i in range(1000):
    username = nicknames1[random.randint(0, 49)] + " " + nicknames2[random.randint(0, 49)] + " " + last_names[random.randint(0, 49)]
    email = username.replace(" ", "") + "@gmail.com"
    result = requests.post("http://localhost:8000/api/create_bot", data={"username": username, "email": email, "password": "12345678"})
    print(result.status_code)
    if result.status_code == 201:
        print("Bot created!")
        created += 1
    time.sleep(0.1)
print("Created " + str(created) + " bots!")
"""

bot_accounts = requests.get("http://localhost:8000/api/get_bots").json()
bot_ids = [bot["id"] for bot in bot_accounts]
random_bot = bot_ids[random.randint(0, len(bot_ids) - 1)]
      
