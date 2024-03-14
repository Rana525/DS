accounts = [[1, 2], [3, 2],[7,3]]

def maximumWealth(accounts):
    ans = 0  # Initialize ans to 0
    for person in accounts:
        sums = sum(person)  # Calculate the wealth of each person
        if sums > ans:
            ans = sums
    return ans

print(maximumWealth(accounts))

