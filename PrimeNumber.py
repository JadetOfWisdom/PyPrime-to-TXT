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
f = None
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

def fillPrime():
    global f
    try:
        try:
            f = open(fp,'r')
        except FileNotFoundError:
            f = open(fp,'w')
            f.write("2\n")
            f.close()
        # end read fp

        try:
            k = open(fp,'r')
            pm = list(k)
            k.close()
            del k
            # p = pm[-1]
            p = int(pm[-1]) if ( int(pm[-1]) > int(pm[-2]) ) else int(pm[-2])
            del pm
            # print(p)
            f = open(fn, "r")
            s = f.read()
            if s == "":
                s = "1"
            if(int(s) < p):
                s = p
            num=int(s)
            del p, s

            print(f'number = {num}')
            while(1):
                num += 1
                prime_num(num)

        except FileNotFoundError:
            f = open(fn,"w")
            f.write("1\n")
            print('Written')
        #end read fn
    except KeyboardInterrupt:
        print("\nkey board interrupt.")
        if(not f.closed):
            print(f.name,"is being open, flushing file buffer (",int.from_bytes(f.buffer.readline(),'big'),")")
            f.flush()
            print("closing file")
            f.close()
        print("stop")
        # exit()

modes = [
    ('f','create/fill prime.txt'),
    ('d','create/fill prime_diff.txt')
]

while(1):
    try:
        print('\n----------------------------\nplease select operation:\n')
        for m in modes:
            print(m[0],":",m[1])
        mode = input()
        print()
        if(mode == 'f'):
            fillPrime()
        elif (mode=='d'):
            print('this mode is not ready')
        elif (mode=='x' or mode=='q'):
            print('exit')
            exit()
        else:
            print("invalid input.")
    except KeyboardInterrupt:
        print("\nto exit, please enter 'x' or 'q'\n")