import random
coin = random.choice(["heads", "tails"]) 
print(coin)

from random import choice
coin = choice(["heads", "tails"]) 
print(coin) 


number = random.randint(1,10)
print(number)

cards =["apple", "banana", "orange"]
random.shuffle(cards)
print(cards)

import statistics
print(statistics.mean([10, 5]))

import sys
print("hello, MY NAME IS ", sys.argv[1])

if len(sys.argv)<2:
    sys.exit("too few")
elif len(sys.argv)>2:
    sys.exit("too many")

print("hello, MY NAME IS ", sys.argv[1])

import requests
url = "https://catfact.ninja/fact"
try:
    response = requests.get(url)
    print("Success! Status code:", response.status_code)
    print(response.json())
except requests.exceptions.ConnectionError:
    print("Connection failed. Please check if your computer is connected to the internet!")

import json
response = requests.get("https://catfact.ninja/fact")
print(json.dumps(response.json(), indent=2))

from hello import hellos
if __name__ == "__main__":
    if len(sys.argv) == 2:
        hellos(sys.argv[1])
