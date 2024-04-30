class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        arr = [0]*26
        for c in s:
            o = ord(c) - 97
            _max = 0
            for i in range(max(0, o-k), min(26, o+k+1)):
                _max = max(_max, arr[i]+1)
            arr[o] = _max
        return max(arr)