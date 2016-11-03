# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution(object):

        def findMedianSortedArrays(self, arr1, arr2):
            total = len(arr1) + len(arr2)
            is_odd = total % 2 != 0
            full_range = total / 2 if not is_odd else total / 2 + 1
            for counter in range(full_range):
                x, arr1, arr2 = self.find_next_lowest(arr1, arr2)

            if is_odd:
                return x
            else:
                y, _, _ = self.find_next_lowest(arr1, arr2)
                return (x + y) / 2.0

        def find_next_lowest(self, arr1, arr2):
            if len(arr1) == 0:
                return arr2[0], arr1, arr2[1:]
            if len(arr2) == 0:
                return arr1[0], arr1[1:], arr2

            if arr1[0] < arr2[0]:
                return arr1[0], arr1[1:], arr2
            else:
                return arr2[0], arr1, arr2[1:]

assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert Solution().findMedianSortedArrays([2], [1, 3]) == 2
assert Solution().findMedianSortedArrays([], [1, 2, 3]) == 2
assert Solution().findMedianSortedArrays([], [1, 2, 3, 4]) == 2.5
assert Solution().findMedianSortedArrays([1, 2, 3, 4], []) == 2.5
assert Solution().findMedianSortedArrays([1, 2, 3], []) == 2
assert Solution().findMedianSortedArrays([3, 4], [1, 2]) == 2.5
assert Solution().findMedianSortedArrays([1, 4], [2, 3]) == 2.5
print 'OK'
