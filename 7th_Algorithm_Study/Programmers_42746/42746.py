def quick_sort(unsorted_list):
    quick_sort_recursive(unsorted_list, 0, len(unsorted_list)-1)


def quick_sort_recursive(unsorted_list, left, right):
    if right > left:
        pivot = left
        pivot_item = unsorted_list[left]
        for i in range(left + 1, right + 1):
            if pivot_item + unsorted_list[i] < unsorted_list[i] + pivot_item:
                unsorted_list[pivot+1], unsorted_list[i] = unsorted_list[i], unsorted_list[pivot+1]
                pivot += 1
        unsorted_list[left], unsorted_list[pivot] = unsorted_list[pivot], unsorted_list[left]
        quick_sort_recursive(unsorted_list, left, pivot-1)
        quick_sort_recursive(unsorted_list, pivot + 1, right)

def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    str_num = list(map(str, numbers))
    quick_sort(str_num)
    return ''.join(str_num)



'''
# 처음 접근했던 방식은 아래 코드와 같다.
# 하지만 밑의 코드는 이 문제에서는 통과하지만 numbers의 원소의 크기가 더 큰 경우에는 잘못된 답을 낼수도 있다.

def extend_len(s, max_len):
    if len(s) < max_len:
        s = s * (max_len // len(s) + 1)

    return s[:max_len]
def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    max_len = 4
    str_num = list(map(str, numbers))
    return ''.join(sorted(str_num, key=lambda x: extend_len(x, max_len), reverse=True))


# abc와 abcxxxyyyzzz를 비교

# abcxxxyyyzzzabc
# abcabcxxxyyyzzz

# 여기서 abc와 xxx를 비교하고 둘중 더 큰애를 가져가면 된다.
# abc와 xxx가 같은경우 xxx와 yyy를 비교하는데 xxx가 abc이므로 abc와 yyy를 비교하는 것이 된다.

# 즉 abcabcabcabc와 abcxxxyyyzzz를 비교하는 것이 된다.

# 하지만 다음과 같은 경우에는 잘못된 값이 나온다.
# max_len을 8이 아닌 9로 설정해줘야 제대로 결과가 나온다.

# abc abcxxxyy

# 321 32132132

# 321 321 321 32
# 321 321 32 321

'''