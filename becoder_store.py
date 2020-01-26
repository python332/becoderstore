#clotbing store becoder
print '''
1 >>> cheap price
2 >>> Average price
3 >>> Expensive
'''
becoder = raw_input ("becoder >> " )
if becoder == '1':
    print '''
        A > Egyptian jeans 
        B > Syrian jeans
        C > Egyptian shirt
        D > Syrian shirt
    '''
    becoder = raw_input ('Choose the number you want')
    if becoder == 'A':
        print '20 $'
    elif becoder == 'B':
        print '15 $'
    elif becoder == 'C':
        print '25 $'
    elif becoder == 'D':
        print '30 $'
if becoder == '2':
    
    print '''
        1 > German jeans
        2 > Turkish jeans
        3 > German shirt
        4 > Turkish shirt
        '''
    becoder = raw_input ('Choose the number you want >> ' )
    if becoder == '1':
        print '50 $'
    elif becoder == '2':
        print '60 $'
    elif becoder == '3':
        print '40 $'
    elif becoder == '4':
        print '45 $'
if becoder == '3' :
  
    print '''
        1 > Lebanese jeans
        2 > Japanese jeans 
        3 > American jeans
        
'''
    becoder = raw_input ('Choose the number you want')
    if becoder == '1' :
         print ('75 $')
    elif becoder == '2':
         print ' 85 $ '
    elif becoder == '3':
         print '120 $'
    
