if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    score_list = list(arr)[:n]

    max_score = max(score_list)

    # method 1
    score_set = set(score_list)
    score_set.remove(max_score)

    # method 2
    # while (max_score in score_list):
    #     score_list.remove(max_score)

    second_max = max(score_turple)

    print(second_max)
