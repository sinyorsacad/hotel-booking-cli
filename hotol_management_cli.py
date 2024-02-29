from datetime import date
Hotel_list = ["Maansoor Hotel", "Jees Hotel", "Koroon Hotel"]
rooms = ["r1", "r2", "r3"]
# Hotel_dec = {
# "maansoor": ["r1", "r2", "r3"]
# "jees": ["r1", "r2", "r3"]
# "Koroon": ["r1", "r2", "r3"]
# }
dates = []
names = []
phones = []
r_numbers = []
b_stays = []
hotel = []
#print(Hotel_list)
#print(rooms)
Chosen = 0
while Chosen != "q":
    print("___________________")
    print("1) Maansoor Hotel ")
    print("2) Jees Hotel")
    print("3) Koroon Hotel\n")
    print("Press 'q' to Quit")
    Chosen = input("Enter hotel you need: ")
    if Chosen == '1':
        print("you choosed Maansoor Hotel")
        print("- - - - - - - - - - - - - - - - - -")
        print("Welcome to Maansoor hotel")
        choice = 0
        while choice != 4:
            print(rooms)
            print("1)add booking")
            print("2)looking up for booking")
            print("3)Display all booking")
            print("4)quit")
            choice = int(input("enter your choice: "))
            if choice == 1:
                print("Adding booking...")

#                while choice1 not in Hotel_list:
#                    print("Hotel not found, please try again")
#                    Hotel = input("enter hotel? ")
#                    if Hotel in Hotel_list:
#                        print("Thanks for adding")
#                        break
                name = input("enter name: ")
                while name == "":
                    print("enter your name")
                    name = input("enter name: ")
                phone = input("enter phone number: ")
                while phone == "":
                    print("enter your phone number")
                    phone = input("enter phone number: ")
                date = str(input("enter date of booking (MM-DD-YY): "))
                while date == "":
                    print("enter your date of booking")
                    date = str(input("enter date of booking: "))
                b_stay = int(input("enter the period of stay: "))
                while b_stay == "":
                    print("please enter your period of stay")
                    b_stay = int(input("enter the period of stay: "))
                r_number = input("room number: ")
                while r_number not in rooms:
                    print("invalid room number")
                    r_number = input("room number: ")
                    if r_number in rooms:
                        break
                Hotel_list.append([name, phone, date, b_stay, r_number])
                b_stays.append(b_stay)
                dates.append(date)
                names.append(name)
                phones.append(phone)
                r_numbers.append(r_number)
                hotel.append([name, phone, date, b_stay, r_number])
                print(f"Thanks {name} for booking Maansoor Hotel\n {hotel}")
            elif choice == 2:
                print("looking up for booking...")
                keyword = input("enter name: ")
                for hotel in Hotel_list:
                    if keyword in hotel:
                        print(hotel)
                        break
                    else:
                        print("Not found")
            elif choice == 3:
                print("Display all booking...")
                for hotel in Hotel_list:
                    print(hotel)
    elif Chosen == '2':
        print("you choosed Jees Hotel, thank for your booking")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Welcome to Jees hotel")
        choice = 0
        while choice != 4:
            print(rooms)
            print("1)add booking")
            print("2)looking up for booking")
            print("3)Display all booking")
            print("4)quit")
            choice = int(input("enter your choice: "))
            if choice == 1:
                print("Adding booking...")
                name = input("enter name: ")
                while name == "":
                    print("enter your name")
                    name = input("enter name: ")
                phone = input("enter phone number: ")
                while phone == "":
                    print("enter your phone number")
                    phone = input("enter phone number: ")
                date = str(input("enter date of booking (MM-DD-YY): "))
                while date == "":
                    print("enter your date of booking")
                    date = str(input("enter date of booking: "))
                b_stay = int(input("enter the period of stay: "))
                while b_stay == "":
                    print("please enter your period of stay")
                    b_stay = int(input("enter the period of stay: "))
                r_number = input("room number: ")
                while r_number not in rooms:
                    print("invalid room number")
                    r_number = input("room number: ")
                    if r_number in rooms:
                        break
                Hotel_list.append([name, phone, date, b_stay, r_number])
                b_stays.append(b_stay)
                dates.append(date)
                names.append(name)
                phones.append(phone)
                r_numbers.append(r_number)
                hotel.append([name, phone, date, b_stay, r_number])
                print(f"Thanks {name} for booking Jees Hotel\n {hotel}")
            elif choice == 2:
                print("looking up for booking...")
                keyword = input("enter name: ")
                for hotel in Hotel_list:
                    if keyword in hotel:
                        print(hotel)
                        break
                    else:
                        print("Not found")
            elif choice == 3:
                print("Display all booking...")
                for hotel in Hotel_list:
                    print(hotel)
    elif Chosen == '3':
        print("you choosed Krown Hotel, thank for your booking")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Welcome to Krown hotel")
        choice = 0
        while choice != 4:
            print(rooms)
            print("1)add booking")
            print("2)looking up for booking")
            print("3)Display all booking")
            print("4)quit")
            choice = int(input("enter your choice: "))
            if choice == 1:
                print("Adding booking...")
                name = input("enter name: ")
                while name == "":
                    print("enter your name")
                    name = input("enter name: ")
                phone = input("enter phone number: ")
                while phone == "":
                    print("enter your phone number")
                    phone = input("enter phone number: ")
                date = str(input("enter date of booking (MM-DD-YY): "))
                while date == "":
                    print("enter your date of booking")
                    date = str(input("enter date of booking: "))
                b_stay = int(input("enter the period of stay: "))
                while b_stay == "":
                    print("please enter your period of stay")
                    b_stay = int(input("enter the period of stay: "))
                r_number = input("room number: ")
                while r_number not in rooms:
                    print("invalid room number")
                    r_number = input("room number: ")
                    if r_number in rooms:
                        break
                Hotel_list.append([name, phone, date, b_stay, r_number])
                b_stays.append(b_stay)
                dates.append(date)
                names.append(name)
                phones.append(phone)
                r_numbers.append(r_number)
                hotel.append([name, phone, date, b_stay, r_number])
                print(f"Thanks {name} for booking Krown Hotel\n {hotel}")
            elif choice == 2:
                print("looking up for booking...")
                keyword = input("enter name: ")
                for hotel in Hotel_list:
                    if keyword in hotel:
                        print(hotel)
                        break
                    else:
                        print("Not found")
            elif choice == 3:
                print("Display all booking...")
                for hotel in Hotel_list:
                    print(hotel)
#choice = 0

#while choice != 4:
#     print("1)add booking")
#     print("2)looking up for booking")
#     print("3)Display all booking")
#     print("4)quit")
#    choice = int(input("enter your choice: "))
#    if choice == 1:
#        print("Adding booking...")
#        Hotel = input("enter hotel? ")
#        while Hotel not in Hotel_list:
#            print("Hotel not found, please try again")
#            Hotel = input("enter hotel? ")
#            if Hotel in Hotel_list:
#                print("Thanks for adding")
#                break
#        name = input("enter name: ")
#        phone = input("enter phone number: ")
#        r_number = input("room number: ")
#        while r_number not in rooms:
#            print("invalid room number")
#            r_number = input("room number: ")
#            if r_number in rooms:
#                break
#        Hotel_list.append([name, Hotel, phone, r_number])

#        Hotels.append(Hotel)
#        names.append(name)
#        phones.append(phone)
#        r_numbers.append(r_number)
#    elif choice == 2:
#        print("looking up for booking...")
#        keyword = input("enter name: ")
#        for hotel in Hotel_list:
#            if keyword in hotel:
#                print(hotel)
#                break
#            else:
#                print("Not found")
#    elif choice == 3:
#        print("Display all booking...")
#        print(f"{[names]},{[Hotels]},{[phones]}{[r_numbers]}")