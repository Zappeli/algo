import cProfile
from random import randint

def task_6_2(randoms):
    min_num, max_num = randoms[0], randoms[0]
    i_min, i_max = 0, 0
    for ind, elem in enumerate(randoms):
        if elem < min_num:
            i_min=ind
            min_num = elem
        if elem > max_num:
            i_max = ind
            max_num = elem
    if i_min > i_max:
        i_min, i_max = i_max, i_min
    print(sum(randoms[i_min+1:i_max]))


def task_6_2_second_v(randoms):
    i_min, i_max = min(randoms), max(randoms)
    if i_min > i_max:
        i_min, i_max = i_max, i_min
    print(sum(randoms[i_min+1:i_max]))



randoms = [randint(-10, 10) for x in range(1000000)]
time1 = cProfile.run('task_6_2(randoms)')
time2 = cProfile.run('task_6_2_second_v(randoms)')