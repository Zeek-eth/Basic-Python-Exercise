#Convert Minutes into hours,minutes and seconds
#Give Minutes
time = input("Give minutes:\n")
time = int(time)
#Calculate hours
hours = time //60
#Calculate minutes and print
minutes = time - hours*60
print(f"{hours}h {minutes}min")