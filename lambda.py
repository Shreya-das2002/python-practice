
multiplication = lambda x: x*5
print(multiplication(5))


market = [
    ("apple", 10, 60),
    ("banana", 24, 15),
    ("orange", 10, 50)
]

sorted_bazaar_price = sorted(market, key=lambda x: x[2])
print(sorted_bazaar_price)

sorted_bazaar_price = sorted(market, key=lambda x: x[2], reverse=True)
print(sorted_bazaar_price)

players = [
    {"name": "Shreya", "level": 12, "score": 850},
    {"name": "Rinki", "level": 5, "score": 1200},
    {"name": "Debjani", "level": 12, "score": 400}
]

sorted_player = sorted(players, key=lambda x: (x["level"], x["score"]), reverse=True)
print(sorted_player)