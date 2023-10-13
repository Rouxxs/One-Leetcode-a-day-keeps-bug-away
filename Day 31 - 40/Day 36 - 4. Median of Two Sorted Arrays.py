class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        
        if len(A) > len(B):
            A, B = B, A

        half = total // 2
        l, r = 0, len(A) - 1

        while True:
            half1 = (l + r) // 2
            half2 = half - half1 - 2

            l1 = A[half1] if half1 >= 0 else float("-infinity")
            r1 = A[half1 + 1] if (half1 + 1) < len(A) else float("infinity")
            l2 = B[half2] if half2 >= 0 else float("-infinity")
            r2 = B[half2 + 1] if (half2 + 1) < len(B) else float("infinity")


            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                
            elif l1 > r2:
                r = half1 - 1
            else:
                l = half1 + 1
        return 0
            

