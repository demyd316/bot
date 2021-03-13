import csv

with open('freelancer-test-csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            username = row[0]
            password = row[1]
            firstname = row[2]
            lastname = row[3]
            birthday = row[4]
            birth = birthday.split(".")
            birth_day = birth[0]
            birth_month = birth[1]
            birth_year = birth[2]

            line_count += 1
        if line_count == 1:
            break
    print(f'Processed {line_count} lines.')