def almostIncreasingSequence(sequence):
   droppped = False
   # breakpoint()
   last = prev = min(sequence) - 1
   for elm in sequence:
       if elm <= last:
           if droppped:
               return False
           else:
               droppped = True
           if elm <= prev:
               prev = last
           elif elm >= prev:
               prev = last = elm
       else:
           prev, last = last, elm
   return True

print(almostIncreasingSequence([10,1,2,3,4]))




# l=[5,1,2,3]
# count=0
# for i in range(len(l)):
# l3=l[:i]+l[i+1:]
# if sorted(l3)== l3:
# count+=1
# else:
# pass
# if count != 0:
# print("Number is Strictly Increasing")
# else:
# print("List is not Strictly Increasing")


# def increasing_sequence(sequence):
# t=0
# for i in range(len(sequence)):
# temp=sequence.copy()
# del temp[i]
# if temp==sorted(temp) and not (any (i==j for i,j in zip (sorted(temp),sorted (temp[1:])))):
# t+=1
# return t>0
# print(increasing_sequence([10,1,2,3,4]))


