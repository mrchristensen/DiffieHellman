# Diffie Hellman

## How to Run the Code
The values are hard coded in, so simply run ```python main.py``` to find *g^a % p* and *g^ab % p*

## Values
* The value *p* is found using openssl to find a safe prime of 512 bites (```openssl prime -safe -generate -bits 512```)
* A random int for the value *a* is found by reading from */dev/urandom* (for an int of 512 bits)
* *g* is equal to 5 (from spec)
* *g^b % p* comes from the passoff driver (https://grader.cs465.byu.edu/diffie-hellman)

The modular exponentiation is done using a handmade divide and conquer algorithm

## Version
Use Python 3.7.2