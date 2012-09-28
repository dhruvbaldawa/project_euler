"""
http://projecteuler.net/problem=31
"""
count = 0

def generate_denominations(amount, coins):
    # A successful find, add 1
    if amount == 0:
        return 1
    # An unsuccessful find, add 0
    elif amount < 0 or len(coins) < 1:
        return 0
    # Deduct the coin, and calculate and don't deduct and calculate with
    # rest of the coins
    else:
        coin, rest = coins[0], coins[1:]
        return generate_denominations(amount-coin, coins) + \
            generate_denominations(amount, rest)
           
def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    amount = 200
    print generate_denominations(amount, coins)
    
main()