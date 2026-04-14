class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def checker(dis):
            count = 0
            next = position[0]

            for i in range(n):
                if position[i] >= next:
                    count += 1
                    next = position[i] + dis
            
            return count >= m

        left = 1
        right = position[-1] - position[0]

        while left <= right:
            mid = left + (right - left) // 2

            if checker(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
        