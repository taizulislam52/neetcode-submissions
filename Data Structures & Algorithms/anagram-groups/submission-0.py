class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strSet = set()
        anagramGroup = []
        for i in range(len(strs)):
            s = strs[i]
            if s not in strSet:
                strSet.add(s)
                group = [s]
                for j in range(i+1,len(strs)):
                    t = strs[j]
                    if len(t) == len(s):
                        s_sorted = "".join(sorted(s))
                        t_sorted = "".join(sorted(t))
                        if s_sorted == t_sorted:
                            group.append(t)
                            strSet.add(t)
                
                anagramGroup.append(group)
        return anagramGroup
                




        