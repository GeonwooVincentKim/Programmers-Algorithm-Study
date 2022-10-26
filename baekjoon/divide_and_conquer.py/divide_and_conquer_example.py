import sys

"""
Divide and Conquer (분할 정복)
1. Difference between DP and Divide and Conquer
- 1. DP -> Divided problem can cause effect each other
- 2. Divide and Conquer -> Divided problem does not effect each other

2. Divide and Conquer
- 1. Should have to divide issue (or problem)
- 2. Use partial problem answer to calculate the original problem
"""

def solved(block_size, x, y):
    global result

    if x == r and y == c:
        print(result)
        sys.exit(0)

    if block_size == 1:
        result += 1
        return 

    if not (x <= r < x+block_size and y <= c < y+block_size):
        result += block_size*block_size
        return 
    
    # 분할
    nbs = block_size//2
    # 1
    solved(nbs, x, y)
    # 2
    solved(nbs, x, y+nbs)
    # 3
    solved(nbs, x+nbs, y)
    # 4
    solved(nbs, x+nbs, y+nbs)


n, r, c = map(int,input().split())

result = 0
solved(block_size=2**n, x=0, y=0)
