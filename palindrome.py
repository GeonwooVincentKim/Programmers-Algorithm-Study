def solution(queries):
    for i in queries:
        for j in i:
            print(j)

    if queries == queries[::-1]:
        print("yes")
    else:
        print("no")
        

if __name__ == "__main__":
    solution([[2, 0], [3, 1]])
    
# 1. 