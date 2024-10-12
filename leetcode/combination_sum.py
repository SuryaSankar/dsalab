from typing import List

class Solution:
    def already_in_combos(self, combos, new_combo):
        for combo in combos:
            if sorted(combo) == sorted(new_combo):
                return True
        return False

    def combinationSum(self, candidates: List[int], target: int, memo: dict = {}) -> List[List[int]]:
        if target in memo:
            print('memo hit')
            print(target, memo[target])
            return memo[target]
        if target == 0:
            return [[]]
        if target < 0:
            return None
        combos = []
        for candidate in candidates:
            rem = target - candidate
            rem_combos = self.combinationSum(candidates, rem, memo)
            memo[rem] = rem_combos
            if rem_combos is not None:
                for combo in rem_combos:
                    combo += [candidate]
                    if not self.already_in_combos(combos, combo):
                        combos += [combo]
        return combos
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7)) # [[7], [2, 2, 3]]
    # print(sol.combinationSum([2, 3, 5], 8)) # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    # print(sol.combinationSum([2], 1)) # []
    # print(sol.combinationSum([1], 1)) # [[1]]
    # print(sol.combinationSum([1], 2)) # [[1, 1]]
    # print(sol.combinationSum([2, 3, 6, 7], 1)) # []
    # print(sol.combinationSum([2, 3, 6, 7], 2)) # [[2]]
    # print(sol.combinationSum([2, 3, 6, 7], 3)) # [[3]]
    # print(sol.combinationSum([2, 3, 6, 7], 4)) # [[2, 2]]
    # print(sol.combinationSum([2, 3, 6, 7], 5)) # [[2, 3]]
    # print(sol.combinationSum([2, 3, 6, 7], 6)) # [[6]]
    # print(sol.combinationSum([2, 3, 6, 7], 8)) # [[2, 2, 2, 2], [2, 3, 3], [3, 5], [2, 6], [7]]
    # print(sol.combinationSum([2, 3, 6, 7], 9)) # [[2, 2, 2, 3], [3, 3, 3], [2, 2, 5], [2, 7]]
    # print(sol.combinationSum([2, 3, 6, 7], 10)) # [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [5, 5], [2, 2, 6], [3, 7]]
    # print(sol.combinationSum([2, 3, 6, 7], 11)) # [[2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [2, 2, 7], [3, 2, 6]]