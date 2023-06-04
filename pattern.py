'''from operator import le


a = [4,3,7,8,6,2,1]
i=0
while(i < len(a)-1):
    swap =0
    if(a[i] > a[i+1]  and  i%2 == 0):
        swap = a[i]
        a[i]= a[i+1]
        a[i+1] = swap
    elif(a[i] < a[i+1] and i%2 ==1):
        swap = a[i+1]
        a[i+1]= a[i]
        a[i] = swap
    i =i+1

print(a)

sum= 12
size =5
cur_sum =0
for i in range(0, (size-1)):
    cur_sum = a[i]
    for j  in range(i+1, size):
        if(sum == cur_sum):
            print(f'the subarray of given sum are present at index {i} to {j}')
            break
        elif (cur_sum > sum or j == size):
            cur_sum = 0
            break
        cur_sum = cur_sum+ a[j]
        j= j+1
    i=i+1'''

a = [1,2,3,7,5]
size =5
sum = 0
count = 0
for i in range(0,size-1):
    for j in range(i+1, size):
        sum =  a[i] + a[i+1]
        if((sum == a[i+1])):
            count =count+1
            break
        j = j+1
    i =i+1

print (count)