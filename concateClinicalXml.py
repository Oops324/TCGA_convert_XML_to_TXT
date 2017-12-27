#!/usr/bin/env python

'''
Author: Anna Fei
Date: 23/Nov/2017
Usage: python concateClinicalXml.py clinicalF_List
Function: concatenate content of files
Version: python 2.7

'''


import xml.etree.ElementTree as ET
import csv
import sys

def Xml2csv(listF,outputF):
	listF_handle = open(listF,'r')
	Resident_data = open(outputF,'w')

	n = 0
	for fileName in listF_handle:
		n +=1
		xmlF = fileName.rstrip()

		tree = ET.parse(xmlF)
		root = tree.getroot()

		Head_L =[]
		Value_L =[]		
	
		histological_type_tag = root[1][2].tag
		histological_type_text = root[1][2].text
		vital_status_tag = root[1][5].tag
		vital_status_text = root[1][5].text
		daysToBirth_tag = root[1][6].tag
		daysToBirth_text = root[1][6].text
		daysToLastKnowAlive_tag = root[1][7].tag
		daysToLastKnowAlive_text = root[1][7].text
		daysToDeath_tag = root[1][8].tag
		daysToDeath_text = root[1][8].text
		daysToLastFollowup_tag = root[1][9].tag
		daysToLastFollowup_text = root[1][9].text
		raceList_tag = root[1][10].tag
		raceList_text = root[1][10].text
		patientBarcode_tag = root[1][11].tag
		patientBarcode_text = root[1][11].text
		patientId_tag = root[1][13].tag
		patientId_text = root[1][13].text
		patientUUID_tag = root[1][14].tag
		patientUUID_text = root[1][14].text
		icdSite_tag = root[1][17].tag
		icdSite_text = root[1][17].text
		icdHistology_tag = root[1][18].tag
		icdHistology_text = root[1][18].text
		icd10_tag = root[1][19].tag
		icd10_text = root[1][19].text
		stageEvent_tag = root[1][25].tag
		stageEvent_text = root[1][25].text
		cancerStatus_tag = root[1][26].tag
		cancerStatus_text = root[1][26].text
		residualTumor_tag = root[1][33].tag
		residualTumor_text = root[1][33].text
	
		HeadFinal_L = []
		ValueFinal_L = []
		Head_L = [patientBarcode_tag,cancerStatus_tag,vital_status_tag,daysToBirth_tag]
		Value_L = [patientBarcode_text,cancerStatus_text,vital_status_text,daysToBirth_text]
		for element in Head_L:
			if element is None:
				element = str(element)
			title = element.split("}",1)[1]
			HeadFinal_L.append(title)
		for Element in Value_L:
			if Element is None:
				Element = str(Element)
			ValueFinal_L.append(Element)
		HeadLine = "Index\t" + "\t".join(HeadFinal_L)
		ValueLine = "Patient\t" + "\t".join(ValueFinal_L)
		if n ==1:
			Resident_data.write("%s\n" % HeadLine)
			Resident_data.write("%s\n" % ValueLine)
		else:
			Resident_data.write("%s\n" % ValueLine)
	Resident_data.close()


if __name__=="__main__":
        listF = sys.argv[1]
	
	
        outputF = listF.split(".",1)[0]+"_Total.txt"
 	Xml2csv(listF,outputF)
	'''
	head_L = []
	value_L = []

	for n in range(1,66):
		title_long = root[1][n].tag
		title = title_long.split("}",1)[1]
		value = root[1][n].text
		if title is None:
			title= str(title)
		if value is None:
			value = str(value)
		head_L.append(title)
		value_L.append(value)
	print head_L
	print value_L
	headLine = "Patient\t" + "\t".join(head_L)
	valueLine = "Patient\t" + "\t".join(value_L)

	for member in root:
		print "member.tag:",member.tag

	for patient in root.findall('{http://tcga.nci/bcr/xml/clinical/read/2.7}patient'):
	
		gender = patient.find('{http://tcga.nci/bcr/xml/shared/2.7}gender').text
	
		print "find.text",gender

	
	gender = patient.find('{http://tcga.nci/bcr/xml/shared/2.7}gender').text

	'''

