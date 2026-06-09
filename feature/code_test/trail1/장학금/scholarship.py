mid_test,final_test=map(int,input().split())

if mid_test<90:
    print(0)
elif 95<=final_test<=100:
    print(100000)
elif 90<=final_test:
    print(50000)
else:
    print(0)