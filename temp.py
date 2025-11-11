import sys
if len(sys.argv) ==1;
filename = sys.argv[0]
temp=(sys.argv[1])
print("user provided input:")
else:
print("no input found !")
print("Temperature=:",temp)
if (temp<15){
  print("COLD")
}
elif (temp>=30){
  print("NORMAL TEMPERATURE")
}
else:
print("TOO HOT !")
