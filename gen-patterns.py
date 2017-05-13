__author__ = 'Jozef Tenus'  # v. 10.04.2016 10:20PM
import csv
import datetime
import codecs

fname = "listfile"

timestart = datetime.datetime.now()

plcharacters = ('ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', '(', ')', '©', '?')
plcharactersDICT = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z', '(': '', ')': '', '©': '', '?': ''}

def main():
	def colnames():
		with codecs.open(fname + '.csv', 'r', 'UTF-8') as csvfile:
		#with open(fname + '.csv', newline='\n') as csvfile:
			emaildict = csv.reader(csvfile, delimiter=',', quotechar='"')
			columnnames = list(next(emaildict))
			first_nameDICT = ['firstname', 'first name', 'first_name', 'imie', 'imię']
			surnameDICT = ['surname', 'last name', 'last_name', 'nazwisko']
			emailDICT = ['e-mail', 'email', 'e mail']
			companyDICT = ['company', 'firma']
			tempcol = []
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
			
			if len(tempcol) == 4:
				columnnames = [first_name, surname, email, company]
			elif len(tempcol) != 4:
				print('Error: Check column names')
		return columnnames
	

	first_name = colnames()[0]
	surname = colnames()[1]
	email = colnames()[2]
	company = colnames()[3]
	emailslist = []
	EMerrorfile = []



	# with open(fname + '.csv', newline='\n') as csvfile:
	with codecs.open(fname + '.csv', 'r', 'UTF-8') as csvfile:
		emaildict = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		
		cntr = 0
		cntrpercent = 0
		for i in emaildict:
			cntrpercent +=1
		print('Number of records: ' + str(cntrpercent))
	
	emailcntr = 0
	emailcntr_uniq = 0
	countercheck = []

	# with open(fname + '.csv', newline='\n') as csvfile:
	with codecs.open(fname + '.csv', 'r', 'UTF-8') as csvfile:
		emaildict = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		
		for row in emaildict:
			xlineFN = row[first_name]
			xlineSU = row[surname]
			xlineEM = row[email]
			xlineEM = xlineEM.strip()
			xlineCO = row[company]
			contact = xlineFN + xlineSU
			xlineEMlen = len(xlineEM)
			dot = ('.')
			dash = ('_')
			dict_email = []

			xlineFN_org = xlineFN
			xlineSU_org = xlineSU

			if any(i in plcharacters for i in xlineFN):
			
				for i in xlineFN:
					if i in plcharacters:
						xlineFN = xlineFN.replace(i, plcharactersDICT[i])

			if any(i in plcharacters for i in xlineSU):
			
				for i in xlineSU:
					if i in plcharacters:
						xlineSU = xlineSU.replace(i, plcharactersDICT[i])

			if ("@") in str(xlineEM):
				xlineEMspAT = xlineEM.split('@')  				# dzieli email na pol '@'																
				dotnumber = 0
				for xchar in xlineEMspAT[1]:
					if xchar == dot: dotnumber +=1
				
				xlineEMspDOT = str(xlineEMspAT[1]).split('.')
				xdotnumber = 0
				domError = ''
				##
				# rozdziela domene emaila na company name i domene dlobalna (ale tylo jak do 2 dots, powyzej jeszcze nie)
				##
				while xdotnumber <= dotnumber:
					if dotnumber == 0: domError = 'no valid email adress'
					elif dotnumber == 1:
						domComp = str(xlineEMspDOT[0])
						domGlob = str(xlineEMspDOT[1])
					elif dotnumber == 2:
						domComp = str(xlineEMspDOT[0])
						domGlob = str(xlineEMspDOT[1] + '.' + xlineEMspDOT[2])
					xdotnumber +=1											
				
				xindxat = str(xlineEM).index("@")
				if str(xlineEMspAT[0]).lower() == (xlineFN[0] + xlineSU).lower():			# 01: fsurname@domain.com
					dict_email = [xlineCO, 'fsurname', '@' + xlineEMspAT[1]]
					emailcntr +=1
				
				elif str(xlineEMspAT[0]).lower() == (xlineFN + '.' + xlineSU).lower():		# 02: first_name.surname@domain.com
					dict_email = [xlineCO, 'first_name.surname', '@' + xlineEMspAT[1]]
					emailcntr +=1

				elif str(xlineEMspAT[0]).lower() == (xlineFN[0] + '.' + xlineSU).lower():	# 03: f.surname@domain.com
					dict_email = [xlineCO, 'f.surname', '@' + xlineEMspAT[1]]
					emailcntr +=1
				
				elif str(xlineEMspAT[0]) == (xlineFN).lower():								# 04: first_name@domain.com
					dict_email = [xlineCO, 'first_name', '@' + xlineEMspAT[1]]
					emailcntr +=1
				
				elif str(xlineEMspAT[0]) == (xlineSU).lower():								# 05: surname@domain.com
					dict_email = [xlineCO, 'surname', '@' + xlineEMspAT[1]]
					emailcntr +=1
				
				elif str(xlineEMspAT[0]).lower() == (xlineFN + '_' + xlineSU).lower():		# 06: first_name_surname@domain.com
					dict_email = [xlineCO, 'first_name_surname', '@' + xlineEMspAT[1]]
					emailcntr +=1

				elif str(xlineEMspAT[0]).lower() == (xlineFN + '-' + xlineSU).lower():		# 07: first_name-surname@domain.com
					dict_email = [xlineCO, 'first_name-surname', '@' + xlineEMspAT[1]]
					emailcntr +=1
				
				elif str(xlineEMspAT[0]).lower() == (xlineFN + xlineSU).lower():			# 08: first_namesurname@domain.com
					dict_email = [xlineCO, 'first_namesurname', '@' + xlineEMspAT[1]]
					emailcntr +=1
				
				elif str(xlineEMspAT[0]).lower() == (xlineSU + xlineFN).lower():			# 09: surnamefirst_name@domain.com
					dict_email = [xlineCO, 'surnamefirst_name', '@' + xlineEMspAT[1]]
					emailcntr +=1	

				elif str(xlineEMspAT[0]).lower() == (xlineSU + '.' + xlineFN).lower():			# 10: surname.first_name@domain.com
					dict_email = [xlineCO, 'surname.first_name', '@' + xlineEMspAT[1]]
					emailcntr +=1

				elif str(xlineEMspAT[0]).lower() == (xlineSU + '-' + xlineFN).lower():			# 11 surname-first_name@domain.com
					dict_email = [xlineCO, 'surname-first_name', '@' + xlineEMspAT[1]]
					emailcntr +=1

				elif str(xlineEMspAT[0]).lower() == (xlineSU + '_' + xlineFN[0]).lower():			# 12: surname_f@domain.com
					dict_email = [xlineCO, 'surname_f', '@' + xlineEMspAT[1]]
					emailcntr +=1

				elif str(xlineEMspAT[0]).lower() == (xlineSU + '_' + xlineFN).lower():			# 13: surname_first_name@domain.com
					dict_email = [xlineCO, 'surname_first_name', '@' + xlineEMspAT[1]]
					emailcntr +=1

				elif str(xlineEMspAT[0]).lower() == (xlineSU + xlineFN[0]).lower():			# 14: surnamef@domain.com
					dict_email = [xlineCO, 'surnamef', '@' + xlineEMspAT[1]]
					emailcntr +=1

				elif str(xlineEMspAT[0]).lower() == (xlineFN + xlineSU[0]).lower():			# 15: first_name[s]@domain.com
					dict_email = [xlineCO, 'first_names', '@' + xlineEMspAT[1]]
					emailcntr +=1


				else:
					# print("Can't recognise the pattern: " + xlineFN_org + ' ' + xlineSU_org + ' - ' + xlineEM)
					EMerrorfile.append([xlineFN_org, xlineSU_org, xlineEM])

				if str('@' + xlineEMspAT[1]) not in str(emailslist) and dict_email != []:							# wybiera niepowtarzalne emaile
					emailslist.append(dict_email)
					emailcntr_uniq +=1


			cntr +=1

			if round((cntr/cntrpercent), 2) > 0.05 and '5' not in countercheck:
				print('Progress: 5%')
				countercheck.append('5')			
			if round((cntr/cntrpercent), 2) > 0.25 and '25' not in countercheck:
				print('Progress: 25%')
				countercheck.append('25')
			if round((cntr/cntrpercent), 2) > 0.50 and '50' not in countercheck:
				print('Progress: 50%')
				countercheck.append('50')
			if round((cntr/cntrpercent), 2) > 0.75 and '75' not in countercheck:
				print('Progress: 75%')
				countercheck.append('75')
			if round((cntr/cntrpercent), 2) > 0.95 and '95' not in countercheck:
				print('Progress: 95%')
				countercheck.append('95')
			if round((cntr/cntrpercent), 2) == 1.00 and '100' not in countercheck:
				print('Progress: 100%')
				countercheck.append('100')

				
	# with open('emailDICT.csv', 'w', newline='\n') as EMfile:
	with codecs.open('emailDICT.csv', 'w', 'UTF-8') as EMfile:
		writer = csv.writer(EMfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		dict_email = ['company', 'format', 'domain']
		writer.writerow(dict_email)
		
		for i in emailslist:
			writer.writerow(i)

	with open('FormatError.txt', 'w', newline='\n') as EMerror:
		writer = csv.writer(EMerror, delimiter=',')
		
		for i in EMerrorfile:
			writer.writerow(i)

	timestop = datetime.datetime.now()
	
	print('Unique email formats created: ' + str(emailcntr_uniq) + ' (' + str(round((emailcntr_uniq/cntrpercent), 2)*100) + '%) in ' + str(timestop-timestart))


if __name__ == "__main__": main()
