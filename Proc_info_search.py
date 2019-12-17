# Automation script which accept process name and display information of that process if it is running. 
# Usage : ProcInfo.py Notepad 



from sys import *;
import sys;
import psutil;



def Display(Process):
	
	for pobj in psutil.process_iter():

		try:
			pinfo = pobj.as_dict (attrs = ['pid','name','username']);

		except psutil.NoSuchProcess:
			pass;

		else:
		#	if pinfo['name'] == Process:
			if Process in pinfo['name'] :
				print(pinfo);
	    



def main():
	
	print("******** Script by Vishwajeet Patil *******");
	print("Application name :",argv[0]);

	if len(argv) != 2 :
		print("Error : Invalid Number of elements");
		exit();

	if (argv[1] == "-h") or (argv[1] == "-H") :
		print("This script is used to find process is running or not");
		exit();

	if (argv[1] == "-u") or (argv[1] == "-U") :
		print("How to run : python file_name process_name");
		print("File name : Name of file");
		print("process_name : Process name ");
		print("Example : python file_name sublime_text");
		exit();

	try :
		Display(argv[1]);

	except Exception as E:
		print('Error occured :',E);



if __name__ == "__main__":
	main();