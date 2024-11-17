import time

# Wait for user to press a key to begin the timer
input("Press Enter to start the timer...")

# Countdown timer
for i in range(10, 0, -1):
    print(i, "seconds remaining")
    time.sleep(1)

# Display message at end
print("Time's up!")