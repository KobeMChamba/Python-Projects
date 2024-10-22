class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to apply binary search on it
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            # Partition nums1 and nums2
            partition1 = (low + high) // 2
            print("partition1: ", partition1)
            partition2 = (m + n + 1) // 2 - partition1
            print("partition2: ", partition2)
            
            # Left and right parts of nums1
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            print("max_left1: ", max_left1)
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            print("min_right1: ", min_right1)
            
            # Left and right parts of nums2
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            print("max_left2: ", max_left2)
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            print("min_right2: ", min_right2)
            
            # Check if the partition is correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                print("if")
                # If the total number of elements is odd
                if (m + n) % 2 == 1:
                    return max(max_left1, max_left2)
                # If the total number of elements is even
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                print("elif")
                high = partition1 - 1  # Move the partition in nums1 to the left
            else:
                print("else")
                low = partition1 + 1  # Move the partition in nums1 to the right

        raise ValueError("Input arrays are not sorted.")
