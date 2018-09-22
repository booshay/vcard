import csv

with open('contacts.vcf', mode='w') as header:
    header.write("BEGIN:VCARD\nVERSION:3.0\nN:;SPAM;;;\nFN: SPAM\n")

for x in range(0, 10000):
    with open('contacts.vcf', mode='a') as contact:
        contact_writer = csv.writer(contact, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if len(str(x))==1:
            contact_writer.writerow(['TEL;TYPE=OTHER;TYPE=VOICE:(508) 479-000'+str(x)])
        if len(str(x))==2:
            contact_writer.writerow(['TEL;TYPE=OTHER;TYPE=VOICE:(508) 479-00'+str(x)])
        if len(str(x))==3:
            contact_writer.writerow(['TEL;TYPE=OTHER;TYPE=VOICE:(508) 479-0'+str(x)])
        if len(str(x))==4:
            contact_writer.writerow(['TEL;TYPE=OTHER;TYPE=VOICE:(508) 479-'+str(x)])
            
            
with open('contacts.vcf', mode='a') as footer:
    footer.write("PRODID:-//Apple Inc.//iCloud Web Address Book 1817B12//EN\nREV:2018-09-19T16:48:22Z\nEND:VCARD\n")
        



