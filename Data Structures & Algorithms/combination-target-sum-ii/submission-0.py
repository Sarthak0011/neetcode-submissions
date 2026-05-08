class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        ds = []

        def helper(index, target):
            if target == 0:
                res.append(ds.copy())
                return
            
            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i-1]:
                    continue
                
                if (target-candidates[i]) >= 0:
                    ds.append(candidates[i])
                    helper(i+1, target-candidates[i])
                    ds.pop()

        helper(0, target);
        return res