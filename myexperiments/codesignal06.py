# 6.Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
# each statue having an non-negative integer size. Since he likes to make things perfect,
# he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1.
# He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

def makeArrayConsecutive2(statues):
   s=statues
   n=0
   for i in range(min(s),max(s)):
       if i not in s:
           n=n+1
   return n