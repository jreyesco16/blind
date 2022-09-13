class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        q = deque([s[0]])
        m = len(q)
        
        for i in range(1, len(s)):
            while s[i] in q:
                q.popleft()
            
            q.append(s[i])
            
            m = max(m, len(q))

        return m