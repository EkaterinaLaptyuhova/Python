# Exercise 1-2
print("Hello world!")
sec = 42 * 60 + 42
print("There are ", sec, "seconds in 42 minutes and 42 seconds.")
miles = 10 / 1.61
print("There are", miles, "miles in 10 kilometers")
print(miles / sec, "is a speed mile per sec;", miles / (sec / 60), "is a speed miles per min", miles / (sec / 3600),
      "is a speed miles per hour")

# Exercise 2-2.1
pi = 3.14
r = 5  # radius of a sphere
V = (4 * pi * r ** 3) / 3
print("The volume of a sphere with radius = 5 is", V)

# Exercise 2-2.3
leave_house = 6*60+52  # in minute
easy_pace = 8*60+15  # in sec
tempo = 7*60+12  # in sec
time = easy_pace*2+tempo*3
print('I get home at ', int((leave_house + int(time / 60)) / 60), ":", int((leave_house + int(time / 60)) % 60))
