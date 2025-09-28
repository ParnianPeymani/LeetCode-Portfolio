class Solution:
    def permute(self, nums):
        final = []
        temp = []
        def backtrack(LIST):
            if not LIST:
                final.append(temp[:])
                return
            for i in range(len(LIST)):
                temp.append(LIST[i])
                backtrack(LIST[:i] + LIST[i+1:])
                temp.pop()
        backtrack(nums)
        return final