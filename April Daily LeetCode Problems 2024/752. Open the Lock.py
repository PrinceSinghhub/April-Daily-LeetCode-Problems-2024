class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        zero_cahnce = set(["1000", "0100", "0010", "0001", "9000", "0900", "0090", "0009"])
        prohibt = set(deadends)
        if prohibt == zero_cahnce:
            return -1
        possible = set()
        start = ""
        tab = list(target)
        if "0000" in prohibt:
            return -1
        if target == "0000":
            return 0
        for i in range(4):
            val = int(tab[i])
            val1 = val - 1 if val != 0 else 9
            val2 = (val + 1) % 10
            rest = "".join(tab[i + 1:])
            target1 = start + str(val1) + rest
            target2 = start + str(val2) + rest
            if val == 0:
                if target1 not in prohibt:
                    possible.add(target1)
                if target2 not in prohibt:
                    possible.add(target2)
            else:
                if val == 1:
                    possible.add(target1)
                for item in range(1, val1 + 1):
                    if start + str(item) + rest in prohibt:
                        break
                    if item == val - 1:
                        possible.add(target1)
                if val == 9:
                    possible.add(target2)

                for item in range(9, val, -1):
                    if start + str(item) + rest in prohibt:
                        break
                    if item == val + 1:
                        possible.add(target2)
            start += tab[i]
        if not possible:
            return -1

        def helper(source, target) -> int:
            if source == target:
                return 0
            res = 0
            src = list(source)
            target = list(target)
            for i in range(4):
                val1 = int(src[i])
                val2 = int(target[i])
                if val1 < val2:
                    res += min(val2 - val1, 10 + val1 - val2)
                else:
                    res += min(val1 - val2, 10 + val2 - val1)
            return res

        minimum = float("inf")
        for item in possible:
            my_min = helper("0000", item)
            if my_min < minimum:
                minimum = my_min
        return minimum + 1


