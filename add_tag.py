# -*- coding: utf8 -*-
import sys
import os

#Add tag at the end of the line
#Usage: list_filename output_folder
#emotion information are in mono file
def Make_output_fn(lab_fn,output_folder):

	lab_fn_no_folder_index = lab_fn.rindex('\\')
	out_lab_fn = output_folder + lab_fn[lab_fn_no_folder_index:len(lab_fn)]

	return out_lab_fn

def Get_phone_in_states(states_info):

	begin_index = states_info.index('-')
	end_index = states_info.index('+')
	current_phone = states_info[begin_index+1:end_index]
	return current_phone

def Get_emotion_1(emotion):

	emotion_all = emotion.split(',')
	return emotion_all[2]

	
if __name__ == "__main__":

	lab_full_fn = ""
	lab_mono_fn = ""
	
	with open(sys.argv[1], mode='r', encoding='UTF-8') as file:
	
		phone_and_emotion = []
		emotion = []
		phone = []

		list_fn = file.readlines()

		i = 0	
		while i < len(list_fn):
			
			phone.clear()	
			emotion.clear()

			list_fn[i] = list_fn[i].strip()
			line = list_fn[i].split(" ")
			lab_full_fn = line[0]
			lab_mono_fn = line[1]			
			out_lab_fn = Make_output_fn(lab_full_fn,sys.argv[2])
			
			print("loading ",lab_mono_fn)

			with open(lab_mono_fn, mode='r', encoding='UTF-8') as file:
				
				phone_info = file.readlines()
				phone_and_emotion.clear()
				j = 0
				while j < len(phone_info):
					phone_info[j] = phone_info[j].strip()
					phone_line = phone_info[j].split(" ")
					phone_and_emotion = phone_line[-1].split("\t")
					phone.append(phone_and_emotion[0])
					emotion.append(phone_and_emotion[-1].split(","))
					j += 1
	
			out = open(out_lab_fn, mode='w', encoding='UTF-8')
			with open(lab_full_fn, mode='r', encoding='UTF-8') as file:

				full_info = file.readlines()
				j = 0
				while j < len(full_info):
					
					full_info[j] = full_info[j].strip("\n")
					#out.write(full_info[j][0:len(full_info[j])]+"[e1="+str(emotion[j][0])+"]"+"[e2="+str(emotion[j][2])+"]"+"[e3="+str(emotion[j][4])+"]"+"[e4="+str(emotion[j][6])+"]"+"[e5="+str(emotion[j][8])+"]\n")
					out.write(full_info[j][0:len(full_info[j])]+"[e1="+str(emotion[j][0])+"]"+"[e2="+str(emotion[j][1])+"]"+"[e3="+str(emotion[j][2])+"]"+"[e4="+str(emotion[j][3])+"]"+"[e5="+str(emotion[j][4])+"]\n")
					j += 1
			#for states
			#with open(lab_full_fn, mode='r', encoding='UTF-8') as file:
			#		
			#	states_info = file.readlines()
			#	j = 0
			#	if len(states_info) != len(phone) * 5 :
			#		input()
			#	while j < len(states_info):
			#		states_info[j] = states_info[j].strip()
			#		states_phone = Get_phone_in_states(states_info[j])
			#		phone_index = int(j/5)
			#		if states_phone == phone[phone_index]:
			#			emotion_1 = Get_emotion_1(emotion[phone_index])	
			#			e = states_info[j].rindex("[")				
			#			#print("%s[e1=%s]%s"%(states_info[j][0:e],emotion_1,states_info[j][e:len(states_info[j])]))
			#			out.write(states_info[j][0:e]+"[e1="+emotion_1+"]"+states_info[j][e:len(states_info[j])]+"\n")			
			#		j += 1								
	
			out.close()
			i += 1
	