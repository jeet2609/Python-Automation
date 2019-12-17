# Automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID, Username.
# After creating log file send that log file to the specified mail. 
# Usage : ProcInfoLog.py Demo svishpatil@gmail.com
# Demo is name of Directory.
# svishpatil@gmail.com is the mail id.




from sys import *;
import sys;
import psutil;
import os;
import urllib.request;
import smtplib;
from email.message import EmailMessage;
import time;



def CreateLogFile(path):
	
	if not(os.path.isabs(path)):
		path = os.path.abspath(path);

	if not(os.path.exists(path)):
		os.mkdir(path);

	process = list();
	for pobj in psutil.process_iter():

		try:
			pinfo = pobj.as_dict (attrs = ['pid','name','username']);
			process.append(pinfo);

		except psutil.NoSuchProcess:
			pass;

	file = open(os.path.join(path,'log.txt'),'w');																# create file in user entered directory.
	file.write("******************************** Process log file ******************************** \n\n");
	for i in process:
		file.write(str(i) + '\n');

	print("Log file created");
	file.close();



def is_connected():
	
	try :
		urllib.request.urlopen('https://www.google.com/',timeout=2);
		return True;
	
	except urllib.request.URLError as err:
		return False;



def SendMail(gmail_user,gmail_pass,send_to):
	
	send_from = gmail_user;

	try:
		msg = EmailMessage();
		msg['From'] = send_from;
		msg['To']	= send_to;
		msg['Subject'] = 'Log file of process running';
		ctime = time.ctime();
		msg.set_content('File created at %s' %ctime);

		f = open('Demo/log.txt','rb');
		file_data = f.read();
		file_name = f.name;

		msg.add_attachment(file_data , maintype='application' , subtype='octet-stream' , filename=file_name);

		server = smtplib.SMTP_SSL('smtp.gmail.com',465);
		server.ehlo();
		server.login(gmail_user,gmail_pass);
		server.send_message(msg);

	except Exception as Exe:
		print('Unable to send message :',Exe);


def main():
	
	print("******** Script by Vishwajeet Patil *******");
	print("Application name :",sys.argv[0]);


	if len(sys.argv)<2 or len(sys.argv)>3 :
		print("Enter valid number of arguments");
		exit();

	if sys.argv[1] == "-h":
		print("This script is to create log file of running process and send mail");
		exit();

	if sys.argv[1] == "-u":
		print("How to use :-");
		print("Run it as : python application_file Directory Recipient_mail");
		print('Directory : The directory where user log file will be created');
		print('Recipient_mail : The Recipient mail-id');
		print("Example : python application_name.py Data svishpatil@gmail.com");
		exit();

	try :
		CreateLogFile(sys.argv[1]);

		connected = is_connected();
		if connected :
			gmail_user = 'svishpatil@gmail.com';
			gmail_pass = '----------';

			SendMail(gmail_user,gmail_pass,sys.argv[2]);

	except Exception as E:
		print('Error occured :',E);



if __name__ == "__main__":
	main();