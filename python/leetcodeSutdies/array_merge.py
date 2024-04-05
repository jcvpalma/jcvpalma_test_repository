# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing #order,
# and two integers m and n, representing the number of elements in nums1 #and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be
# stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged, and the
# last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3: Input: nums1 = [0], m = 0, nums2 = [1], n = 1 Output: [1]
# Explanation: The arrays we are merging are []
# and [1]. The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only
# there to #ensure the merge result can fit in nums1.

def array_merge(nums1, m, nums2, n):
    if m > 1 and n > 1:
        del nums1[-n:]
        nums1 = nums1 + nums2
    else:
        nums1 = [x for x in nums1 if x > 0] + nums2
    nums1.sort()
    return nums1


def array_merge2(nums1, m, nums2, n):
    if n > 1 and m > 1:
        for x in range(len(nums1) - 3, len(nums1)):
            nums1[x] = nums2[m - x]
    else:
        for x, y in enumerate(nums1):
            if y == 0:
                nums1[x] = nums2[0]
                nums2.pop(0)

    nums1.sort()
    return nums1


def array_merg3(nums1, m, nums2, n):
    #print("nums1 = {}, m = {}, nums2 = {}, n = {}".format(nums1, m, nums2, n))
    if n == 0:
        nums1 += nums2
    else:
        total_zeros_to_remove = n
        cont_remove = 0
        for zero in reversed(range(m + n)):
            # check value and delete
            #print("idx: {}, to_remove: {}".format(zero, total_zeros_to_remove))
            if nums1[zero] == 0 and cont_remove < n:
                nums1.pop(zero)
                cont_remove = cont_remove+1
            else:
                break

        #print(nums1, nums2, cont_remove)

        nums1 += nums2
        #print("after: {}".format(nums1))

    nums1.sort()

    return nums1


if __name__ == '__main__':

    test_cases = [
        {'test': 1, 'nums1': [1, 2, 3, 0, 0, 0], 'm': 3, 'nums2': [2, 5, 6], 'n': 3, 'esperado': [1, 2, 2, 3, 5, 6]},
        {'test': 2, 'nums1': [1], 'm': 1, 'nums2': [], 'n': 0, 'esperado': [1]},
        {'test': 3, 'nums1': [0], 'm': 0, 'nums2': [1], 'n': 1, 'esperado': [1]},
        {'test': 4, 'nums1': [0, 0, 3, 0, 0, 0, 0, 0, 0], 'm': 3, 'nums2': [-1, 1, 1, 1, 2, 3], 'n': 6,
         'esperado': [-1, 0, 0, 1, 1, 1, 2, 3, 3]},
        {'test': 5, 'nums1': [0, 0, 0, 0, 0], 'm': 0, 'nums2': [1, 2, 3, 4, 5], 'n': 5, 'esperado': [1, 2, 3, 4, 5]},
        {'test': 6, 'nums1': [-1, -1, 0, 0, 0, 0], 'm': 4, 'nums2': [-1, 0], 'n': 2, 'esperado': [-1, -1, -1, 0, 0, 0]},
    ]

    for tests in test_cases:
        test, nums1, m, nums2, n = tests['test'], tests['nums1'], tests['m'], tests['nums2'], tests['n']
        nums3 = array_merg3(nums1, m, nums2, n)
        print("teste: {} - Final: {} == Esperado: {} = {}".format(test, nums3, tests['esperado'],
                                                                  nums3 == tests['esperado']))
