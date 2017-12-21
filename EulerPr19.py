''' === Problem Statement ===

How many centuries fell on the first of the month during the 20th century?
'''

# If we wanted to cheat, we could use a solution found on the forum:

# sundays = 0
# for i in range(1901,2001):
#   for j in range(1,13):
#       if datetime.date(i,j,1).weekday() == 6:
#            sundays += 1
# print(sundays)

sundaysCount = 0
currDay = 1
# Monday = 0, Sunday 6
for year in range(1901, 2001):
    for month in range(1, 12+1):
        # Month 1 - January - 31 Days
        # Month 2 - February - 28 / 29 Days
        # Month 3 - March - 31 Days
        # Month 4 - April - 30
        # Month 5 - May - 31
        # Month 6 - June - 30
        # Month 7 - July - 31
        # Month 8 - August - 31
        # Month 9 -  September - 30
        # Month 10 - October - 31
        # Month 11 - November - 30
        # Month 12 - December - 31

        # If a month has 31 days, then the 29th day will be the same as
        #  the 1st.
        # 30th day will be +1
        # 31th day will be +2
        # 1st day of next month will be +3

        # These are all the months will 31 days

        if currDay == 6:
            sundaysCount += 1

        if month == 1 or month == 3 or month == 5 or month == 7 or \
           month == 8 or month == 10 or month == 12:
            currDay += 3
            currDay %= 7
            # This makes sure that the current day is not > 6
        # These are all of the months with 30 days
        elif month == 4 or month == 6 or month == 9 or month == 1:
            currDay += 2
            currDay %= 7
        else:
            # this is February
            if year % 4 != 0:
                # if it is NOT a leap year, then the day does not change
                pass
            else:
                currDay += 1
                currDay %= 7

print(sundaysCount)
