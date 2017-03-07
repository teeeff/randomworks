
a=[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2]
distance=10
b = []
master_list=[]

def perm_list(list_input):
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

def comb_list(list_to_comb):
    for tt in range(0,len(list_to_comb)):
        for tt2 in range(0,len(list_to_comb)):
            new_array=[]
            new_array=list(list_to_comb)
            if tt <> tt2:
                a=new_array[tt]
                new_array[tt]=new_array[tt2]
                new_array[tt2]=a
                if new_array not in master_list:
                    master_list.append(new_array)
                    comb_list(new_array)
                    
if __name__=="__main__":
    perm_list(a)
    for m in sorted(b):
        sum = list_sum(m)
        if sum == distance:
            #print "tuple identified:{}".format(m)
            comb_list(m)                  
        else:
            pass
    for el in master_list:
        print el