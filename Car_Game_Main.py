# run_game = True
# car_running = False
# while run_game == True:
#     #UI = user input
#     UI = (input('>'))
#     if UI == 'start':
#         car_running = True
#         print('Car started... Ready to go!')
#     elif UI == 'quit':
#         run_game = False
#         break
#     elif UI == 'stop':
#         if car_running == True:
#             print('Car stopped.')
#             car_running = False
#         else:
#             print('Car already stopped.')
#     elif UI == 'help':
#         print('start - to start the car\n'
#               'stop - to stop the car\n'
#               'quit - to exit\n')
#     else:
#         print('I don\'t understand that.')
#

#Revised Code
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start = to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand ")
