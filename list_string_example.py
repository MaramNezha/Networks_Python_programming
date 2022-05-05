#Defining the subjects list
L = ['Network','Math','Programming', 'Physics','Music']
for s in L:
    #test whether the subject start with P or not
    if s.startswith('P'):
        #print the subject and its length
        print(s,end=', ')
        print(s, 'length is', len(s))