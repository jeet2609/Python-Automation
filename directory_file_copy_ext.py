# Design automation script which accept two directory names and one file extension.
# Copy all files with the specified extension from first directory into second directory. Second directory should be created at run time. 
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe” 
# Demo is name of directory which is existing and contains files in it.
# We have to create new Directory as Temp and copy all files with extension .exe from Demo to Temp. 



from sys import *;
import os;
import shutil



def CopyFiles(source,destination,ext):
	
	if not(os.path.isabs(source)):
		os.path.abspath(source);

	if not(os.path.isabs(destination)):
		os.path.abspath(destination);

	if os.path.exists(destination):
		print("\nDestination directory already present !!");
		print("Please eneter valid destination directory ");
		exit();

	if not(os.path.exists(source)):
		print("\nEnter Valid Source directory");
		exit();

	os.mkdir(destination);
	files = os.listdir(source);

	for fil in files:
		path = os.path.join(source,fil);
		if os.path.isfile(path):														# to check it is file or folder. If we dont write this then we will get error permission dennied due to present of subfolders.
			if ext in fil:
				shutil.copy(path,destination);
		


def main():

	print("******** Script by Vishwajeet Patil ********");
	print("Application name :",argv[0]);

	if len(argv)<2 or len(argv)>4 :
		print("Enter valid number of arguments");
		exit();

	if argv[1].lower == "-h":
		print("This script is for display only files that have .txt extension");

	if argv[1].lower == "-u":
		print("How to use :-");
		print("Run it as : python application_file Source__Directory Destination_Directory extension");
		print("Example : python Assignment10_1.py Source Destination .txt");
	
	CopyFiles(argv[1],argv[2],argv[3]);



if __name__ == "__main__" :
	main();