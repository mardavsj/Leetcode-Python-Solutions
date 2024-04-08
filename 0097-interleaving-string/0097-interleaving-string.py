class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)
        @cache
        def isInter(i1,i2,i3):
            if i1==n1 and i2==n2 and i3==n3:
                return True

            return i3<n3 and (i1<n1 and s1[i1]==s3[i3] and isInter(i1+1,i2,i3+1) or i2<n2 and s2[i2]==s3[i3] and isInter(i1,i2+1,i3+1))

        return isInter(0,0,0)    