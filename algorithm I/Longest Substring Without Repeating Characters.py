class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = len(set((list(s))))
        iterate = s
        print(count)
        i = 0
        while i < (len(s)-count+1):
            iterate = iterate[i:i+count]
            count1 = len(set(list(iterate)))
            if count1 == count:
                return count
            elif i==len(s)-count:
                count-=1
                i=-1
            iterate = s
            i+=1