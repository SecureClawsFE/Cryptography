import random

#powMod_sm is a function that implements the Square-and-
# Multiply algorithm for modular exponentiation
def powMod_sm(base, exp, n):
    exp_b = bin(exp)
    value = base
    for idx in range(3, len(exp_b)):
        value = (value ** 2)%n
        if exp_b[idx: idx+1]== '1':
            value = (value * base)%n
    return value


#EA, this function find the GCD of two number x,y

def EA_GCD(x, y):
    while y:
        x, y = y, x %y

    return x

#EEA, this one find the modular inverse of two number a, b

def EEA_GCD(a, b):
    if a == 0:
        return b, 0, 1

    gcd,x1,y1 = EEA_GCD(b % a, a)
    x = y1 - (b // a) *x1
    y = x1
    return gcd, x, y


##mod_inv computes the modular inverse of b modulo n using the Extended Euclidean Algorithm.
#If the inverse does not exist, it will print the string message.


def mod_inv(b,n):
    gcd, _, t = EEA_GCD(n, b)
    if gcd == 1:
        i = t%n

    elif gcd != 1:

        print("Inverse does not exist")

    return i

#is_primeMillerRabin uses the Miller-Rabin Primality Test to check
# if a number p is likely prime.
def is_primeMillerRabin(p):

    if p == 2 or p == 3:
        return True

    if p <= 1 or p % 2 == 0:
        return False

    p1 = p-1
    t = 18
    u= 6
    r = p1
    while r%2 == 0:
        u = u + 1
        r = r / 2

    for i in range (1, t):

        a = random.randint(2, p-2)
        z = powMod_sm(a, int(r), p)
        if z != 1 and z != p1:
            j = 1
            while j < u and z != p1:
                z = powMod_sm(z, 2, p)
                if z == 1:
                    return False

                j += 1

            if z != p1:

                return False

    return True

#generate_prime generates a random prime number with the specified number
# of bits using the Miller-Rabin primality test.

def generate_prime(bits):

    n = random.getrandbits(bits)
    n |= (1 << bits - 1) | 1

    while not is_primeMillerRabin(n):
        n = random.getrandbits(bits)
        n |= (1 << bits - 1)|1

    return n

#rsa_key_gen generates RSA public and private keys (n, e, d)
# based on two prime numbers (p and q).
def rsa_keyGen(p, q):
    n = p *q
    phi_n = (p-1) * (q-1)
    for idx in range(2, 256):
        if EA_GCD(idx, phi_n) == 1:
            e = idx
            break

    d = mod_inv(e, phi_n)
    return n, e, d

def main():

    # Generate and print two prime numbers
    p = generate_prime(40)
    q = generate_prime(40)

    while p == q:
        q = generate_prime(40)

    print("The first prime number is: ", p)
    print("The second prime number is: ", q)

    #Generate and print public and private keys
    n,e,d = rsa_keyGen(p,q)

    print("\nPublic key:")
    print("Exponent e:", e)
    print("N:", n)

    print("\nPrivate key:")
    print("Exponent d:", d)
    print("N:", n)

    #Test encryption and decryption
    msg = 875
    print("\nThe original message is: ", msg)
    #Encryption
    encrypted_message = int(powMod_sm(msg, e, n))
    print("The encrypted message is: ", encrypted_message)

    #Decryption
    decrypted_message = int(powMod_sm(encrypted_message, int(d), n))
    print("The decrypted message is: ", decrypted_message)

main()
