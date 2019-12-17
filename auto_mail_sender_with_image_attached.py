import sys;
import urllib.request;
import smtplib;
from email.message import EmailMessage;
import imghdr;



def SendMail(gmail_user,gmail_pass):
	
	send_from = gmail_user;
	send_to = ['svishpatil@gmail.com','np52622@gmail.com','prakashtiwari468@gmail.com'];

	try :

		msg = EmailMessage();
		msg['From'] = send_from;
		msg['To']	= send_to;
		msg['subject'] = 'Check the images .....';
		msg.set_content('Done by python script');

		total = ['joker.jpg','joker2.png'];

		for file in total :

			f = open(file,'rb');
			file_data = f.read()	
			file_type = imghdr.what(f.name);
			file_name = f.name;

			msg.add_attachment(file_data , maintype='image' , subtype=file_type , filename=file_name);

		server = smtplib.SMTP_SSL('smtp.gmail.com',465);
		server.ehlo();
		server.login(gmail_user,gmail_pass);
		server.send_message(msg);

		print('Mail successfully send');

	except Exception as E:
		print('Unable to send message :',E);



def is_connect():
	
	try :
		urllib.request.urlopen('https://www.google.com/',timeout=1);
		return True;
	except urllib.request.URLError as Error:
		return False;



def main():

	print("******** Script by Vishwajeet Patil ********");
	print("Apllication name :",sys.argv[0]);

	connect = is_connect;

	try :

		if connect:
			print('Connection to internet establish');

			gmail_user = 'svishpatil@gmail.com';
			gmail_pass = 'JEETPATIL2609';

			SendMail(gmail_user,gmail_pass);

		else:
			print('You are not connected to internet , Please check your connection !!');

	except Exception as exe:
		print(exe);
	


if __name__ == '__main__':
	main();