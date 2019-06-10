import xml.etree.ElementTree as ET
import csv

tree = ET.parse("InputFile.xml")
root = tree.getroot()

# open a file for writing

Owner_data = open('OutputFile.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Owner_data)
owner_head = []


count = 0
for member in root.findall('Owner'):
	owner = []
	address_list = []
	if count == 0:
		name = member.find('Name').tag
		nickname = member.find('NickName').tag        
		owner_head.append(name)
		PhoneNumber = member.find('PhoneNumber').tag
		owner_head.append(PhoneNumber)
		EmailAddress = member.find('EmailAddress').tag
		owner_head.append(EmailAddress)
		Address = member[4].tag
		owner_head.append(Address)
		csvwriter.writerow(owner_head)
		count = count + 1

	name = member.find('Name').text
	owner.append(name)
	nickname = member.find('NickName').text
	owner.append(nickname)
	PhoneNumber = member.find('PhoneNumber').text
	owner.append(PhoneNumber)
	EmailAddress = member.find('EmailAddress').text
	owner.append(EmailAddress)
	Address = member[4][0].text
	address_list.append(Address)
	City = member[4][1].text
	address_list.append(City)
	StateCode = member[4][2].text
	address_list.append(StateCode)
	PostalCode = member[4][3].text
	address_list.append(PostalCode)
	Country = member[4][4].text
	address_list.append(Country)
	owner.append(address_list)
	csvwriter.writerow(owner)
Owner_data.close()