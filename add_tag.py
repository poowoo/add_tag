# -*- coding: utf8 -*-
import sys
import os

#Add emotion tag at the end of the line
#Usage: list_filename output_extension

emotion = -1
lab_fn = ""

with open(sys.argv[1], mode='r', encoding='UTF-8') as file:
	list_info = file.readlines()
	i = 0
	while i < len(list_info):
		list_info[i] = list_info[i].strip()
		line = list_info[i].split(" ")
		emotion = line[1]
		lab_fn = line[0]
		o_lab_fn = line[0].replace(".lab",sys.argv[2])
		out = open(o_lab_fn, mode='w', encoding='UTF-8')
		with open(lab_fn, mode='r', encoding='UTF-8') as file:
			lab_info = file.readlines()
			j = 0
			while j < len(lab_info):
				lab_info[j] = lab_info[j].strip()
				#e = lab_info[j].rindex("[")
				#print("%s[e1=%s]%s"%(lab_info[j][0:e],emotion,lab_info[j][e:len(lab_info[j])]))				
				#out.write(lab_info[j][0:e]+"[e1="+emotion+"]"+lab_info[j][e:len(lab_info[j])]+"\n")
				out.write(lab_info[j][0:len(lab_info[j])]+"[e1="+emotion+"]"+"\n")
				j += 1				
		out.close()
		i += 1
