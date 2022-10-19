# guess = 5
# input_guess = int(input("Guess: "))


# count = 2

# if input_guess != guess:
#     while count > 0:
#         input_guess = int(input("Guess: "))
#         if input_guess == guess:
#             print("You win")
#             break
#         count = count-1
# if count == 0:
#     print("Sorry, you have failed")
# else:
#     print("You win")


# secret_number = 8
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, you have failed.")


# command = ""
# count_for_start = 0
# count_for_stop = 0
# while True:
#     command = input("> ").lower()
#     if command == "start" and count_for_start == 1:
#         print("Car already started...")
#     elif command == "start":
#         print("Car started")
#         count_for_start += 1
#     elif command == "stop" and count_for_stop == 1:
#         print("Car already stopped...")
#     elif command == "stop":
#         print("Car stopped")
#         count_for_stop += 1

#     elif command == "help":
#         print("""
# start -- to start the car
# stop -- to stop the car
# quit -- to exit
#         """)
#     elif command == "quit":
#         print("I am exiting from the block...")
#         break
#     else:
#         print("I don't understand that...")
