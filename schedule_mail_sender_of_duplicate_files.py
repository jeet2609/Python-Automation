# Automation script which performs following task. 
# Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.
# Create one Directory named as Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted.
# Name of that log file should contains the date and time at which that file gets created.
# Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
# Accept Mail id from user and send the attachment of the log file.
# Mail body should contains statistics about the operation of duplicate file removal.

# DuplicateFileRemoval.py  E:/Data/Demo 50  svishpatil@gmail.com. 
# DuplicateFileRemoval.py      Name of python automation script 
# E:/Data/Demo      Absolute path of directory which may contains duplicate files 
# 50   Time interval of script in minutes 
# svishpatil@gmail.com     Mail ID of the receiver 



import sys;
import os;
import hashlib;
import time;
import schedule;
import urllib.request;
from email.message import EmailMessage;
import smtplib;

inc = 0;



def hashfile(path, blocksize = 1024):
	afile = open(path,'rb');
	hasher = hashlib.md5();
	buf = afile.read(blocksize);

	while len(buf) > 0:
		hasher.update(buf);
		buf = afile.read(blocksize);

	afile.close();

	return hasher.hexdigest();



def DeleteFiles(path , send_to):

	s_time = time.ctime();
	total_files_scanned = 0;
	total_files_deleted = 0;

	if not(os.path.isabs(path)):
		path = os.path.abspath(path);

	if os.path.isdir(path):

		dups = {};
		dup_file = list();
		for folder,subfolder,files in os.walk(path):
			
			for file in files:

				total_files_scanned = total_files_scanned+1;

				file = os.path.join(folder,file);
				chksum = hashfile(file);

				if chksum in dups:
					total_files_deleted = total_files_deleted+1;
					dup_file.append(file);
					os.remove(file);
				else:
					dups[chksum] = [file];

		Create_Log_File(dup_file);

		Send_mail(send_to , s_time , total_files_scanned , total_files_deleted);

	else :
		print('Enter valid path !!\n');
		exit;



def Create_Log_File(del_files):
	
	global inc;
	inc = inc+1;

	if not(os.path.isdir('Marvellous')):
		os.mkdir('Marvellous');

	directory = os.path.abspath('Marvellous');

	f = open('Marvellous/log_file_%d.txt' %inc , 'w');
	f.write('************************** Log file created at %s ************************** \n' %time.ctime());

	if len(del_files)==0 :
		f.write('There are no Duplicate files \n');

	else :
		f.write('Duplicate files are :- \n\n');

		for file in del_files:
			f.write(file + '\n');

	print('Log file created');

	f.close();



def is_connected():
	
	try :
		urllib.request.urlopen('https://www.google.com/',timeout=1);
		return True;
	
	except urllib.request.URLError as err:
		return False;


def Send_mail(send_to , s_time , total_files_scanned , total_files_deleted):
	
	global inc;
	send_from  = gmail_user = 'svishpatil@gmail.com';
	gmail_pass = 'JEETPATIL2609';

	try :

		if is_connected() :
			msg = EmailMessage();
			msg['From'] = send_from;
			msg['To']	= send_to;
			msg['Subject'] = 'This file contains the log file of duplicate files';
			msg.set_content(" Starting time of scanning : {} \nTotal number of files scanned : {} \nTotal number of duplicate files found : {}".format(s_time,total_files_scanned , total_files_deleted));

			f = open('Marvellous/log_file_%d.txt' %inc , 'rb');
			file_data = f.read();
			file_name = f.name;

			msg.add_attachment(file_data , maintype='application' , subtype='octet_stream' , filename=file_name);

			server = smtplib.SMTP_SSL('smtp.gmail.com',465);
			server.ehlo();
			server.login(gmail_user,gmail_pass);
			server.send_message(msg);

			print('Msg send');

		else:
			print('You are offline');

	except Exception as E:
		print('Unable to send message :' , E);



def main():

	print("******** Script by Vishwajeet Patil ********");
	print('Application name :' , sys.argv[0]);

	try :

		schedule.every(int(sys.argv[2])).minutes.do(DeleteFiles , path=sys.argv[1] , send_to=sys.argv[3]);

		while True:
			schedule.run_pending();
			time.sleep(1);

	except Exception as exe:
		print('Enter valid arguments : ',exe);
	


if __name__ == '__main__':
	main();