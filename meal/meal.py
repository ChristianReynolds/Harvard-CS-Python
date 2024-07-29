#ask for user input
#user input will be in the '0:00'
#calculate if the time is within the brackets of time
#return the point of day it is in


'''def get_time():
    time = input("What time is it? ")
    colon_index = time.find(':')
    time = time[0:colon_index] + time[colon_index+1:]
    if int(time)
'''
def main():
    time = convert(input("What time is it? "))
    if time >= 7.0 and time <= 8.0:
        print('breakfast time')
    elif time >= 12.00 and time <= 13.00:
        print('lunch time')
    elif time >= 18.00 and time <= 19.00:
        print('dinner time')



def convert(time):
    colon_index = time.find(':')
    hour = time[0:colon_index]
    minutes = time[colon_index+1:]
    hour = float(hour)
    minutes = float(minutes)/60
    time = hour+minutes
    return time



if __name__ == "__main__":
    main()
