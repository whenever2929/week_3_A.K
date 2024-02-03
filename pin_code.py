# This is Abiola





var = input("please enter your pin:")
def correct_pin():
    correct_pin= "1234"

    max_attempts = 2
    attempts = 0

    user_input = input()
    while attempts < max_attempts:

        if user_input == correct_pin:
            print("correct pin")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            var = input("please enter correct pin:")
            print("incorrect pin you have",remaining_attempts,"attempt remaining")




correct_pin()
print("end of function")





