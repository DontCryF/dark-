#! /usr/bin/env python3
from datetime import datetime
import time

file = str(input("File or Hash:"))
time1 = datetime.now()

Words = ('a','e','i','o','u','as','es','is','os','us','am','em','im','om','um',
	'ae','ai','ao','au','ea','ei','eu','ia','ie','io','iu','oa','oe','ou','oi',
	'ba','be','bi','bo','bu','ca','ce','ci','co','cu','da','de','di','do','du',
	'fa','fe','fi','fo','fu','ga','ge','gi','go','gu','ha','he','hi','ho','hu',
	'ia','ie','ii','io','iu','ja','je','ji','jo','ju','ka','ke','ki','ko','ku','la',
	'le','li','lo','lu','ma','me','mi','mo','mu','na','ne','ni','no','nu','oa','oe',
	'oi','oo','ou','ua','ue','pa','pe','pi','po','pu','qa','qe','qi','qo','qu','ra',
	're','ri','ro','ru','sa','se','si','so','su','ta','te','ti','to','tu','ua','ue',
	'ui','uu','va','ve','vi','vo','vu','wa','we','wi','wo','xa','xe','xi','xo','xu',
	'ya','ye','yi','yo','yu','ar','er','ir','or','ur','za','ze','zi','zo','zu','rr',
	'cha','che','chi','cho','chu','lha','lhe','lhi','lho','lhu','nha','nhe','nhi','nho',
	'nhu','sha','she','shi','sho','shu','rra','rre','rri','rro','rru','ssa','sse','ssi',
	'sso','gua','gue','gui','gue','guo','guu','qua','que','qui','quo','quu',)

numbers = ('0','1','2','3','4','5','6','7','8','9','10',)

symbols = ('!','@','#','$','%','&','*','_','-','=',)

AltWords = ('a','e','i','o','u','as','es','is','os','us','am','em','im','om','um',
	'Ba','Be','Bi','Bo','Bu','Ca','Ce','Ci','Co','Cu','Da','De','Di','Do','Du',
	'Fa','Fe','Fi','Fo','Fu','Ga','Ge','Gi','Go','Gu','Ha','He','Hi','Ho','Hu',
	'ia','ie','ii','io','iu','ja','je','ji','jo','ju','ka','ke','ki','ko','Ku','La',
	'Le','Li','Lo','Lu','Ma','Me','Mi','Mo','Mu','Na','Ne','Ni','No','Nu','Oa','Ie',
	'oi','oo','ou','ua','ue','Pa','Pe','Pi','Po','Pu','Qa','Qe','Qi','Qo','Qu','Ra',
	'Re','Ri','Ro','Ru','Sa','Se','Si','So','Su','Ta','Te','Ti','To','Tu','Ua','Ue',
	'ui','uu','Va','Ve','Vi','Vo','Vu','Wa','We','Wi','Wo','Xa','Xe','Xi','Xo','Ru',
	'Ya','Ye','Yi','Yo','Yu','aR','eR','iR','oR','uR','Za','Ze','Zi','Zo','Zu','Rr',
	'Cha','che','chi','cho','chu','lha','lhe','lhi','lho','lhu','nha','nhe','Nhi','nho',
	'Nhu','sha','she','shi','sho','shu','rra','rre','rri','rro','rru','SSa','SSe','SSi',
	'SSo','Gua','Gue','Gui','Gue','Guo','Guu','Qua','Que','Qui','Quo','Quu',)

for i1 in Words:
	for i2 in Words:
		for i3 in Words:
			word = (i1 + i2 + i3)
			if word == file:
				time2 = datetime.now()
				result = time2 - time1
				print ("[+] Key Cracked:{}".format(word))
				print ("[!] Time:{}".format(result))
				exit()
			elif word != file:
				print ("[-] Key Not Cracked..\nTrying Other BruteForce....")
				time.slee(2)
				for i1 in Words:
					for i2 in Words:
						word2 = (i1 + i2)
						if word2 == file:
							time3 = datetime.now()
							result2 = time3 - time1
							print ('[+] Key Cracked: {}'.format(word2))
							print ("[!] Time:{}".format(result2))
							exit()
