# Automation script which display information of running processes as its name, PID, Username. 
# Usage : ProcInfo.py 



import sys;
import psutil;



def Display():
	
	for pobj in psutil.process_iter():

		try:
			pinfo = pobj.as_dict (attrs = ['pid','name','username']);

		except psutil.NoSuchProcess:
			pass;

		else:												# else lihala nahi tari pan chalta.
			print(pinfo);



def main():
	
	print("******** Script by Vishwajeet Patil *******");
	print("Application name :",sys.argv[0]);

	try :
		Display();

	except ValueError:
		print("Error : Invalid datatype of input");



if __name__ == "__main__":
	main();