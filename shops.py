list= {
    "piekarnia" : ["chleb", "paczek", "bułki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
print("Lista zakupów")

for shop in list:
    print(f"Ide do {shop.capitalize()}", "i kupuję tam:", (list[shop]))
