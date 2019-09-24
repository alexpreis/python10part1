def inloop(list, new_list=None):
    new_list = [temp if temp != "no data" else 0 for temp in list ]
    return new_list

print (inloop([0.0,'no data', 5, 15]))

def summmm(list, tsum=None):

    tsum = [float(temp) for temp in list]
    t = 0
    for temp in tsum:
        t=t+temp
    return t

print (summmm(['0.0','0.2', '5', '15']))


low_case =['aaaa','bbb','cccc']

for t in range (len(low_case)):
    low_case[t]=low_case[t].upper()
    print (t)


print (low_case)


def upeerargs(*args):
    upper = [temp.upper() for temp in args]

#    return upper.sort()
    return sorted(upper)

print (upeerargs('bbb','aaa','ccc'))