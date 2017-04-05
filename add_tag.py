# -*- coding: utf8 -*-
import sys
import os

#Add tag at the end of the line
#Usage: list_filename output_folder
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

lab_state_fn = ""
lab_mono_fn = ""

with open(sys.argv[1], mode='r', encoding='UTF-8') as file:

	list_info = file.readlines()
	i = 0	
	while i < len(list_info):
		phone = []
		emotion = []
		list_info[i] = list_info[i].strip()
		line = list_info[i].split(" ")
		lab_mono_fn = line[1]
		lab_state_fn = line[0]		
		out_lab_fn = Make_output_fn(lab_state_fn,sys.argv[2])
				
		with open(lab_mono_fn, mode='r', encoding='UTF-8') as file:
			mono_info = file.readlines()
			j = 0
			while j < len(mono_info):
				mono_info[j] = mono_info[j].strip()
				mono_line = mono_info[j].split(" ")
				phone_emo = mono_line[-1].split("\t")
				phone.append(phone_emo[0])
				emotion.append(phone_emo[-1])
				j += 1

		out = open(out_lab_fn, mode='w', encoding='UTF-8')
		with open(lab_state_fn, mode='r', encoding='UTF-8') as file:

			states_info = file.readlines()
			j = 0
			if len(states_info) != len(phone) * 5 :
				input()
			while j < len(states_info):
				states_info[j] = states_info[j].strip()
				states_phone = Get_phone_in_states(states_info[j])
				mono_index = int(j/5)
				if states_phone == phone[mono_index]:
					emotion_1 = Get_emotion_1(emotion[mono_index])	
					e = states_info[j].rindex("[")				
					#print("%s[e1=%s]%s"%(states_info[j][0:e],emotion_1,states_info[j][e:len(states_info[j])]))
					out.write(states_info[j][0:e]+"[e1="+emotion_1+"]"+states_info[j][e:len(states_info[j])]+"\n")
				j += 1				
		out.close()
		i += 1
