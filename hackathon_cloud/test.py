import time
def powReduce(c,pw,n):
    
    for j in range(1,pw):
        print "------",c,"------"
        if(pow(c,j) < n ):
            print "asdasd",j
            continue
        else:
            power = int(pw/j)
            rem = int(pw%j)
            print power,rem,j
            time.sleep(2)
            return ((powReduce(c**j,power,n) % n) * ((c**rem) % n))%n
        
    
    return c
    
c = [1,2,3,4]
n = 9
pk = 1
s = 4
pw = 20
rem = 0
x = powReduce(212,pw,n)
print "-------",x    
        
            
        
