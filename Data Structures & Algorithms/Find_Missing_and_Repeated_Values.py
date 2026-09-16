class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        seen = set()
        repeated = -1

        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                seen.add(num)

    
        for i in range(1, n * n + 1):
            if i not in seen:
                return[repeated, i]
        
        return []
