import sys
import os
import uuid
import pendulum
import string
import random


def get_utc_timestamp():
    return pendulum.now('UTC')
# end


def display_message(message):
    print('{} {}'.format(get_utc_timestamp(), message))
# end


def main():
    display_message('Starting...')

    P = [x for x in string.punctuation]
    L = [x for x in string.ascii_lowercase]
    U = [x for x in string.ascii_uppercase]
    D = [x for x in string.digits]

    # print(P)
    # print(L)
    # print(U)
    # print(D)

    P_sampled = random.sample(P, 4)
    L_sampled = random.sample(L, 4)
    U_sampled = random.sample(U, 4)
    D_sampled = random.sample(D, 4)

    pw_list = P_sampled + L_sampled + U_sampled + D_sampled

    # print(pw_list)

    random.shuffle(pw_list)

    # print(pw_list)

    password = ''.join(pw_list)
    print(password)


    display_message('Done.')
# end


if __name__ == '__main__':
    main()
