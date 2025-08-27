# Queue using two stacks logic
# Ashray_kumar_5008756

fill = []

a = int(input())

for k in range(a):
    to = input().split()
    
    temp = to
    
    if len(temp) == 2:
        fill.append(temp[1])
    
    elif temp[0] == '2':
        fill.pop(0)
    
    else:
        print(fill[0])
