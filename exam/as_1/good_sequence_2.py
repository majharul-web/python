# Good Sequence function
def good_sequence(A):
    free_dic = {}
    for num in A:
        if num in free_dic:
            free_dic[num] += 1
        else:
            free_dic[num] = 1

    # print(free_dic)
    remove_cnt = 0

    for key in free_dic:
        cnt = free_dic[key]
        if cnt == key:
            continue
        elif cnt > key:
            remove_cnt += cnt - key
        else:
            remove_cnt += cnt

    return remove_cnt

# Get the input values
N = int(input())
A = [int(x) for x in input().split()]

# Print the result
print(good_sequence(A))
