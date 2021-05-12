# integer-break
The integer break algorithm: how to break any number into the largest possible product of all possible integer addends

- - - S O L U T I O N - - -
The given number, rope_length, can be broken down into the smallest possible addends, that have increasing multiplicative values, of 2 and 3.
Whatever input is given, all that need be done is check if the remaining_length is evenly divisible by 3. If it is, the power x can be set to the dividend. If the remaining_length
is not yet divisible by 3, 2 will be subtracted from remaining_length and 1 will be added to the power y.
Once remaining_length == 0, the product will be found by raising 3 to the power of x and raising 2 to the power of y, and multiplying the 2 resulting numbers together.

E.X
rope_length = 13
Rd. 1: 13(remaining_length) % 3 != 0 --> remaining_length = 13 - 2; two_count(y) = 1
Rd. 2: 11(remaining_length) % 3 != 0 --> remaining_length = 11 - 2; two_count(y) = 2
Rd. 3: 9(remaining_lenght) % 3 == 0 --> three_count(x) = remaining_length / 3 = 3; remaining_length = 0
Product: (3 ** x) * (2 ** y)
