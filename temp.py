import sys

if len(sys.argv) == 2:
    temp = float(sys.argv[1])
    print("User provided input:")
else:
    print("No input found! Using default temperature...")
    temp = 0  

print("Temperature:", temp)

if temp < 15:
    print("COLD")
elif temp >= 30:
    print("NORMAL TEMPERATURE")
else:
    print("TOO HOT!")
