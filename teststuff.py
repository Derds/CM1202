import csv
from collections import defaultdict

def readCSV(filename):
	with open(filename) as csvfile:
		next(csvfile)
		reader = csv.reader(csvfile)
		storedStudents = defaultdict(list)
		for row in reader:
			storedStudents[row[0]].append(row)
			mess1 = list(storedStudents.items())
		return mess1

def staffCSV(filename):
	with open(filename) as csvfile:
		next(csvfile)
		reader = csv.reader(csvfile)
		storedStaff = defaultdict(list)
		for row in reader:
			storedStaff[row[0]].append(row)
			staff1 = list(storedStaff.items())
		return staff1

readCSV("student_lists.csv")
staffCSV("staff_lists.csv")