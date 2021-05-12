#!/usr/bin/env python3
import csv

FILE_DIR = "./lab27_outputFile/csv_users.txt"

with open(FILE_DIR, 'r') as csv_file:
    index = 0
    for row in csv.reader(csv_file):
            print(row)
            index += 1
            newFile = f'./lab27_outputFile/admin.rc{index}'
            with open(newFile, 'w') as rcfile:
                print("export OS_AUTH_URL=" + row[0], file=rcfile)
                print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
                print("export OS_USERNAME=" + row[3], file=rcfile)
                print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
                print("export OS_PASSWORD=" + row[5], file=rcfile)
                print(rcfile.__dir__)
                rcfile.close()
    csv_file.close()

