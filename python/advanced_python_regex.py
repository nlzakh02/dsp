import csv, re
## Q1. Find how many different degrees there are, and their frequencies:
##     Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
def count_degrees(csv_file_name):
    t2 = []
    with open(csv_file_name, newline='') as csvfile:
        info = list(csv.reader(csvfile))[1:]
    t = [i[1] for i in info]
    t1 = [j.strip().replace('.', '').split(' ') for j in t]
    for i in t1:
        t2.extend(i)
    return {i:t2.count(i) for i in set(t2)}

print(count_degrees('faculty.csv'))


## Q2. Find how many different titles there are, and their frequencies:
##     Ex:  Assistant Professor, Professor
def count_titles(csv_file_name):
    t = []
    with open(csv_file_name, newline='') as csvfile:
        info = list(csv.reader(csvfile))[1:]
    for g in info:
        t.extend([i.rsplit(' ', 2)[0].strip() for i in g if re.search('Biostatistics', i)])
    return {i:t.count(i) for i in set(t)}

print(count_titles('faculty.csv'))


## Q3. Search for email addresses and put them in a list.
##     Print the list of email addresses.
def emails(csv_file_name):
    mail = []
    with open(csv_file_name, newline='') as csvfile:
        info = list(csv.reader(csvfile))[1:]
    for q in info:
        mail.extend([i.strip() for i in q if re.search('@', i)])
    return(mail)

print(emails('faculty.csv'))


## Q4. Find how many different email domains there are
##    (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).
##    Print the list of unique email domains.
def unique_domains(emails):
    return set([i.split('@')[-1].strip() for i in emails])

print(unique_domains(emails('faculty.csv')))
