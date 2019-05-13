# -*- coding: utf-8 -*-
"""
Created on Thu May 17 15:44:16 2018

@author: Zankhana Patel ZKP
"""
import compute
import sys
maxPointDic = {}

classFile = open('class.txt', 'r')
student = {}
for line in classFile:
    fields = line.split('|')
    student[fields[0]] = str(fields[2]).replace("\n","")+', '+ str(fields[1])
classFile.close()

a1File = open('a1.txt', 'r')
a1Map = {}
maximumA1Point = a1File.readline().replace("\n","")
lines = a1File.readlines()[0:]
for line in lines:
    fields = line.split('|')
    a1Map[fields[0]] = int(fields[1].replace("\n",""))
a1File.close()

a2File = open('a2.txt', 'r')
a2Map = {}
maximumA2Point = a2File.readline().replace("\n","")
lines = a2File.readlines()[0:]
for line in lines:
    fields = line.split('|')
    a2Map[fields[0]] = int(fields[1].replace("\n",""))
a2File.close()

ProjectFile = open('project.txt', 'r')
ProjectMap = {}
maximumProjectPoint = ProjectFile.readline().replace("\n","")
lines = ProjectFile.readlines()[0:]
for line in lines:
    fields = line.split('|')
    ProjectMap[fields[0]] = int(fields[1].replace("\n",""))
ProjectFile.close()

test1File = open('test1.txt', 'r')
test1Map = {}
maximumTest1Point = test1File.readline().replace("\n","")
lines = test1File.readlines()[0:]
for line in lines:
    fields = line.split('|')
    test1Map[fields[0]] = int(fields[1].replace("\n",""))
test1File.close()

test2File = open('test2.txt', 'r')
test2Map = {}
maximumTest2Point = test2File.readline().replace("\n","")
lines = test2File.readlines()[0:]
for line in lines:
    fields = line.split('|')
    test2Map[fields[0]] = int(fields[1].replace("\n",""))
test2File.close()

maxPointDic['A1'] = int(maximumA1Point)
maxPointDic['A2'] = int(maximumA2Point)
maxPointDic['PR'] = int(maximumProjectPoint)
maxPointDic['T1'] = int(maximumTest1Point)
maxPointDic['T2'] = int(maximumTest2Point)


def display():
    operation = input('''
    #1> Display individual component
    #2> Display component average
    #3> Display Standard Report
    #4> Sort by alternate column
    #5> Change Pass/Fail point
    #6> Exit
    #''')
    return operation


number = display()
while True:
    if number.isdigit() and int(number) == 1:
        compute.DisplayIndividualComponent(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
    
    elif number.isdigit() and int(number) == 2:
        compute.DisplayComponentAverage(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
    
    elif number.isdigit() and int(number) == 3:
        compute.DisplayStandardReport(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
    
    elif number.isdigit() and int(number) == 4:
        compute.SortbyAlternateColumn(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
        
    elif number.isdigit() and int(number) == 5:
        compute.ChangePassFailPoint(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
        
    elif number.isdigit() and int(number) == 6:
        print('Good Bye')
        sys.exit(0)
    
    else:
        print('You have not typed a valid option')
    number = display()