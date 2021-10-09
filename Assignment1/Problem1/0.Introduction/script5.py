# Write a function

# I think it will be batter, if the CONSTRAINTS
# will be written above the def (method) because,
# if the unit test call this method with an argument 10000+
# the method will not response, but it will be executed.
def is_leap(year):
    leap = False
    if year >= 1900 and year <= 10 ** 5:
        if (year % 4 == 0):
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            leap = False
            return leap
