import csv
import sys

args = sys.argv[1:]

if len(args) < 2:
    print("This converter requires both input and output csv file paths")

bitwarden = open(args[0],'r', encoding='utf-8-sig')
bitcsv = csv.DictReader(bitwarden)

chrome = open(args[1],'w',encoding='utf-8-sig',newline='')
chromecsv = csv.DictWriter(chrome, ['name','url','username','password'])
chromecsv.writeheader()

for row in bitcsv:
    chromecsv.writerow({'name':row['name'], 'url':row['login_uri'], 'username':row['login_username'], 'password':row['login_password']})

bitwarden.close()
chrome.close()

print("complete")