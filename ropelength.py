'''
K E N N E T H  M C K R O L A

T H E  I N T E G E R  B R E A K  P R O B L E M

Take a rope of length n and cut it into 2 pieces that when multiplied together form the optimal product
of potential cut lengths
Only integer lengths are allowed


This code is entirely my own and is meant to be an algorithmic challenge
'''


def rope_cutter(rope_length):
    remaining_length = rope_length
    two_ct = 0
    three_ct = 0
    # I S  R O P E  O D D  O R  E V E N ?
    while remaining_length != 0:
        if remaining_length % 3 == 0:
            three_ct = remaining_length / 3
            remaining_length = 0
        else:
            remaining_length -= 2
            two_ct += 1
            # print(two_ct)

    product = (3**three_ct) * (2**two_ct)
    print(product)


rope_cutter(100)
