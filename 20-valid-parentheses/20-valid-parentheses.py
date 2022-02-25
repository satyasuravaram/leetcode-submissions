class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        op = {'(':')','[':']','{':'}'}
    
        for c in s:
            if c in op:
                st.append(c)
            else:
                if st and op[st[-1]] == c:
                    st.pop()
                else:
                    return False
        
        return not st