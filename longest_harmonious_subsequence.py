from collections import Counter

def findLHS(nums):
    cnt = Counter(nums)
    return max((cnt[k] + cnt[k+1] for k in cnt if k+1 in cnt), default=0)