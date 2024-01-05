# 2870. Minimum Number of Operations to Make Array Empty
from typing import List
class Solution:

    def minOperations2(self, nums: List[int]) -> int:
        d={}
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        print("dict", d)

        nops=0
        for v  in d.values():
            if v%3 == 0:
                nops+=v//3
            elif v%2 ==0:
                nops+=v//2
            else:
                return -1

        return nops




    def minOperations(self, nums: List[int]) -> int:
        nums2 = self.mysort(nums)
        print("nums2", nums2)
        # return 0
        nops = 0
        fi = 0
        nskip = 0
        while True:
            # position ofthe last equal
            li = self.n_eq(nums2, fi)
            print((f"fi {fi} li {li} "))
            rem3 = (li - fi + 1) % 3
            quot3 = (li - fi + 1) // 3
            rem2 = (li - fi + 1) % 2
            quot2 = (li - fi + 1) // 2
            if rem3 == 0:
                fi += quot3 * 3
                nops += quot3
                print(f"full 3")
            elif rem2 == 0:
                fi += quot2 * 2
                nops += quot2
                print(f"full 2")
            else:
                quot32 = rem3 // 2
                rem32 = rem3 % 2
                # advance and increase ops
                nops += quot3
                nops += quot32
                print(f"quot3 {quot3} quot32 {quot32} rem3 {rem3} rem2 {rem32}")
                fi += quot3 * 3
                fi += quot3 * 2
                if rem32 != 0:
                    # skip and count
                    fi += rem32
                    nskip += rem32
            if fi >= len(nums2):
                break
        if nskip > 0:
            return -1
        else:
            return nops

    def mysort(self, nums):
        nums1 = nums[:]
        nums2 = []
        while len(nums1) > 0:
            # find min
            imin = 0
            for i in range(0, len(nums1) - 1):
                if nums1[i + 1] < nums1[imin]:
                    imin = i + 1
            # move over
            nums2.append(nums1[imin])
            # remove
            nums1.remove(nums1[imin])
        return nums2

    def n_eq(self, nums, fi):
        print(f"n_eq nums {nums} fi {fi} ")
        li = fi
        while (li < len(nums)) and nums[li] == nums[fi]:
            li += 1
        li = li - 1
        return li

s=Solution()

print(s.minOperations2([2,3,3,2,2,4,2,3,4]))
print(s.minOperations2([2,3,3,2,2,4,2,3,5,4]))
print(s.minOperations2([2,3,2,3,2,2,4,2,3,5,4]))
# print(s.minOperations([2,3,3,2,2,4,2,3,4]))
# print(s.minOperations([2,3,3,2,2,4,2,3,5,4]))
# print(s.minOperations([2,3,2,3,2,2,4,2,3,5,4]))