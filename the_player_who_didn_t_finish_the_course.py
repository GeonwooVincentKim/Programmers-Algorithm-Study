def solution(participant, completion):
    a = sorted(participant)
    b = sorted(completion)

    for i in range(len(b)):
        if (a[i] != b[i]):
            return a[i]
    
    return a[len(a) - 1]


if __name__ == "__main__":
    solution(["leo", "kiki", "eden"], ["eden", "kiki"])
    solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])


"""
1. Compare to participant List and completion list
- 1. Sort the sequence of List element
- 2. Find the difference between two List

2. Compare to participant List and completion list, but check the number of specific User Number
- 1. Sort teh sequence of List element
- 2. Find the difference between two List
- 3. Count the number of specific element
  = If the number of specific element between two List does not same, return it
"""