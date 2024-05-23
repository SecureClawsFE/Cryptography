In the first part of the code, I used the square and multiplication algorithm to evaluate exponentiation. This part is not that hard because we have done it for homework, so I have taken some guidance to be able to do this.

The second part of the code I developed the code for Euclidean algorithm (EA_GCD) and the extended version of it (EEA_GCD). I used the Extended Euclidean Algorithm to be able to find the inverse modular among the two.

I employed the Miller-Rabin Test algorithm (is_primeMillerRabin) to find if the integer generated is prime or not prime.

The generate_prime method is created to generate a sequence of random numbers to check every random number until the desired prime number is obtained.

In the last part which is the main function, I used the generate_prime function to generate two prime numbers (p,q), in which this function includes  the random.getrandbits function. Then, the rsa key generator is used to obtain the public and private key having the exponent randomly selected. At the end, I test the encryption and decryption with a plaintext number where the formulas for both are performed to obtained the results, and the to get the same plaintext value for the decryption.
