#!/usr/bin/env python
# remove duplicates from a list

a_list = ["blue", "blue", "green", "red", "red", "yellow"]

def rm_dups(a_list):
    new_list = set(a_list)
    return list(new_list)

new_list = rm_dups(a_list)
# prettier: print ', '.join(new_list)
print new_list
