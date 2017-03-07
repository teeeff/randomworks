
import datetime

a = [1,2,3,4,5,100,-92,1000,-998,1,1,1,98,-90,23,-15]
#a = [1,2,3,4,5]
b = []


def perm_list(list_input):
    #recursion_count+=1
    #print "recursion"
    length = len(list_input)
    for i in range(0,length):
        arr=[]
        for j in range(0,length):
            if i <> j:
                arr.append(list_input[j])
        if arr not in b:
            b.append(arr)
            perm_list(arr)
        arr=[]

def list_sum(list_to_add):
    s = 0
    for i in enumerate (list_to_add):       
        s = s + i[1]
    return s
        
if __name__=="__main__":
    #recursion_count=0
    print a
    print datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    perm_list(a)
    for m in sorted(b):
        sum = list_sum (m)
        if sum == 8:
            print "tuple identified:{}".format(m)
        else:
            pass
    print datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    