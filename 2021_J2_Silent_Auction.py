n = int(input())
winner = " "
win_bid = 0

for i in range(n):
    name = input()
    bid = int(input())
    if bid > win_bid:
        winner = name
        win_bid = bid

print(winner)