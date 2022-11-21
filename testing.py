

import math
import numpy as np
import cmath
import ast



x = [23, 1, 9, 3]
y = ["a", "b", "c", "d"]

y.insert(1, "y")

print(y)

x = sorted(x)




#x = "777"
#if type(eval(x[-1])) == int :
#	print("integer")




#prior = "[ [4, 5, 4], [7, 7, 8], [1, 6, 7] , [5, 7, 4]]"

#prior = prior.replace("v", "")
#prior = prior.replace("x", "")
#prior = prior.replace("y", "")
#prior = prior.replace("z", "")
#prior = prior.replace("k", "")
#prior = prior.replace("{", "[")
#prior = prior.replace("}", "]")
#prior = prior.replace(" ", "")

#prior1 = ast.literal_eval(prior)
#print(len(prior1))

#prior2 = prior1[:-1]
#print(prior2)

#prior3 = prior1[-1]
#print(prior3)
#result = np.linalg.inv(prior2).dot(prior3)

#v= result[0]

#x = result[1]

#y = result[2]

#print(f" v = {v}    x = { x}   y = {y}")





#c = []
#hint = "X² -  2x - 8" 

#h = hint.index("x")

#if hint[h-1] == " ":
#	hint = hint.replace("x", "1x")
#	
#if hint[0] == "X" or hint[0] == "-":
#	hint = hint.replace("X²", "1X²")
#	hint = hint.replace("X2", "1X2")
#	
#if hint[-1] == "x" or hint[-2] == "x":
#	hint = hint.replace("x", "x + 0")


#	

#hint = hint.replace("X²", "")
#hint = hint.replace("x2", "")
#hint = hint.replace("x", "")
#hint = hint.split(" ")

#for i in hint:
#	if i != "":
#		c.append(i)
#g = len(c)
#print(c)

#hinta = c[0]
#hintb = c[2]
#hintc = c[4]




#print(hinta)
#print(hintb)
#print(hintc)


#if c[1] == "+" and c[3] == "+":

#	a = eval(hinta)
#	b = eval(hintb)
#	c = eval(hintc)
#	
#	px = (-b + np.sqrt(b*b - (4 * a* c))) /(2 * a)
#	py = (-b - np.sqrt(b*b - (4 * a* c))) /(2 * a)
#	
#	print(px)
#	print(py)

#elif c[1] == "+" and c[3] == "-":

#	a = eval(hinta)
#	b = eval(hintb)
#	c = -eval(hintc)
#	
#	px = (-b + np.sqrt(b*b - (4 * a* c))) /(2 * a)
#	py = (-b - np.sqrt(b*b - (4 * a* c))) /(2 * a)
#	
#	print(px)
#	print(py)

#elif c[1] == "-" and c[3] == "+":

#	a = eval(hinta)
#	b = -eval(hintb)
#	c = eval(hintc)
#	
#	px = (-b + np.sqrt(b*b - (4 * a* c))) /(2 * a)
#	py = (-b - np.sqrt(b*b - (4 * a* c))) /(2 * a)
#	
#	print(px)
#	print(py)

#elif c[1] == "-" and c[3] == "-":

#	a = eval(hinta)
#	b = -eval(hintb)
#	c = -eval(hintc)
#	
#	px = (-b + np.sqrt(b*b - (4 * a* c))) /(2 * a)
#	py = (-b - np.sqrt(b*b - (4 * a* c))) /(2 * a)
#	
#	print(px)
#	print(py)




#m1 = "{ {2, 0}, {7, 9} }"
#m2 = m1.replace("{", "[")
#m3 = m2.replace("}","]")
#m4= np.array(ast.literal_eval(m3))

#mx2 = "{ {4, 7} ,  {8, 4} }"
#mx3 = mx2.replace("{", "[")
#mx4 = mx3.replace("}","]")
#mx5 = np.array(ast.literal_eval(mx4))












#x = "1 ,2, 3, 4"
#print(type(x))
#y = ast.literal_eval(x)
#print(type(y))

#y = x.replace(",", "")

#print(y.replace(" ", ""))








#u = math.degrees(math.asin(0.5))
#print(u)


#original_list= []

#final_list = []

#prior = "[ [2, 0], [0, 2]]"

#y = ""

#for i in prior:
#	y+= i

#p = eval(y)

#Fig = len(p)

#original_list.append(p)


#for j in range(Fig):
#	

#	final_list.append(original_list[0][j])

#x = np.linalg.det(final_list)


