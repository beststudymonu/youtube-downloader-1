#/usr/bin env python3.x
# _*_ Coding UTF-8 _*_
'''
--------------------
Author : Edi Garsell
Youtube: Edi ID
--------------------
Note:
no need to RECODE our script
Just use it. YES
once again there is no need to RECODE
thank you...
--------------------
'''
import getpass
import sys
import time
import os
from time import sleep

def info(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(10. /100)
logo = ('''
	+-+-+-+-+-+-+-+-+-+-+-+-+
	| YOUTUBE | DOWNLOADER  |
	+-+-+-+-+-+-+-+-+-+-+-+-+
''')
menu = ('''
-----------------
[+] MENU:
-----------------
[1] Youtube
[0] Exit
-----------------
[?] Enter Number:
''')
def youtuber():
	try:
		print ('[+] Please Enter a valid Video URL:')
		sleep(1)
		url = input('=>: ')
		os.system('cls')
		print (logo)
		print ('-------------------')
		print ('[+] MENU:          ')
		print ('-------------------')
		print ('[1] Download MP3   ')
		print ('[2] Download MP4   ')
		print ('-------------------')
		print ('[?] Enter Number:  ')
		print ('')
		download = input('root@Edi ID~# ')
		os.system('cls')
		print ('')
		print ('-------------------------------------------------')
		print ('           Download in process                   ')
		print ('-------------------------------------------------')
		def mp3():
			os.system('youtube-dl {0} --extract-audio --audio-format mp3 -o /Audio/%(title)s.%(ext)s'.format(url))
			print ('-------------------------------------------------')
			print ('Download Audio from Youtube Successfully         ')
			print ('')
			Stop()
		def mp4():
			os.system('youtube-dl -f mp4 {0} -o Video/%(title)s.%(ext)s'.format(url))
			print ('-------------------------------------------------')
			print ('Download Video from Youtube Successfully         ')
			print ('')
			Stop()
		if '1' in download:
			mp3()
		elif '2' in download:
			mp4()
		else:
			pass
	except KeyboardInterrupt:
		sys.exit()

def ex():
	try:
		print ('-----------------------')
		info ('Thank you!')
		sleep(2)
		info ('have used this script')
		sleep(2)
		info ('hope this helps.')
		sleep(3)
		Stop()
	except KeyboardInterrupt:
		sys.exit()

def Stop():
    back = input('[?] Want to Download Again [Y/n] ')
    if back[0].upper() == 'N':
        sys.exit()
    else:
        os.system('cls')
        print (logo)
        youtuber()

try:
	os.system('cls')
	print (logo)
	print (menu)
	choose = input('root@Edi ID~# ')
	if choose == '1':
		youtuber()
	elif choose == '0':
		ex()
	else:
		print ('-----------------------')
		print ('[!] Wrong Input')
		sleep(3)
		os.system('python downloader.py')
except KeyboardInterrupt:
	print ('')
