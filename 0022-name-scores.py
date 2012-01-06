"""
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""
def the_obvious_way():
    f = open("names.txt")
    
    names = f.read()[1:-1] # eliminating the first and last "
    names = names.split('","') # a workaround to skip the csv parsing
    names.sort()
    
    # the preceding space is because we want alphabets with indices 1..26
    letters = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    sum_ = 0
    for name in names:
        ind = names.index(name) + 1 # since array indexing starts from 0
        total = sum([letters.index(x) for x in name])
        score = ind * total
        sum_ = sum_ + score
    
    return sum_
        
print "Answer by the obvious way:", the_obvious_way()
