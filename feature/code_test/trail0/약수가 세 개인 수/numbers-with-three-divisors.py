start, end = map(int, input().split())

divisor_cnt:int=0
div_num_3_cnt:int=0

for i in range(start,end+1):
    for j in range(1,i+1):
        if i%j==0:
            divisor_cnt+=1
    if divisor_cnt==3:
        div_num_3_cnt+=1
    divisor_cnt=0


print(div_num_3_cnt)
    
