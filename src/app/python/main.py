import datetime

f = open("fooFile.txt", "w")
f.write("Yo it's me python\n")

# Get current date and time
current_time = datetime.datetime.now()
# Print date and time stamp
ts = "Current date and time:" + str(current_time)
f.write(ts)
f.close()
print("python script created a new file")