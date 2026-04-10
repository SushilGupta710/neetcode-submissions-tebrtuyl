class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Goal:
        # For each index, we want product of all elements except itself
        # Idea:
        # answer[i] = product of elements on LEFT of i * product of elements on RIGHT of i

        n = len(nums)

        # left[i]  = product of all elements before index i
        # right[i] = product of all elements after index i
        left = [1] * n
        right = [1] * n
        result = [1] * n


        # ---------------- LEFT PASS ----------------
        # Build left array
        # left[0] = 1 because there are no elements before index 0
        # For every other index:
        # left[i] = product of all elements before i
        #         = left[i-1] * nums[i-1]

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]


        # ---------------- RIGHT PASS ----------------
        # Build right array
        # right[n-1] = 1 because there are no elements after last index
        # We move from right → left
        # right[i] = product of all elements after i
        #          = right[i+1] * nums[i+1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]


        # ---------------- FINAL RESULT ----------------
        # For each index:
        # result[i] = left[i] * right[i]
        # This gives product of all elements except nums[i]

        for i in range(n):
            result[i] = left[i] * right[i]

        return result