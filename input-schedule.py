f=open('scheduler.txt','w')
#print('Enter the names of the processes that needs to be blacklisted (Enter to give and input \'q\' to quit')

working_window=int(input('Enter Working time(hrs):'))
scheduled_break=int(input('Enter Scheduled break(min):'))

f.write(str(working_window))
f.write('\n')
f.write(str(scheduled_break))
f.close()

print('Your Schedules are fixed... You\'ll get a Working Window of',working_window,'hours with a scheduled break of',scheduled_break,'minutes')

