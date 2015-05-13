#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getIntInput():
	num = raw_input('开始猜数字，请输入数字: ')
	while not num.isdigit():
		print('输入错误，请输入数字')
		num = raw_input('开始猜数字，请输入数字: ')
	return int(num)

import random 
num = random.randint(1,100)
inputNumber = getIntInput()
while inputNumber != num:  
	if inputNumber>num:	
		print('大了')
	else:
		print('小了')
	inputNumber = getIntInput()
print('恭喜猜对了，游戏结束')