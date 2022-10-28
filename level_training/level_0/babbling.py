from itertools import permutations

def solution(babbling):
    count = 0

    speek = ["aya", "ye", "woo", "ma"]
    word = []

    for i in range(1, len(speek) + 1):
        for j in permutations(speek, i):
            word.append(''.join(j))
    
    for i in babbling:
        if i in word:
            count += 1

    return count


if __name__ == "__main__":
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
    print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
