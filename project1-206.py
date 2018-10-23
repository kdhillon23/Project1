import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	filenew = open(file, "r")
	topline = filenew.readline()
	datalines = filenew.readlines()
	settopline = topline.split(",")
	info_list = []
	
	for line in datalines[0:]:
		newdict = {}
		values = line.split(',')
		
		newdict[settopline[0]] = values[0] #first name
		newdict[settopline[1]] = values[1] #last name
		newdict[settopline[2]] = values[2] #email
		newdict[settopline[3]] = values[3] #Class
		newdict[settopline[4]] = values[4] #date of birth
		
		if newdict not in info_list:
			info_list.append(newdict)	
	filenew.close()	
	return info_list
	
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	pass

def mySort(data,col):
	sortedlist = sorted(data, key=lambda i:i[col])
	names = []
	for name in sortedlist:
		first = name["First"]
		last = name["Last"]
		names.append(first + " " + last)

	return names[0]
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	pass


def classSizes(data):
	freshman = 0
	sophomore = 0 
	junior = 0
	senior = 0 
	
	for student in data:
		classinfo = student["Class"]
		if classinfo == "Freshman":
			freshman += 1
		elif classinfo == "Sophomore":
			sophomore += 1
		elif classinfo == "Junior":
			junior += 1
		elif classinfo == "Senior":
			senior += 1
	#adding values to a list
	histogram = []
	histogram.append(("Freshman", freshman))
	histogram.append(("Sophomore", sophomore))
	histogram.append(("Junior", junior))
	histogram.append(("Senior", senior))
	#creating a tuple

	#sorting the list of tuples
	histogram.sort(key=lambda x: x[1], reverse = True)
	return histogram# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	pass


def findMonth(a):
	months = {}
	for entry in a:
		dates = entry["DOB\n"].split("/")
		x = int(dates[0])
		if x in months:
			months[x] = months[x] + 1
		else:
			months[x] = 1

	sorted_months = sorted(months.items(), key=lambda t: t[1], reverse=True)
	print (sorted_months)
	return(sorted_months[0][0])
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	pass

def mySortPrint(a,col,fileName):
	file = open(fileName, 'w')

	data_list = sorted(a, key=lambda k: k[col])

	for col in data_list:
		first = col['First']
		last = col['Last']
		email = col['Email']
		file.write(first + ',' + last + ',' + email + '\n')

	file.close()
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
	age_count = []
	average_age = 0 
	current = date.today()
	for entry in a:
		dates = entry["DOB\n"].split("/")
		age = (current.year - int(dates[2]))
		age_count.append(age)

	print(age_count)
		#for dates in a:
	pass

# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
 
################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()