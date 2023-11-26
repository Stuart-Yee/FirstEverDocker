run = True
while run:
    a = input("select option, okay? ")
    if a.lower() == "q":
        print(f"selected option {a}, quitting...")
        run = False
    else:
        print(f"selected option {a}, keep going!")
