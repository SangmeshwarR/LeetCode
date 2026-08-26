# 461. Hamming Distance

class Solution:
    def hammingDistance(self, x, y):
        xb, yb, ans = f'{x:032b}', f'{y:032b}', 0
        return sum(i != j for i, j in zip(xb, yb))