"""
Problem 67

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt,
a 15K text file containing a triangle with one-hundred rows.
"""
import copy
data = open("triangle.txt").read()
def traditional():
    # Initialization of data
    global data
    data = data.splitlines()
    data = [x.split() for x in data]

    # Converting string to int
    for i in range(len(data)):
        data[i] = map(int, data[i])

    # Creating a answer matrix
    ans = copy.deepcopy(data)
    
    for i in range(len(data)-1):
        # Updating current matrix with answer matrix
        data = copy.deepcopy(ans)
        for j in range(len(data[i])):
            # Computing the left child
            temp = data[i][j] + data[i+1][j]
            ans[i+1][j] = max(ans[i+1][j], temp)

            # Computing the right child
            temp = data[i][j] + data[i+1][j+1]
            ans[i+1][j+1] = max(ans[i+1][j+1], temp)

    return max(ans[-1])

print "Answer:", traditional()
