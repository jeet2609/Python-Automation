# Design automation script which accept two directory names.
# Copy all files from first directory into second directory. Second directory should be created at run time. 
# Usage : DirectoryCopy.py “Demo” “Temp” 
# Demo is name of directory which is existing and contains files in it.
# We have to create new Directory as Temp and copy all files from Demo to Temp. 



from sys import *;
import os;
import shutil



def CopyFiles(source,destination):
	
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
			shutil.copy(path,destination);



def main():

	print("******** Script by Vishwajeet Patil ********");
	print("Application name :",argv[0]);

	if len(argv)<2 or len(argv)>3 :
		print("Enter valid number of arguments");
		exit();

	if argv[1].lower == "-h":
		print("This script is for display only files that have .txt extension");

	if argv[1].lower == "-u":
		print("How to use :-");
		print("Run it as : python application_file Source__Directory Destination_Directory");
		print("Example : python Assignment10_1.py Source Destination");
	
	CopyFiles(argv[1],argv[2]);



if __name__ == "__main__" :
	main();