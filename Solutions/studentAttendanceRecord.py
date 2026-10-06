# 551. Student Attendance Record I

class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt = 0
        cnt1 = 0
        for ch in s:
            if ch == 'A':
                cnt += 1
                if cnt >= 2:
                    return False
            if ch == 'L':
                cnt1 += 1
                if cnt1 >= 3:
                    return False
            else:
                cnt1 = 0

        return True