""""

    Name: Muhammad Rizwan Khalid
    Class: BSCS-6A
    Reg. ID: 180459

"""
import math as m
import re as r
import time as t

#this function calculated frequency of each word in a string
def calculate_frequency(string):
    D = {}
    for word in string.strip().split(" "):
        if(word in D):
            D[word] += 1
        else:
            D[word] = 1
    return D

#this function calcuate inner product b/w two vectors
def inner_product(D1, D2):
    inner_product = 0
    for word in D1:
        if(word in D2):
            inner_product += D1[word] * D2[word]
    return inner_product

#this function caluclates vector angle b/w the files
#as we know A.A = |A|^2
def angle(D1, D2):
    num = inner_product(D1, D2)
    den = m.sqrt(inner_product(D1, D1) * inner_product(D2, D2))
    angle = m.acos(safe_div(num, den))
    angle *= 57.2958
    return round(angle, 2)

#safe divide in case of division by zero
def safe_div(x,y):
    if y == 0:
        return 0
    return x / y


"""

    START OF THE MAIN FUNCTION

"""


file = open("Test Files\\test5.txt",'r')
doc1 = file.read()
file = open("Test Files\\test5.txt",'r')
doc2 = file.read()
#removing punctuations from the files and converting to lowercase
doc1 = doc1.lower()
doc1 = r.sub(r'[^\w\s]','',doc1) #removing non-alphabets
doc1 = r.sub("\n\s*\n*", ' ', doc1) #removing multiple lines
doc1 = r.sub(' +',' ', doc1) #removing multiple spaces
doc2 = doc2.lower()
doc2 = r.sub(r'[^\w\s]','',doc2)
doc2 = r.sub("\n\s*\n*", ' ', doc2)
doc2 = r.sub(' +',' ', doc2)

#starting timer
start = t.time()
#caculating the frequency of each documnet for both files
D1 = calculate_frequency(doc1)
D2 = calculate_frequency(doc2)
#calculating vector angle between the file 
angle = angle(D1, D2)
end = t.time()
#getting time in milliseconds
time_taken = (end -  start) * 1000 
if(angle == 0.0):
    print("The angle between these files is %d degree" %(int(angle)))
    print("The documents are similar because document distace is zero")
    print("The running time is %.2f milliseconds" %(time_taken))
    
elif(angle == 90.0):
    print("The angle between these files is %d degree" %(int(angle)))
    print("The documents are totally different because document distace is 90")
    print("The running time is %.2f milliseconds" %(time_taken))
    
else:
    percentage = ((90-angle)/90) * 100
    print("The angle between these files is about %.2f degree" %(angle))
    print("The documents are about %.2f percent similar" %(percentage))
    print("The running time is %.2f milliseconds" %(time_taken))


