import math
import cProfile


def without_eratosthenes(i):
    lst_prime = [2]
    curr_count = 1
    number = 3
    while curr_count < i:
        flag = True
        for j in lst_prime:
            if number % j == 0:
                flag = False
                break
        if flag:
            curr_count += 1
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]

# 0(n+m)

def with_eratosthenes(i):
    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in  range(2, i_max)]
    len_lst = len(lst_prime)

    for number in lst_prime:
        if number != 0:
            for j in range(number, len_lst, number):
                lst_prime[j] = 0
    res_list = [x for x in lst_prime if x != 0]
    return res_list[-1]


# O(n+ln(n))

def prime_counting_function(i):
    count_of_primes = 0
    cur_number = i
    while count_of_primes <= i:
        count_of_primes = cur_number / math. log(cur_number)
        cur_number +=1
    return cur_number

time1 = cProfile.run('without_eratosthenes(5000)')
time2 = cProfile.run('with_eratosthenes(5000)')