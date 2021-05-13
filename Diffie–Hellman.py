from random import randint 
print("PRATYUSH AVI A203")
if __name__ == '__main__':
 
    P = int(input('Enter prime P: '))
    G = int(input('Enter prime G: '))
     
    print('The Value of P is :%d'%(P))
    print('The Value of G is :%d'%(G))
      
    a = int(input('Enter Secret Key for Alice: '))
    print('The Secret Key a for Alice is :%d'%(a)) 
    x = int(pow(G,a,P))  
    b = int(input('Enter Secret Key for Bob: '))
    print('The Secret Key b for Bob is :%d'%(b))
    
    y = int(pow(G,b,P))  
    ka = int(pow(y,a,P))
    kb = int(pow(x,b,P))

    print('Secret key for the Alice is : %d'%(ka))
    print('Secret Key for the Bob is : %d'%(kb))