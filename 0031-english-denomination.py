"""
http://projecteuler.net/problem=31
"""
count = 0

def generate_denominations(base, coin, limit):
    global count
    if base + coin == limit:
        count += 1
    elif base + coin > limit:
        return
    else:
        generate_denominations(base+coin, 1, limit)
        generate_denominations(base+coin, 2, limit)
        generate_denominations(base+coin, 5, limit)
        generate_denominations(base+coin, 10, limit)
        generate_denominations(base+coin, 20, limit)
        generate_denominations(base+coin, 50, limit)
        generate_denominations(base+coin, 100, limit)
        generate_denominations(base+coin, 200, limit)
        
def main():
    global count
    limit = 200
    
    generate_denominations(0, 1, limit)
    generate_denominations(0, 2, limit)
    generate_denominations(0, 5, limit)
    generate_denominations(0, 10, limit)
    generate_denominations(0, 20, limit)
    generate_denominations(0, 50, limit)
    generate_denominations(0, 100, limit)
    generate_denominations(0, 200, limit)
    
    print count
    
main()
