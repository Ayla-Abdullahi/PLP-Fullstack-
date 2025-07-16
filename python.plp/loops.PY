from time import sleep # Importing sleep function from time module

# #for loop
for i in range(10):
     print(str(i) + "\n")


#     #while loop

countdown=10
while countdown > 0:
    print("take off in", countdown)
    countdown -= 1
    sleep(1)  # Sleep for 1 second to simulate a countdown
