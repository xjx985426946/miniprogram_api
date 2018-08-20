#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/15 11:45
# @Author  : yixiong

#! /usr/bin/env python
# encoding=utf-8

import xlrd
import os

# 获取login.xls的文件路径
Dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
excelDir = Dir + "//config_testcase//"+"Case.xls"
rows_list = []
cols_list = []

def open_excel(excelDir):
    try:
        data = xlrd.open_workbook(excelDir,'a+')
        return data
    except Exception as e:
        print(str(e))

def readExcel(sheetName):
    data=open_excel(excelDir)
    table = data.sheet_by_name(sheetName)
    nrows = table.nrows
    for i in range(nrows):
        if table.row_values(i)[0] != u'Test_Case':
            rows_list.append(table.row_values(i))
    return rows_list

def readExcelCol(sheetName):
    data = open_excel(excelDir)
    table = data.sheet_by_name(sheetName)
    nrows = table.nrows
    for i in range(nrows):
        table.row_values(i)
        cols_list.append(table.row_values(i))
    return cols_list

if __name__=="__main__":
    readExcel("case")
    # readExcelCol("testcase")