#2
import random

#Implement a primality test, e.g. the Fermat
#primality test or the Miller-Rabin primality test. Use it to find a prime number
#p with exactly d bits, where:

d1 = 500
d2 = 671
d3 = 1024

#Returns true if n is prime with high probability using Fermats theorem
def checkIfPrime(number, k):
     
    # First we check some special corner cases
    if number == 2 or number == 3: return True
    elif number == 1 or number == 4: return False
     
    else:
        for _ in range(k):
            #Choose random number between 2 -> n-2
            random_number = random.randint(2, number - 2)
             
            #Fermats primality test
            if pow(random_number, number - 1, number) != 1:
                return False      
    return True

#Find prime number of bitlength d 
def primalityTest(d):

    #Choose domain for testing
    lower = 2**(d-1)
    upper = (2**d)-1
    #Loop over the ranges we are interested in
    for i in range(lower, upper):
        #checkIfPrime return true if i is a prime with high probability
        if(checkIfPrime(i,100)):
            #Print our result
            print(f"Prime number with bit-length {i.bit_length()}:")
            print(str(i) + "\n" )
            break

#Find prime numbers of the given bit-length using Fermats primality test
primalityTest(d1)
primalityTest(d2)
primalityTest(d3)

#From our code we find 3 numbers with the given bit lengths 500, 671 and 1024:
num1 = 1636695303948070935006594848413799576108321023021532394741645684048066898202337277441635046162952078575443342063780035504608628272942696526664263794849
#bit length 500

num2 = 4898883310657342436947850401401639604522231782621865961233415550616320366316550245614411808808882209683752589725123921141977824503727074585042721378292777435812376133285876920625254286345394996247527433
#bit length 671

num3 = 89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270413618581675255342293149119973622969239858152417678164812112069763
#bit length 1024