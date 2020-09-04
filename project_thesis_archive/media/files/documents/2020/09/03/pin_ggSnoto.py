
pin = "042"

while(1):
    count = 0
    new_pin = input("Enter 3 digit code : ")

    if pin == new_pin:
        print("Welcome!!")
        break

    for index_of_pin, value_of_pin in enumerate(pin):
        for index_of_new_pin, value_of_new_pin in enumerate(new_pin):
            if value_of_pin == value_of_new_pin:
                count += 1

                if index_of_pin == index_of_new_pin:
                    place = "well placed"
                else:
                    place = "wrong placed"

    if place == "wrong placed":
        conjunction = "but"
    else:
        conjunction = "and"

    if count == 0:
        print("Nothing is correct")
    elif count == 1:
        print("{} number is correct {} {}".format(count, conjunction, place))
    else:
        print("{} numbers are correct {} {}".format(count, conjunction, place))