"""
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
# Lookup table for units place
lookup_units = {
    "0": 0, #nothing
    "1": 3, #one
    "2": 3, #two
    "3": 5, #three
    "4": 4, #four
    "5": 4, #five
    "6": 3, #six
    "7": 5, #seven
    "8": 5, #eight
    "9": 4, #nine
    "11": 6, #eleven
    "12": 6, #twelve
    "13": 8, #thirteen
    "14": 8, #fourteen
    "15": 7, #fifteen
    "16": 7, #sixteen
    "17": 9, #seventeen
    "18": 8, #eighteen
    "19": 8, #nineteen
}

lookup_tens = {
    "0": 0, #adds nothing
    "1": 3, #ten
    "2": 6, #twenty
    "3": 6, #thirty
    "4": 5, #forty
    "5": 5, #fifty
    "6": 5, #sixty
    "7": 7, #seventy
    "8": 6, #eighty
    "9": 6, #ninety
}

def sum_of_words(number):
    str_ = str(number)
    # Initialize the sum
    sum_ = 0
    # A flag for checking the tens digit (redundant)
    tens_flag = False
    
    # Checking the last two digits
    if str_[-2:] in lookup_units:
        tens_flag = True
        sum_ = sum_ + lookup_units[str_[-2:]]
    
    # Checking the last one digit 
    elif str_[-1] in lookup_units:
        sum_ = sum_ + lookup_units[str_[-1]]
        # Checking the second-last digit
        if str_[-2] in lookup_tens:
            tens_flag = True
            sum_ = sum_ + lookup_tens[str_[-2]]
        
        else:
            print "Error at ten's position for number:", number
            raise Exception
    
    else:
        print "Error at unit's position for number:", number
        raise Exception
    
    # For hundreds
    if len(str_) == 3:
        sum_ = sum_ + 7 #hundred
    
        if tens_flag:
            sum_ = sum_ + 3 #and
    
        if str_[-3] in lookup_units:
            sum_ = sum_ + lookup_units[str_[-3]]
    
        else:
            print "Error at hundred's position for number:", number
    
    # For thousands
    if len(str_) == 4:
        sum_ = sum_ + lookup_units[str_[-4]]
        sum_ = sum_ + 8 # thousand
        sum_ = sum_ + 3 # for the cutting off after this structure
    
    # For numbers like one hundred, removing the "and" component
    if str_[-2:] == "00":
        sum_ = sum_ - 3
    
    return sum_
        

def traditional():
    start = 1
    end = 1000
    sum_ = 0
    
    for i in range(start, end + 1):
        sum_ = sum_ + sum_of_words(i)
    return sum_

print "Answer by traditional method:", traditional()
