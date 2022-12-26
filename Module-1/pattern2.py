"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for r in range(6):
    for c in range(r):
        print(c+1,end=" ")
    print(" ")