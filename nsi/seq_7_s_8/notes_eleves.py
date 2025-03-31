import csv


data_file = open("NotesEleves.csv", encoding="utf8")
data = list(csv.DictReader(data_file, delimiter=","))
print(data)
data_file.close()

p3 = [line["Nom"] for line in data if int(line["Maths"]) > 18 and int(line["NSI"]) > 13]

p4 = [line["Nom"] for line in data if int(line["Maths"]) > 18 or int(line["NSI"]) > 13]

print(p3)
print(p4)

data_file = open("NotesEleves.csv", encoding="utf8")
table1 = list(csv.DictReader(data_file, delimiter=","))
data_file.close()

data_file = open("NotesEleves2.csv", encoding="utf8")
table2 = list(csv.DictReader(data_file, delimiter=","))
data_file.close()

table3 = table1 + table2

print(table3)

with open("NotesEleves3.csv","w") as new_file:
    objet = csv.DictWriter(new_file,['Nom','Maths','NSI','Anglais'])
    objet.writeheader()
    objet.writerows(table3)
