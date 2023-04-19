# pincode variables
pincode = "1234"
supplied_pin = None

# failed_attempts variable
failed_attempts = 0

# loop while supplied_pin is not equal to the hardcoded pincode
while supplied_pin != pincode:
    # read pin input from terminal
    supplied_pin = input("Please enter your pin: ")
    # check whether input is numeric
    if supplied_pin.isdecimal():

        # if the supplied pin does not match increment the failed attempts variable by 1
        if supplied_pin != pincode:
            failed_attempts += 1

        # nested if - if the failed attempts variable is now 3 print "Locked out" and exit loop
#       # else if failed attempts is still < 3 run the loop again and print the number of failed attempts
        if failed_attempts == 3:
            print("OOPS! You are locked out!")
            break
        else:
            print("Incorrect attempt number: ", failed_attempts)

    # if the pin entered matches the pin hardcoded above then print well done and break the loop
    else:
        print("WELL DONE")
        break


# give the user a limited number of times to try and input their PIN correctly
# increment in range goes up 1 , 2, 3
# second number - first number in this case
for i in range(1, 4):

    # read in the user input
    supplied_pin = input("Please enter your pin: ")

    # if the supplied pin matches print "well done" and exit loop
    # else print incorrect attempt number and carry on
    if supplied_pin == pincode:
        print("WELL DONE")
        break
    else:
        print("Incorrect attempt number: ", i)

    # if this is the third time the loop has run without breaking (exiting)
    # user must have got it wrong 3 times. print "locked out" and break.
    if i == 3:
        print("OOPS! You are locked out!")