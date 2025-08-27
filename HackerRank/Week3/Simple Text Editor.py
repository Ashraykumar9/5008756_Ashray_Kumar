# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    # Simple text editor logic
    # Ashray_kumar_5008756
    
    fill = []
    
    a = int(input())
    
    place = ''
    
    for k in range(a):
        inquery = input().split()
        
        temp = inquery
        
        if temp[0] == '1':
            fill.append(place)
            place = place + temp[1]
            
        elif temp[0] == '2':
            fill.append(place)
            place = place[:len(place) - int(temp[1])]
            
        elif temp[0] == '3':
            print(place[int(temp[1]) - 1])
            
        elif temp[0] == '4':
            place = fill.pop()
