n, m = map(int, input().split())

print("Can't win" if n % (m + 1) == 1 else "Can win")
