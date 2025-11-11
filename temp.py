import sys

if len(sys.argv) == 2:
    filename = sys.argv[0]
    temp = int(sys.argv[1])
    print("User provided input:")
else:
    print("No input found!")
    temp = 0  

print("Temperature:", temp)

if temp < 15:
    print("COLD")
elif temp >= 30:
    print("NORMAL TEMPERATURE")
else:
    print("TOO HOT!")
