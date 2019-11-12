def d2i(delta,r):
            """
            Calculate the isotope masses from bulk mass and delta value.
            Arguments are m = mass, d= delta value, r = abundance ratio 
            element
            """

            if isinstance(delta,list):
                        i = 0
                        li = []
                        hi = []
                        for e in delta:
                             d = delta[i]
                             li.append(1000 / ((d + 1000) * r + 1000))
                             hi.append(((d + 1000) * r) / ((d + 1000) * r + 1000))
            else:
                        d = delta
                        li = 1000 / ((d + 1000) * r + 1000)
                        hi = ((d + 1000) * r) / ((d + 1000) * r + 1000)
                        
            return li, hi

d=[21.77, 22, 23 ,12]

s32, s34 = d2i(d,R)
print(s32)
print(s34)
s32[2] = 0
