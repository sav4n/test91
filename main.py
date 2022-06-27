import random
import requests
import json
from faker import Faker
import time

fake = Faker()

url = input("URL:")
def run():
  payload = json.dumps({
    "personName": fake.name(),
    "phoneNumber": fake.phone_number(),
    "email": fake.email(),
    "city": fake.city(),
    "gender": random.choice(("Female", "male")),
    "age": random.random()*100,
    "companyForm": fake.company(),
    "position": ""
  })
  headers = {
    'Content-Length': '230',
    'Sec-Ch-Ua': '"Chromium";v="103", ".Not/A)Brand";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'lang=en'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.status_code)
  # print(payload)
for i in range(1,999999):
  time.sleep(random.random()*10)
  run();

# print(keys(response))
