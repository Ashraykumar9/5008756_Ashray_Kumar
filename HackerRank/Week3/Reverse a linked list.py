def reverse(lead):
    
    # reverse a linked list logic 
    # Ashray_kumar_5008756
    
    back = None
    data = lead
    temp1 = data
    while temp1 is not None:
        a = temp1.next
        temp1.next = back
        back = temp1
        temp1 = a
        
    lead = back
    temp = lead
    return temp
