class Solution:
    def __merge(self, nums: List[int], low: int, mid: int, high: int) -> None:
        i = low
        j = mid+1
        temp = []

        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= high:
            temp.append(nums[j])
            j += 1
        
        k = 0
        for i in range(low, high+1):
            nums[i] = temp[k]
            k += 1

    def __mergeSort(self, nums: List[int], low: int, high: int) -> None:
        if low >= high:
            return
        
        mid = low + (high - low) // 2

        self.__mergeSort(nums, low, mid)
        self.__mergeSort(nums, mid+1, high)

        self.__merge(nums, low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.__mergeSort(nums, 0, n-1)
        return nums