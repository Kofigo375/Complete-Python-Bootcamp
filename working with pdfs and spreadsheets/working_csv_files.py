import csv

# open the file
data = open("example.csv", encoding='utf-8')

# read the file
csv_data = csv.reader(data)

# reformart it into a python object list of list
dat_lines = list(csv_data)
#print(dat_lines)
print(dat_lines[0])

all_emails = []
for line in dat_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)

full_names = []
for line in dat_lines[1:]:
    full_names.append(line[1]+ ' '+line[2])

print(full_names)

file_to_output = open('to_save_file.csv', mode='w')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows((['1','2','3'],['1','2','3'],['1','2','3']))
file_to_output.close()
