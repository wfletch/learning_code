class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # What's my plan.
        # Well, move through the list and when we find continuous baloons of the same color, 
        # remove the ones with the lowest cost
        # We can use two pointers to track
        left, right = 0, 1
        time = 0
        # This is the naive solution. It should not really time out.
        while right != len(colors):
            if colors[left] == colors[right]:
                # We are currently in a continuous color line
                right +=1
                continue
                # Otherwise, we are finished with our current set. Prune
            if right - left == 1:
                left = right
                right +=1
                continue
            else:
                # We are in a long stretch. let's do something cool
                candidates = neededTime[left:right]
                candidates.sort()
                # We remove the n-1 lowest
                time += sum(candidates[0:-1:1])
                left = right
                right+=1
        if right - left != 1:
            # Leftover Set
            candidates = neededTime[left:right]
            candidates.sort()
            # We remove the n-1 lowest
            time += sum(candidates[0:-1:1])
        return time

# LC # 1578
# Time: O(n)
# Space: O(n). there is a better way to keep track of time consumption without duplicating array
        