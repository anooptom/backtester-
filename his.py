import pyautogui
import time

def fun():
	pyautogui.click(767,747);
	for i in range(75):
     		pyautogui.press('left')

t=15
day=4

while t>=1:
	pyautogui.click(837,2); #nifty
	fun();
	pyautogui.hotkey('win', 'printscreen')
	time.sleep(1)
	pyautogui.click(954,1064); #file explorer
	time.sleep(0.5)
	pyautogui.click(865,195);
	pyautogui.hotkey('ctrl', 'x')

	if(day ==5):
		pyautogui.click(103,786) #fri
		pyautogui.hotkey('ctrl', 'v')

	elif (day ==4):
		
		pyautogui.click(89,664) #thru
		pyautogui.hotkey('ctrl', 'v')

	elif(day ==3):
		
		pyautogui.click(98,535) #wed
		pyautogui.hotkey('ctrl', 'v')

	elif (day ==2):		
		
		pyautogui.click(101,395) #tue
		pyautogui.hotkey('ctrl', 'v')
		
	elif(day ==1):
		
		pyautogui.click(92,924) #mon
		pyautogui.hotkey('ctrl', 'v')
	time.sleep(0.5)
	pyautogui.click(85,145); #screenshot
	time.sleep(0.5)
	pyautogui.click(954,1064); #file explorer	
	

	
	pyautogui.click(624,2); #fin
	fun();
	pyautogui.hotkey('win', 'printscreen')
	time.sleep(1)
	pyautogui.click(954,1064); #file explorer
	time.sleep(0.5)
	pyautogui.click(865,195);
	pyautogui.hotkey('ctrl', 'x')

	if(day ==5):
		pyautogui.click(101,756) #fri
		pyautogui.hotkey('ctrl', 'v')

	elif (day ==4):
		
		pyautogui.click(76,628) #thru
		pyautogui.hotkey('ctrl', 'v')

	elif(day ==3):
		
		pyautogui.click(94,498) #wed
		pyautogui.hotkey('ctrl', 'v')

	elif (day ==2):		
		
		pyautogui.click(92,377) #tue
		pyautogui.hotkey('ctrl', 'v')
		
	elif(day ==1):
		
		pyautogui.click(97,892) #mon
		pyautogui.hotkey('ctrl', 'v')
	time.sleep(0.5)
	pyautogui.click(85,145); #screenshot
	time.sleep(0.5)
	pyautogui.click(954,1064); #file explorer	



	pyautogui.click(373,2); #bn
	fun();
	pyautogui.hotkey('win', 'printscreen')
	time.sleep(1);
	pyautogui.click(954,1064); #file explorer
	time.sleep(0.5);
	pyautogui.click(865,195);
	pyautogui.hotkey('ctrl', 'x')

	if(day ==5):
		pyautogui.click(95,730) #fri
		pyautogui.hotkey('ctrl', 'v')
		day=4

	elif (day ==4):
		
		pyautogui.click(98,599) #thru
		pyautogui.hotkey('ctrl', 'v')
		day=3

	elif(day ==3):
		
		pyautogui.click(104,476) #wed
		pyautogui.hotkey('ctrl', 'v')
		day=2

	elif (day ==2):		
		
		pyautogui.click(109,341) #tue
		pyautogui.hotkey('ctrl', 'v')
		day=1
		
	elif(day ==1):
		
		pyautogui.click(96,860) #mon
		pyautogui.hotkey('ctrl', 'v')
		day=5
	time.sleep(0.5)
	pyautogui.click(85,145); #screenshot
	time.sleep(0.5)
	pyautogui.click(954,1064); #file explorer	
	
	t-=1;	

