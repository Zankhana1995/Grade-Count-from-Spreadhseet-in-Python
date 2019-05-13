# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:19:38 2018

@author: Zankhana Patel ZKP
"""

import operator

passFailGradeDefault = 50

def DisplayIndividualComponent(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map):

  componentName = (input("Please enter component name (A1, A2, PR, T1, or T2) :")).upper()

  if componentName == 'A1':
      print('{} grades ({})'.format(componentName, maxPointDic[componentName]))
      for key, value in sorted(student.items()):
          if key in a1Map:
            print('{: <5}\t{: <14}\t{: <2} '.format(key, value,a1Map.get(key," ")))

  elif componentName == 'A2':
      print('{} grades ({})'.format(componentName, maxPointDic[componentName]))
      for key, value in sorted(student.items()):
          if key in a2Map:
            print('{: <5}\t{: <14}\t{: <2} '.format(key, value,a2Map.get(key," ")))

  elif componentName == 'PR':
      print('{} grades ({})'.format(componentName, maxPointDic[componentName]))
      for key, value in sorted(student.items()):
          if key in ProjectMap:
            print('{: <5}\t{: <14}\t{: <2} '.format(key, value,ProjectMap.get(key," ")))

  elif componentName == 'T1':
      print('{} grades ({})'.format(componentName, maxPointDic[componentName]))
      for key, value in sorted(student.items()):
          if key in test1Map:
            print('{: <5}\t{: <14}\t{: <2} '.format(key, value,test1Map.get(key," ")))

  elif componentName == 'T2':
      print('{} grades ({})'.format(componentName, maxPointDic[componentName]))
      for key, value in sorted(student.items()):
          if key in a2Map:
            print('{: <5}\t{: <14}\t{: <2} '.format(key, value,test2Map.get(key," ")))
  else:
      print('Invalid Entry : Please enter valid component name (A1, A2, PR, T1, or T2)')
      return DisplayIndividualComponent(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)

def DisplayComponentAverage(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map):

  componentName = (input("Please enter component name (A1, A2, PR, T1, or T2) :")).upper()

  if componentName == 'A1':
      print('{} average: {}/{}'.format(componentName, round(sum(a1Map.values())/len(a1Map), 2),maxPointDic[componentName]))
  elif componentName == 'A2':
      print('{} average: {}/{}'.format(componentName,round(sum(a2Map.values())/len(a2Map), 2),maxPointDic[componentName]))
  elif componentName == 'PR':
      print('{} average: {}/{}'.format(componentName,round(sum(ProjectMap.values())/len(ProjectMap), 2),maxPointDic[componentName]))
  elif componentName == 'T1':
      print('{} average: {}/{}'.format(componentName,round(sum(test1Map.values())/len(test1Map),2),maxPointDic[componentName]))
  elif componentName == 'T2':
      print('{} average: {}/{}'.format(componentName,round(sum(test2Map.values())/len(test2Map),2),maxPointDic[componentName]))
  else:
      print('Invalid Entry : Please enter valid component name (A1, A2, PR, T1, or T2)')
      DisplayIndividualComponent(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
  return


def DisplayStandardReport(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map):
        sheet = numericCalculations(passFailGradeDefault,student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
        printSpreadsheet(sheet)
        return

def SortbyAlternateColumn(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map):

  orderName = (input("Please enter sort order (LT, GR) :"))

  if orderName == 'LT' or orderName == 'GR':
      sheet = numericCalculations(passFailGradeDefault,student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
      if orderName == 'LT':
          orderName = 'LN'
      sheet.sort(key=operator.itemgetter(orderName))
      printSpreadsheet(sheet)
  else:
      print('Invalid Entry : Please enter valid sort order (LT, GR)')
      SortbyAlternateColumn(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
  return


def ChangePassFailPoint(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map):

  passFailPoint = (input("Please enter new P/F point :"))

  if passFailPoint.isdigit() and (0 < int(passFailPoint) <= 100):
     sheet = numericCalculations(int(passFailPoint),student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
     printSpreadsheet(sheet)
  else:
      print('Invalid Entry : Please enter P/F point between 0 to 100')
      ChangePassFailPoint(student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map)
  return


def numericCalculations(passFailGrade,student,maxPointDic,a1Map,a2Map,ProjectMap,test1Map,test2Map):

    spreadsheet = []

    for key, value in sorted(student.items()):

        studentinfo = {}

        numericTotal = (a1Map.get(key,0)/maxPointDic['A1'])*7.5 + (a2Map.get(key,0)/maxPointDic['A2'])*7.5 + (ProjectMap.get(key,0)/maxPointDic['PR'])*25 + (test1Map.get(key,0)/maxPointDic['T1'])*30 + (test2Map.get(key,0)/maxPointDic['T2'])*30

        grade = getAssociatedLetterGrade(int(numericTotal),passFailGrade)

        studentinfo['ID'] = key
        name = value.split(',')
        studentinfo['LN'] = name[0].strip()
        studentinfo['FN'] = name[1].strip()
        studentinfo['A1'] = a1Map.get(key," ")
        studentinfo['A2'] = a2Map.get(key," ")
        studentinfo['PR'] = ProjectMap.get(key," ")
        studentinfo['T1'] = test1Map.get(key," ")
        studentinfo['T2'] = test2Map.get(key," ")
        studentinfo['GR'] = int(numericTotal)
        studentinfo['FL'] = grade

        spreadsheet.append(studentinfo)

    spreadsheet.sort(key=operator.itemgetter('ID'))

    return spreadsheet

def getAssociatedLetterGrade(numerictotal,passFailGrade):

    grade = ''

    remainingTotal = (100-passFailGrade)
    rangeDifferent = int((remainingTotal)/7)

    minC_range = passFailGrade + 1
    maxC_range = passFailGrade + rangeDifferent

    minB_minus_range = maxC_range + 1
    maxB_minus_range = maxC_range + rangeDifferent

    minB_range = maxB_minus_range + 1
    maxB_range = maxB_minus_range + rangeDifferent

    minB_plus_range = maxB_range + 1
    maxB_plus_range = maxB_range + rangeDifferent

    minA_minus_range = maxB_plus_range + 1
    maxA_minus_range = maxB_plus_range + rangeDifferent

    minA_range = maxA_minus_range + 1
    maxA_range = maxA_minus_range + rangeDifferent

    minA_plus_range = maxA_range + 1
    maxA_plus_range = 100

    if numerictotal <= passFailGrade:
        grade = 'F'
    elif (minC_range <= numerictotal <= maxC_range):
        grade = 'C'
    elif (minB_minus_range <= numerictotal <= maxB_minus_range):
        grade = 'B-'
    elif (minB_range <= numerictotal <= maxB_range):
        grade = 'B'
    elif (minB_plus_range <= numerictotal <= maxB_plus_range):
        grade = 'B+'
    elif (minA_minus_range <= numerictotal <= maxA_minus_range):
        grade = 'A-'
    elif (minA_range <= numerictotal <= maxA_range):
        grade = 'A'
    elif (minA_plus_range <= numerictotal <= maxA_plus_range):
        grade = 'A+'

    return grade

def printSpreadsheet(spreadsheet):

    print('{:<5}\t{:<6}\t{:<6}\t{:<2}\t{:<2}\t{:<2}\t{:<2}\t{:<2}\t{:<2}\t{:<2}'.format("ID", "LN", "FN", "A1", "A2", "PR", "T1", "T2", "GR", "FL"))
    for info in spreadsheet:
        print('{:<5}\t{:<6}\t{:<6}\t{:<2}\t{:<2}\t{:<2}\t{:<2}\t{:<2}\t{:<2}\t{:<2}'.format(info['ID'],info['LN'],info['FN'],info['A1'],info['A2'],info['PR'],info['T1'],info['T2'],info['GR'],info['FL']))

    return
