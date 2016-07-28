#!/usr/bin/env python
# goal: generate strong passwords

import random, string
length = 13
chars = string.ascii_letters + string.digits + '!@#$%^&*()'

rnd = random.SystemRandom()
print ''.join(rnd.choice(chars) for i in range(length))
