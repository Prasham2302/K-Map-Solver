# CSE 101 - IP HW2
# K-Map Minimization 
# Name: PRASHAM NARAYAN
# Roll Number: 2018359
# Section:B
# Group:8
# Date:18-10-2018
def minFunc(numVar, stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.
	"""
	stringIn = stringIn.replace("(","")
	stringIn = stringIn.replace(")","")
	stringIn = stringIn.replace(" ","")
	d_index = stringIn.find("d")
	if d_index != -1:
		dontlist = stringIn[d_index+1:].split(",")
		for i in range (0,len(dontlist),+1):
			dontlist[i] = int(dontlist[i])
	else : 
		dontlist = []
	stringIn = stringIn.replace("d",",")
	list1 = stringIn.split(",")
	for i in range (0,len(list1),+1):
		list1[i] = int_to_binary(int(list1[i]),numVar)
# for 4 variables
	if numVar == 4:
		order_1 = []
		order_2 = []
		order_3 = []
		for i in range (0,len(list1),+1):
			for j in range (i,len(list1),+1):
				order_1.append(simplifier(list1[i],list1[j],4))
		d = order_1.count(None)
		for i in range (0,d,+1):
			order_1.remove(None)
		order_1 = list(set(order_1))
		for i in range (0,len(order_1),+1):
			for j in range (i,len(order_1),+1):
				order_2.append(simplifier(order_1[i],order_1[j],4))
		d = order_2.count(None)
		for i in range (0,d,+1):
			order_2.remove(None)
		order_2 = list(set(order_2))
		for i in range (0,len(order_2),+1):
			for j in range (i,len(order_2),+1):
				order_3.append(simplifier(order_2[i],order_2[j],4))
		d = order_3.count(None)
		for i in range (0,d,+1):
			order_3.remove(None)
		order_3 = list(set(order_3))
		prime = []
		all = []
		all.extend(list1)
		all.extend(order_1)
		all.extend(order_2)
		all.extend(order_3)
		all.extend(order_1)
		if len(order_3)!=0:
			i=0
			while i < len(order_3):
				j=0
				while j<len(all):
					if order_3[i]==all[j]:
						j+=1
					elif cover_checker(order_3[i],all[j],4):
						all.remove(all[j])
					else:
						j+=1
				i+=1
			all = list(set(all))
		if len(order_2)!=0:
			i=0
			while i < len(order_2):
				j=0
				while j<len(all):
					if order_2[i]==all[j]:
						j+=1
					elif cover_checker(order_2[i],all[j],4):
						all.remove(all[j])
					else:
						j+=1
				i+=1
			all = list(set(all))
		if len(order_1)!=0:
			i=0
			while i < len(order_1):
				j=0
				while j<len(all):
					if order_1[i]==all[j]:
						j+=1
					elif cover_checker(order_1[i],all[j],4):
						all.remove(all[j])
					else:
						j+=1
				i+=1
			all = list(set(all))
		prime = all
		#list of all prime impicants
		minterm = {}
		minterm_int = {} 
		for i in range (0,len(all),+1):
			minterm[all[i]], minterm_int[all[i]]=calculate_minterms(all[i],4)
		quinn_Number = []
		#now we have the minterms in integer form and binary form
		a = []
		for i in range (0,len(prime),+1):
			quinn_Number.extend(minterm_int[prime[i]])
		for i in range (0,len(dontlist),+1):
			while dontlist[i] in quinn_Number:
				quinn_Number.remove(dontlist[i])
		quinn = list(set(quinn_Number))
		essentialint = []
		#list of all essential prime implicants
		for i in range (0,len(quinn),+1):
			count = 0
			for j in range (0,len(quinn_Number),+1):
				if quinn[i] == quinn_Number[j]:
					count += 1
			if count == 1:
				essentialint.append(quinn[i])
		final = []
		t = []
		for i in range (0,len(prime),+1):
			t.extend(minterm_int[prime[i]])
			for j in range (0,len(t),+1):
				for k in range (0,len(essentialint),+1):
					if essentialint[k]==t[j]:
						final.append(prime[i])
			t = []
		final = list(set(final))
		#final answer in binary form
		alpha_final = []
		for i in range (0,len(final),+1):
			alpha_final.append(binary_to_alpha(final[i],4))
		answer = ''
		for i in range (0,len(alpha_final),+1):
			answer = answer + str(alpha_final[i])
			if i != len(alpha_final)-1:
				answer += " + "
		print ("Answer : ",answer)
		return answer
#for 3 variables
	elif numVar == 3:
		order_1 = []
		order_2 = []
		for i in range (0,len(list1),+1):
			for j in range (i,len(list1),+1):
				order_1.append(simplifier(list1[i],list1[j],3))
		d = order_1.count(None)
		for i in range (0,d,+1):
			order_1.remove(None)
		order_1 = list(set(order_1))
		for i in range (0,len(order_1),+1):
			for j in range (i,len(order_1),+1):
				order_2.append(simplifier(order_1[i],order_1[j],3))
		d = order_2.count(None)
		for i in range (0,d,+1):
			order_2.remove(None)
		order_2 = list(set(order_2))
		prime = []
		all = []
		all.extend(list1)
		all.extend(order_1)
		all.extend(order_2)
		if len(order_2)!=0:
			i=0
			while i < len(order_2):
				j=0
				while j<len(all):
					if order_2[i]==all[j]:
						j+=1
					elif cover_checker(order_2[i],all[j],3):
						all.remove(all[j])
					else:
						j+=1
				i+=1
			all = list(set(all))
		if len(order_1)!=0:
			i=0
			while i < len(order_1):
				j=0
				while j<len(all):
					if order_1[i]==all[j]:
						j+=1
					elif cover_checker(order_1[i],all[j],3):
						all.remove(all[j])
					else:
						j+=1
				i+=1
			all = list(set(all))
		prime = all
		#list of all prime impicants	
		minterm = {}
		minterm_int = {} 
		for i in range (0,len(all),+1):
			minterm[all[i]], minterm_int[all[i]]=calculate_minterms(all[i],3)
		#now we have the minterms in integer form and binary form		
		quinn_Number = []
		a = []
		for i in range (0,len(prime),+1):
			quinn_Number.extend(minterm_int[prime[i]])
		for i in range (0,len(dontlist),+1):
			while dontlist[i] in quinn_Number:
				quinn_Number.remove(dontlist[i])
		quinn = list(set(quinn_Number))
		essentialint = []
		for i in range (0,len(quinn),+1):
			count = 0
			for j in range (0,len(quinn_Number),+1):
				if quinn[i] == quinn_Number[j]:
					count += 1
			if count == 1:
				essentialint.append(quinn[i])
        #list of all essential prime implicants
		final = []
		t = []
		for i in range (0,len(prime),+1):
			t.extend(minterm_int[prime[i]])
			for j in range (0,len(t),+1):
				for k in range (0,len(essentialint),+1):
					if essentialint[k]==t[j]:
						final.append(prime[i])
			t = []
		final = list(set(final))
		#final answer in binary form
		alpha_final = []
		for i in range (0,len(final),+1):
			alpha_final.append(binary_to_alpha(final[i],3))
		answer = ''
		for i in range (0,len(alpha_final),+1):
			answer = answer + str(alpha_final[i])
			if i != len(alpha_final)-1:
				answer += " + "
		print ("Answer : ",answer)
		return answer	
#for 2 variables
	elif numVar == 2:
		order_1 = []
		for i in range (0,len(list1),+1):
			for j in range (i,len(list1),+1):
				order_1.append(simplifier(list1[i],list1[j],2))
		d = order_1.count(None)
		for i in range (0,d,+1):
			order_1.remove(None)
		order_1 = list(set(order_1))
		prime = []
		all = []
		all.extend(list1)
		all.extend(order_1)
		if len(order_1)!=0:
			i=0
			while i < len(order_1):
				j=0
				while j<len(all):
					if order_1[i]==all[j]:
						j+=1
					elif cover_checker(order_1[i],all[j],2):
						all.remove(all[j])
					else:
						j+=1
				i+=1
			all = list(set(all))
		prime = all
		#list of all prime impicants	
		minterm = {}
		minterm_int = {} 
		for i in range (0,len(all),+1):
			minterm[all[i]], minterm_int[all[i]]=calculate_minterms(all[i],2)
		#now we have the minterms in integer form and binary form
		quinn_Number = []
		a = []
		for i in range (0,len(prime),+1):
			quinn_Number.extend(minterm_int[prime[i]])
		for i in range (0,len(dontlist),+1):
			while dontlist[i] in quinn_Number:
				quinn_Number.remove(dontlist[i])
		quinn = list(set(quinn_Number))
		essentialint = []
		for i in range (0,len(quinn),+1):
			count = 0
			for j in range (0,len(quinn_Number),+1):
				if quinn[i] == quinn_Number[j]:
					count += 1
			if count == 1:
				essentialint.append(quinn[i])
        #list of all essential prime implicants
		final = []
		t = []
		for i in range (0,len(prime),+1):
			t.extend(minterm_int[prime[i]])
			for j in range (0,len(t),+1):
				for k in range (0,len(essentialint),+1):
					if essentialint[k]==t[j]:
						final.append(prime[i])
			t = []
		final = list(set(final))
		#final answer in binary form
		alpha_final = []
		for i in range (0,len(final),+1):
			alpha_final.append(binary_to_alpha(final[i],2))
		answer = ''
		for i in range (0,len(alpha_final),+1):
			answer = answer + str(alpha_final[i])
			if i != len(alpha_final)-1:
				answer += " + "
		print ("Answer : ",answer)
		return answer	
	if numvar == 1:
		if list1[0] == '0':
			return "A"
		else :
			return """A'"""
def int_to_binary(integer,var):
	"""function to convert integer value to binary"""
	a = integer
	st = ""
	while a!=0:
		rem = a%2
		a=a//2
		if rem == 1:
			st = "1" + st
		elif rem==0 :
			st= "0"+ st
	if len(st)<var:
		for i in range (0,var-len(st),+1):
			st = "0"+st
	return st
def simplifier(a,b,numVar):
	"""function which takes two binary inputs and 
		simplifies it by removing the uncommon digit 
		by "-" if all other digits are mathcing""" 
	combined = ''
	quantity = 0
	for i in range (0,numVar,+1):
		if a[i]==b[i]:
			combined+=a[i]
		else:
			combined+='-'
			quantity += 1
	if quantity > 1 :
		return None
	else :
		if combined == a or combined == b :
			return None
		else :
			return combined
def cover_checker(a,b,numVar):
	"""takes two input value (a,b) and checks whether
		b lies in the cover of a""" 
	count = 0
	for i in range (0,numVar,+1):
		if a[i]=='-':
			count += 1
		elif a[i]!='-' and a[i]==b[i]:
			count += 1
	if count == numVar:
		return True
	else :
		return False
def calculate_minterms(prime,numvar):
	"""calculates all original minterms for the given
		input in binary form by replacing each dash with 
		0 and 1""" 
	int_list=[]
	pos = []
	count = 0
	for i in range (0,numvar,+1):
		if prime[i]=="-":
			count+=1
			pos.append(i)
	
	if count == 3:
		a1 = []
		a2 = []
		a3 = []
		a1.append(prime[:pos[0]]+'0'+prime[pos[0]+1:])
		a1.append(prime[:pos[0]]+'1'+prime[pos[0]+1:])
		a2.append(a1[0][:pos[1]]+'0'+a1[0][pos[1]+1:])
		a2.append(a1[0][:pos[1]]+'1'+a1[0][pos[1]+1:])
		a2.append(a1[1][:pos[1]]+'0'+a1[1][pos[1]+1:])
		a2.append(a1[1][:pos[1]]+'1'+a1[1][pos[1]+1:])
		a3.append(a2[0][:pos[2]]+'0'+a2[0][pos[2]+1:])
		a3.append(a2[0][:pos[2]]+'1'+a2[0][pos[2]+1:])
		a3.append(a2[1][:pos[2]]+'0'+a2[1][pos[2]+1:])
		a3.append(a2[1][:pos[2]]+'1'+a2[1][pos[2]+1:])
		a3.append(a2[2][:pos[2]]+'0'+a2[2][pos[2]+1:])
		a3.append(a2[2][:pos[2]]+'1'+a2[2][pos[2]+1:])
		a3.append(a2[3][:pos[2]]+'0'+a2[3][pos[2]+1:])
		a3.append(a2[3][:pos[2]]+'1'+a2[3][pos[2]+1:])
		int_list.extend(a3)
	elif count == 2:
		a1 = []
		a2 = []
		a1.append(prime[:pos[0]]+'0'+prime[pos[0]+1:])
		a1.append(prime[:pos[0]]+'1'+prime[pos[0]+1:])
		a2.append(a1[0][:pos[1]]+'0'+a1[0][pos[1]+1:])
		a2.append(a1[0][:pos[1]]+'1'+a1[0][pos[1]+1:])
		a2.append(a1[1][:pos[1]]+'0'+a1[1][pos[1]+1:])
		a2.append(a1[1][:pos[1]]+'1'+a1[1][pos[1]+1:])
		int_list.extend(a2)
	elif count == 1:
		a1 = []
		a1.append(prime[:pos[0]]+'0'+prime[pos[0]+1:])
		a1.append(prime[:pos[0]]+'1'+prime[pos[0]+1:])
		int_list.extend(a1)
	if count == 0:
		int_list.append(prime)
	full_int = []
	for i in range (0,len(int_list),+1):
		full_int.append(int(int_list[i],2))
	return int_list, full_int
def binary_to_alpha(binary,numvar):
	"""function to convert a binary no. to 
		its required alphabetical value"""
	st = ""
	for i in range (0,numvar,+1):
		if binary[i]!='-':
			st += str(alpha_calculator(binary[i],(numvar-i-1),numvar))
	return st	
def alpha_calculator(digit,pos,numvar):
	"""function to convert a digits alpabetical value
		according to its position in the binary number"""
	if numvar == 3:
		pos += 1
	elif numvar == 2:
		pos+= 2
	digit = int(digit)
	pos = int(pos)
	if pos == 0:
		if digit == 1:
			return "z"
		elif digit == 0:
			return """z'"""	
	if pos == 1:
		if digit == 1:
			return "y"
		elif digit == 0:
			return """y'"""
	if pos == 2:
		if digit == 1:
			return "x"
		elif digit == 0:
			return """x'"""
	if pos == 3:
		if digit == 1:
			return "w"
		elif digit == 0:
			return """w'"""
num = int(input("Enter the no. of Variables : "),10)
string = input("Enter the string : ")
minFunc((num),string)