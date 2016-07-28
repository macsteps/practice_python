#!/usr/bin/env python
# goal: read from a file

if __name__=="__main__":
    counter = 0

    # ** read line by line **
    #with open('nameslist.txt', 'r') as open_file:
        #for line in open_file:
            #print line.rstrip('\n')
            #counter += 1

    #print "Total -> ", counter
    # ***********************

    # ** read entire file into var **
    #all_text = ""
    #with open('nameslist.txt', 'r') as open_file:
        #all_text = open_file.readlines()
#
    #for line in all_text:
        #print line.rstrip('\n')
        #counter += 1

    #print "Total -> ", counter
    # ***********************

    # ** read into a dictionary with count **
    star_names = {}
    with open('nameslist.txt', 'r') as open_file:
        for name in open_file:
            name = name.rstrip('\n')
            if name not in star_names:
                star_names[name] = 1
            else:
                star_names[name] += 1

        for name, count in star_names.iteritems():
            print "Name: ", name, " | Count: ", count
