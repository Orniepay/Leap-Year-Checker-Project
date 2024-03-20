print()
print("__||Leap Year Checker||__")
print("==========================")

def is_leap_year(year):
    """
    Determines and prints whether a given year is a leap year.

    This function assesses if a year is a leap year based on the Gregorian calendar rules:
    - A year is a leap year if it is divisible by 4.
    - If the year can be evenly divided by 100, it is NOT a leap year, unless;
    - The year is also evenly divisible by 400. Then it is a leap year.
    
    This means that years like 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 
    2300, and 2500 are not leap years.

    Parameters:
    year (int): The year to check for being a leap year.

    Returns:
    None: The function directly prints whether the year is a leap year or not.
    """
    
    if year % 4 == 0: 
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
                print()
            else: 
                print("Not Leap Year")
                print()
        else:
            print("Leap Year")
            print()
    else: 
        print("Not Leap Year")
        print()

try:
    print()
    year_input = int(input("Input a year: "))
    is_leap_year(year_input)
except ValueError:
    print()
    print("Please enter a valid year in numeric format.")
    print() 