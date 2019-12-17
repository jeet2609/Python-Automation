import schedule;
import time;
import datetime;



def fun_Minute():
	print("\nCurrent time is :");
	print(datetime.datetime.now());
	print("Schedule executed after minute \n");



def fun_Hour():
	print("\nCurrent time is :");
	print(datetime.datetime.now());
	print("Schedule executed after Hour \n");



def fun_Day():
	print("\nCurrent time is :");
	print(datetime.datetime.now());
	print("Schedule executed after Day \n");



def fun_Afternoon():
	print("\nCurrent time is :");
	print(datetime.datetime.now());
	print("Schedule executed at 12 \n");



def main():

	print("******** Script by Vishwajeet Patil ********");
	print("Python job schedular");
	print(datetime.datetime.now());

	schedule.every(1).minutes.do(fun_Minute);
	schedule.every().hour.do(fun_Hour);
	schedule.every().day.at("00:00").do(fun_Afternoon);
	schedule.every().saturday.do(fun_Day);
	schedule.every().sunday.at("23:40").do(fun_Day);

	while True :
		schedule.run_pending();
		time.sleep(1);
	


if __name__ == "__main__" :
	main();