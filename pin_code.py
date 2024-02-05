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

# katy
pin = '1234'
# defined the initial number of attempts as an integer which can be used to calculate number of attempts
# attempts = 1 - removed as used in range
# defined the count in order to iterate over attempts.
# add 1 to attempts value each time pin entered correctly
# count = 1 removed as used in range
# defined maximum number of time user can enter pin - value integer assigned to variable
max_num_attempts = 3

# used while loop to allow for the prompt to enter pin to run until either
# max number of attempts reacher or pin entered correctly
#
for attempts in range(1, 4):
    # while attempts < 3: removed as used in range
    # supplied_pin = getpass.getpass('Enter your pin: ')
    # input uses the prompt within the function and returns the input of the user as a string
    supplied_pin = input('Enter your pin: ')
    print(supplied_pin)

    # conditional statement
    # if pin given by user equals value of pin stored in variable below if code runs
    # statement returns true
    if supplied_pin in pin:
        print('Have lots of money')
        # added the break to stop the loop continuing to ask for pin
        break
    elif supplied_pin not in pin and attempts < 3:
        # chaining comparison - add value of count to value of attempts
        # attempts += count
        # assign value of attempts to new variable
        # total_attempts = attempts
        # output argument attempts
        print(attempts)
        # print(total_attempts)
        remaining_attempts = max_num_attempts - attempts
        print('Your pin is incorrect, you have ' + str(remaining_attempts) + ' left.')
        # if none of above statements return true, code will run
    else:
        print('Your account is now locked. Have a nice day!')
        # ends loop and stops pin being asked for
        break








