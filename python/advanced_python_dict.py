#### Q6.  Create a dictionary in the below format:
##
##   faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
##                                  ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
##                           'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
##                                  ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
##                                  ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
##
##   Print the first 3 key and value pairs of the dictionary
def get_dict_faculty():
    d = {}
    with open('faculty.csv') as f:
        f.readline()
        for line in f:
            l = line.split(',')
            k = l[0].rsplit(sep=' ', maxsplit=1)[1]
            if k not in d:
                d[k] = [l[1:]]
            else:
                d[k].append(l[1:])
    return(d)

get_d = get_dict_faculty()
for i in list(get_d.keys())[0:3]:
    print(i, ":", get_d[i])


## Q7.  The previous dictionary does not have the best design for keys.
##      Create a new dictionary with keys as:
##
## professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
##                   ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
##                   ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
##                   ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
##                   ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
##
##   Print the first 3 key and value pairs of the dictionary
def get_dict_professor():
    d = {}
    with open('faculty.csv') as f:
        f.readline()
        for line in f:
            l = line.split(',')
            d[tuple(l[0].strip().split())] = l[1:]
    return(d)

get_d = get_dict_professor()
for i in list(sorted(get_d.keys()))[0:3]:
    print(i, ":", get_d[i])


## Q8.  It looks like the current dictionary is printing by first name.
##      Print out the dictionary key value pairs based on alphabetical
##      orders of the last name of the professors
##
##      Print the first 3 key and value pairs of the dictionary
def get_dict_last():
    d = {}
    with open('faculty.csv') as f:
        f.readline()
        for line in f:
            l = line.split(',')
            d[tuple(l[0].strip().split())] = l[1:]
    return(d)

get_d = get_dict_last()
for i in list(get_d.keys())[0:3]:
    print(i, ":", get_d[i])
