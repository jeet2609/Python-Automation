# automation script which accept directory name and file extension from user.
# Display all files with that extension. 
# Usage : DirectoryFileSearch.py “Demo” “.txt” 
# Demo is name of directory and .txt is the extension that we want to search. 



from sys import *;
import os;



def Display(path,extension):
	
	if not(os.path.isabs(path)):
		path = os.path.abspath(path);

	exist = os.path.isdir(path);

	if exist :

		for folder,subfolder,files in os.walk(path) :
			print("\nCurrent folder is :",folder);

			for fil in files :
			#	name,ext = os.path.splitext(fil);
			#	if ext == extension :
			#		print(fil);

				if extension in fil :
					print(fil);

	else :
		print("There is no file with extension :",extension);


def main():

	print("******** Script by Vishwajeet Patil ********");
	print("Application name :",argv[0]);

	if len(argv)<2 or len(argv)>3 :
		print("Enter valid number of arguments");
		exit();

	if argv[1].lower == "-h":
		print("This script is for display only files that have user entered extension");

	if argv[1].lower == "-u":
		print("How to use :-");
		print("Run it as : python application_file directory_path extension");
		print("Example : python Assignment10_1.py New .txt");
	
	Display(argv[1],argv[2]);



if __name__ == "__main__" :
	main();