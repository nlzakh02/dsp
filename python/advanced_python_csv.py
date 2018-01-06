## Q5.  Write email addresses from Part I to csv file
## Your file, emails.csv, will look like this:
##  ```
##  bellamys@mail.med.upenn.edu
##  warren@upenn.edu
##  bryanma@upenn.edu
##  ```
import csv, re

def emails(csv_file_name):
    mail = []
    with open(csv_file_name, newline='') as csvfile:
        info = list(csv.reader(csvfile))[1:]

    for q in info:
        mail.extend([i.strip() for i in q if re.search('@', i)])

    return(mail)


def write_to_csv(list_of_emails):
    with open('emails.csv', 'w', newline='') as csvfile:
        fieldnames = ['Faculty_E-mails']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in list_of_emails:
            writer.writerow({'Faculty_E-mails': i})

m = emails('faculty.csv')
write_to_csv(m)
