class Solution:
    def reverseString(self, s: str) -> str:
        x = 0
        y = -1
        a = list(s)
        for i in range(0, len(s)):
            if x >= y + len(s): break
            a[x], a[y] = a[y], a[x]
            x+=1
            y-=1
        return ''.join(a)
            
    def reverseWords(self, s: str) -> str:
        result = []
        for i in s.split(' '):
            if i != ' ':
                result.append(self.reverseString(i))
            
        return ' '.join(result)