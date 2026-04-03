class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            
            days_needed = 1
            current_load = 0
            for weight in weights:
                if current_load + weight > mid:
                    days_needed += 1
                    current_load = 0
                current_load += weight
            
            if days_needed <= days:
                hi = mid
            else:
                lo = mid + 1

        return lo