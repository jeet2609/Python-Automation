import sys;
import urllib.request
import smtplib;
from email.message import EmailMessage;



def is_connected():
	
	try :
		urllib.request.urlopen('https://www.google.com/',timeout=2);
		return True;
	
	except urllib.request.URLError as err:
		return False;



def mail_sender(gmail_user,gmail_pass):
	
	sent_from = gmail_user;
	send_to = ['np52622@gmail.com','svishpatil@gmail.com','omkarsasane1996@gmail.com'];

	try:
		msg = EmailMessage();																	# email msg object is created which contains all ie from,to,subject and body
		msg['From'] =	sent_from;
		msg['To'] 	=	send_to;
		msg['Subject'] = 'This is auto genereted mail';
		msg.set_content('Done by python script');

		server = smtplib.SMTP_SSL('smtp.gmail.com',465);
		server.ehlo();
		server.login(gmail_user,gmail_pass);
		server.send_message(msg);

		print('Mail sended successfully \n');

	except Exception as E:
		print('Unable to send message !!',E);



def main():

	print("******** Script by Vishwajeet Patil ********");
	print("Apllication name :",sys.argv[0]);

	try :
		connected = is_connected();

		if connected :
				gmail_user = 'svishpatil@gmail.com';
				gmail_pass = 'JEETPATIL2609';

				mail_sender(gmail_user,gmail_pass);

		else :
			print('You are not connected to internet , Please check your connection !!');

	except Exception as exe:
		print(exe);



if __name__ == '__main__' :
	main();