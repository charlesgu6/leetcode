#%%
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        med = (len(nums3)-1)/2.0
        if med == int(med):
            ans = nums3[int(med)]
        else:
            ans = (nums3[int(med)] + nums3[int(med)+1])/2.0
        return ans

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]

    sovler = Solution()
    ans = sovler.findMedianSortedArrays(nums1,nums2)
    print(ans)

#%%

#%%
