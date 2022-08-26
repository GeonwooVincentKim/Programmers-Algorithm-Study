def solution(answers):
    answer_list = []

    max_grade = 0
    get_grade = [0] * 3

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


    # i % (the length of list)
    for i in range(0, len(answers)):
        if answers[i] == student1[i % 5]:
            get_grade[0] += 1
        if answers[i] == student2[i % 8]:
            get_grade[1] += 1
        if answers[i] == student3[i % 10]:
            get_grade[2] += 1

    max_grade = max(get_grade)

    for i in range(0, 3):
        if get_grade[i] == max_grade:
            answer_list.append(i + 1)

    return answer_list


if __name__ == "__main__":
    solution([1, 2, 3, 4, 5])
    solution([2, 1, 2, 3, 2, 4, 2, 5])
    solution([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])


# 1번 수포자가 찍는 방식 - 1, 2, 3, 4, 5, 1, 2, 3, 4, 5
# 2번 수포자가 찍는 방식 - 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5
# 3번 수포자가 찍는 방식 - 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5

# 1. 각 수포자들의 정답을 관리하는 List 3개 생성
# 2. 각 수포자들의 정답을 관리하는 각각의 List 에서 가장 큰 값을 선택
# 3. 가장 많이 맞춘 개수와 같은 플레이어를 List 에 추가
