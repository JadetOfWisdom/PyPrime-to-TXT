# this is a simple prime factorization program
# It will read the "prime.txt" file and check if there's already calculated prime number
# The current number will be stored in number.txt
# And to add the ease of use, this will have another mode called, "prime check".
# The separator is \n.
#
# The "prime check" mode will only read up to half the maximum available RAMs.
# only the first 512 numbers will stay in RAMs throughout the whole life of the program.
# The program will write 64 numbers at a time, not including the 
import math
fn = "number.txt"
fp = "prime.txt"
#f = open(fn,"r")
def prime_num(x):
    global f,fn,fp
    is_prime = True
    f.close()
    f = open(fp,'r')
    primes = list(f)
    #i = 0
    for i in primes:
        y = int(i)
        if x % y == 0:
            is_prime = False
            break
        if y >= int(math.sqrt(x)):
            break

    if is_prime:
        print(f'prime No.{len(primes)+1} = {x}')
        f = open(fp,"a+")
        f.write(f'{x}\n')
        f.close()

    f = open(fn,'w')
    f.write(f'{x}\n')
    f.close()
# end prime_num(x)

try:
    f = open(fp,'r')
except FileNotFoundError:
    f = open(fp,'w')
    f.write("2\n")
    f.close()
# end read fp

try:
    f = open(fn, "r")
    s = f.read()
    if s == "":
        s = "1"
    num=int(s)
    print(f'number = {num}')
    while(1):
        num += 1
        prime_num(num)

except FileNotFoundError:
    f = open(fn,"w")
    f.write("1\n")
    print('Written')
#end read fn



