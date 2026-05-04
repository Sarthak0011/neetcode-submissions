class TimeMap:

    def __init__(self):
        self.mpp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mpp:
            self.mpp[key] = []
        self.mpp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.mpp:
            return res
        values = self.mpp[key]
        low = 0
        high = len(values) - 1

        while low <= high:
            mid = (low + high) // 2
            curr_value, curr_timestamp = values[mid]

            if curr_timestamp == timestamp:
                return curr_value
            elif curr_timestamp < timestamp:
                res = curr_value
                low = mid + 1
            else:
                high = mid - 1
        return res
