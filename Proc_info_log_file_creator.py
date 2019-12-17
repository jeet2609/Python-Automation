# Automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username. 
# Usage : ProcInfoLog.py Demo 
# Demo is name of Directory. 



from sys import *;
import sys;
import psutil;
import os;



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
	    


def main():
	
	print("******** Script by Vishwajeet Patil *******");
	print("Application name :",sys.argv[0]);

	if len(sys.argv) != 2 :
		print('Enter valid number of arguments !!');

	if sys.argv[1] == "-h":
		print("This script is to create log file of running process");
		exit();

	if sys.argv[1] == "-u":
		print("How to use :-");
		print("Run it as : python application_file Directory");
		print('Directory : The directory where user log file will be created');
		print("Example : python application_name.py Data");
		exit();

	try :
		CreateLogFile(sys.argv[1]);

	except Exception as E:
		print('Error occured :',E);



if __name__ == "__main__":
	main();