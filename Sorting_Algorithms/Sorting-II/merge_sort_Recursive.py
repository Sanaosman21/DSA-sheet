class Solution:

    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        # Merge the two sorted halves
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Copy remaining elements from left half
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Copy remaining elements from right half
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy back to original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def merge_sort(self, arr, low, high):
        if low >= high:
            return

        mid = (low + high) // 2

        self.merge_sort(arr, low, mid)
        self.merge_sort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)


# Driver Code
arr = [5, 2, 8, 4, 1]

sol = Solution()
sol.merge_sort(arr, 0, len(arr) - 1)

print(arr)