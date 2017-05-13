__author__ = 'Jozef Tenus'	# v. 20.10.2016 11:29AM
import csv
import sys
from fuzzywuzzy import fuzz
import datetime
import codecs

fname = "noemail"

print('-------------------------------')
print('WARNING: Close all related CSVs')
print()
q1 = input('Do you want to proceed? (Y/N)').lower()
if q1 == 'n': sys.exit()

timestart = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

plcharacters = ('ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'à', 'è', 'ì', 'ò',\
	'ù', 'á', 'é', 'í', 'ú', 'ý', 'â', 'ê', 'î', 'ô', 'û', 'ã', 'ñ', 'õ',\
	'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'ß', 'å')

plcharactersDICT = {\
	'ą': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'å': 'a', 'ć': 'c', 'ę': 'e', 'è': 'e', 'ł': 'l',\
	'ń': 'n', 'ó': 'o', 'ò': 'o', 'ô': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z', 'á': 'a', 'é': 'e',\
	'ê': 'e', 'ë': 'e', 'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', 'ú': 'u', 'ù': 'u', 'ü': 'u',\
	'û': 'u', 'ñ': 'n', 'ß': 's', 'ä': 'a', 'ö': 'o', 'õ': 'o', 'ý': 'y', 'ÿ': 'y'}

dictionary = {}

with codecs.open('emailDICT.csv', 'r', encoding="Latin-1") as csvfile:
	emailGENdict = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	for row in emailGENdict:
		key = row['company'].lower()
		dictionary.setdefault(key, [])
		dictionary[key].append(row['pattern'])
		dictionary[key].append(row['domain'])

		#print(dictionary[key][0])



def main():
	def colnames():
		with codecs.open(fname + '.csv', 'r', encoding="Latin-1") as csvfile:
			emaildict = csv.reader(csvfile, delimiter=',', quotechar='"')
			columnnames = list(next(emaildict))
			first_nameDICT = ['first name', 'first_name', 'imie', 'imię']
			surnameDICT = ['surname', 'last name', 'last_name', 'nazwisko']
			emailDICT = ['e-mail', 'email', 'e mail', 'mail']
			companyDICT = ['company', 'firma', 'organisation']
			primarykeyDICT = ['key', 'id', 'primary_key', 'primary key' 'no', 'ref', 'reference', 'number', 'url']
			tempcol = []
			columnnamesREQ = []
			columnnamesOPN = []
			for i in columnnames:
				if i.lower() in first_nameDICT:
					first_name = i
					tempcol.append(i)
				elif i.lower() in surnameDICT:
					surname = i
					tempcol.append(i)
				elif i.lower() in emailDICT:
					email = i
					tempcol.append(i)
				elif i.lower() in companyDICT:
					company = i
					tempcol.append(i)
				elif i.lower() in primarykeyDICT:
					primary_key = i
					tempcol.append(i)
			
			if len(tempcol) == 5:
				columnnamesREQ = [first_name, surname, email, company, primary_key]
				for i in columnnames:
					if i not in columnnamesREQ: columnnamesOPN.append(i)
			elif len(tempcol) != 5:
				print('Error: Check names of the columns')
		
		columnnames = []
		for i in columnnamesREQ: columnnames.append(i)						# popracuj nad kolumnami!!!!!!!!!!!!!!!!!!!!
		for i in columnnamesOPN: columnnames.append(i)
		
		# print(columnnames)
		return columnnames

	first_name = colnames()[0]
	surname = colnames()[1]
	email = colnames()[2]
	company = colnames()[3]
	primary_key = colnames()[4]
	emailslist = []
	emailslistGG = []
	
	with codecs.open(fname + '.csv', 'r', encoding="Latin-1") as csvfile:
		emaildict = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		
		cntr = 0
		cntrpercent = 0
		for i in emaildict:
			cntrpercent +=1
		print('Number of records: ' + str(cntrpercent))
	
	emailcntr = 0
	countercheck = []

	with codecs.open(fname + '.csv', 'r', encoding="Latin-1") as csvfile:
		emaildict = csv.DictReader(csvfile, delimiter=',', quotechar='"')	
		for row in emaildict:
			xglineFN = row[first_name]
			xglineSU = row[surname]
			xglineEM = row[email]
			xglineCO = row[company]
			xglinePK = row[primary_key]
			contact = xglineFN + xglineSU
			xglineEMlen = len(xglineEM)

			xglineFN_org = xglineFN
			xglineSU_org = xglineSU

			if any(i in plcharacters for i in xglineFN):
			
				for i in xglineFN:
					if i in plcharacters:
						xglineFN = xglineFN.replace(i, plcharactersDICT[i])

			if any(i in plcharacters for i in xglineSU):
			
				for i in xglineSU:
					if i in plcharacters:
						xglineSU = xglineSU.replace(i, plcharactersDICT[i])


			#for itemGG in dictionary:
				
				#print('dict: ' + itemGG.lower())
				#print('file: ' + xglineCO.lower())
			linecheck = []

				#ratio = fuzz.ratio(xglineCO.lower(), itemGG.lower())

				#if ratio >= 90:
			if xglineCO.lower() in dictionary:

				if dictionary[xglineCO.lower()][0] == 'fsurname':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineFN[0].lower() + xglineSU.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'surname':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineSU.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'first_name':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineFN.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'first_name.surname':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineFN.lower() + '.' + xglineSU.lower() + "@" + dictionary[xglineCO.lower()][1]])

				elif dictionary[xglineCO.lower()][0] == 'first_name-surname':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineFN.lower() + '-' + xglineSU.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'surname-first_name':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineSU.lower() + '-' + xglineFN.lower() + "@" + dictionary[xglineCO.lower()][1]])

				elif dictionary[xglineCO.lower()][0] == 'first_name_surname':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineFN.lower() + '_' + xglineSU.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'first_namesurname':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineFN.lower() + xglineSU.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'f.surname':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineFN[0].lower() + '.' + xglineSU.lower() + "@" + dictionary[xglineCO.lower()][1]])


				elif dictionary[xglineCO.lower()][0] == 'surnamefirst_name':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineSU.lower() + xglineFN.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'surname.first_name':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineSU.lower() + '.' + xglineFN.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'surname_first_name':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineSU.lower() + '_' + xglineFN.lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'surname_f':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineSU.lower() + '_' + xglineFN[0].lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'surnamef':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineSU.lower() + xglineFN[0].lower() + "@" + dictionary[xglineCO.lower()][1]])
				elif dictionary[xglineCO.lower()][0] == 'first_names':
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO, xglineFN.lower() + xglineSU[0].lower() + "@" + dictionary[xglineCO.lower()][1]])		
				
				linecheck.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO])
				emailcntr +=1
				# break

				if [xglinePK, xglineFN_org, xglineSU_org, xglineCO] not in linecheck:
					emailslistGG.append([xglinePK, xglineFN_org, xglineSU_org, xglineCO])

			cntr +=1

			if round((cntr/cntrpercent), 2) > 0.05 and '5' not in countercheck:
				timeinterw = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				# print('Progress: 5% (' + str(timeinterw-timestart) + ')')
				print('Progress: 5%')
				countercheck.append('5')
			if round((cntr/cntrpercent), 2) > 0.25 and '25' not in countercheck:
				timeinterw = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				# print('Progress: 25% (' + str(timeinterw-timestart) + ')')
				print('Progress: 25%')
				countercheck.append('25')
			if round((cntr/cntrpercent), 2) > 0.50 and '50' not in countercheck:
				timeinterw = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				# print('Progress: 50% (' + str(timeinterw-timestart) + ')')
				print('Progress: 50%')
				countercheck.append('50')
			if round((cntr/cntrpercent), 2) > 0.75 and '75' not in countercheck:
				timeinterw = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				# print('Progress: 75% (' + str(timeinterw-timestart) + ')')
				print('Progress: 75%')
				countercheck.append('75')
			if round((cntr/cntrpercent), 2) > 0.95 and '95' not in countercheck:
				timeinterw = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				# print('Progress: 95% (' + str(timeinterw-timestart) + ')')
				print('Progress: 95%')
				countercheck.append('95')
			if round((cntr/cntrpercent), 2) == 1.00 and '100' not in countercheck:
				timeinterw = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				# print('Progress: 100% (' + str(timeinterw-timestart) + ')')
				print('Progress: 100%')
				countercheck.append('100')

	timestopdone = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
	
	with codecs.open(fname + '_done_' + str(timestopdone) + '.csv', 'w', encoding="Latin-1") as EMfile:
		writer = csv.writer(EMfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		emailslistGG_fr = ['Primary Key', 'First Name', 'Surname', 'Company', 'Email']
		writer.writerow(emailslistGG_fr)
		
		for i in emailslistGG:
			writer.writerow(i)
			
	timestop = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	# print('Emails created: ' + str(emailcntr) + ' (' + str(round((emailcntr/cntrpercent), 2)*100) + '%) in ' + str(timestop-timestart))
	print('Emails created: ' + str(emailcntr) + ' (' + str(round((emailcntr/cntrpercent), 2)*100) + '%)')
if __name__ == "__main__": main()
