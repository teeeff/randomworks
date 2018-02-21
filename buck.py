class Bucket:
    def __init__(self,index,capacity,level):
        self.my_address=self
        self.left_child=0
        self.right_child=0
        self.index=index
        self.capacity=capacity
        self.level=level
        self.water_filled=0
    
    def set_family(self,l_child,r_child,bucket_list):
        try:
            x=bucket_list[l_child]
            self.left_child=l_child
        except:
            self.left_child = -1
        try:
            x = bucket_list[r_child]
            self.right_child = right_child
        except:
            self.right_child=-1

    def display_bucket(self):
        print("Bucket Address:",self)
        print("Left Child:",self.left_child)
        print("Right Child:",self.right_child)
        print("Index",self.index)
        print("Capacity",self.capacity)
        print("Bucket Level",self.level)
        print("Water Level",self.water_filled)

    def pour_water(self,water_amount,bucket_list):
        if water_amount >= self.capacity:
            self.water_filled=self.capacity
            water_amount=water_amount-self.capacity
        else:
            self.water_filled=water_amount
            water_amount=0       
        if water_amount > 0:
            if self.left_child != -1:
                print("Spilling to Left:", water_amount/2)
                bucket_list[self.left_child].pour_water(water_amount/2,bucket_list)
            else:
                pass            
            if self.right_child != -1:
                print("Spilling to Right", water_amount/2)
                bucket_list[self.right_child].pour_water(water_amount / 2, bucket_list)
        else:
            pass
	            
if __name__=='__main__':
    print("Started")
    index_to_check=30
    water_amount=1000
    capacity_of_bucket=3
    level=1
    level_element_counter=0
    bucket_list={}
    for i in range(1,index_to_check+1):
        if level_element_counter<level:
            level_element_counter+=1
        else:
            level+=1
            level_element_counter=1
        bucket=Bucket(i,capacity_of_bucket,level)
        bucket_list[i]=bucket
     
    for key,value in bucket_list.items():
        left_child=key+value.level
        right_child=key+value.level+1
        value.set_family(left_child,right_child,bucket_list)

    bucket_list[1].pour_water(water_amount,bucket_list)
    print (bucket_list[index_to_check].water_filled)
    print ("Done")
