# Automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion. 
# Usage : DirectoryRename.py “Demo” “.txt” “.doc” 
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.



from sys import *;
import os;



def Display(path,old_extension,new_extension):
	
	if not(os.path.isabs(path)):
		path = os.path.abspath(path);

	exist = os.path.isdir(path);

	if exist :

		for folder,subfolder,files in os.walk(path) :
			print("\nCurrent folder is :",folder);

			for fil in files :
				fil = os.path.join(folder,fil);
				name,ext = os.path.splitext(fil);

				if ext == old_extension :
					os.rename(fil,name+new_extension);

	else :
		print("There is no file with extension :",extension);


def main():

	print("******** Script by Vishwajeet Patil ********");
	print("Application name :",argv[0]);

	if len(argv)<2 or len(argv)>4 :
		print("Enter valid number of arguments");
		exit();

	if argv[1].lower == "-h":
		print("This script is rename the extension");

	if argv[1].lower == "-u":
		print("How to use :-");
		print("Run it as : python application_file directory_path old_extension new_extension");
		print("Example : python Assignment10_1.py New .txt .py");
	
	Display(argv[1],argv[2],argv[3]);



if __name__ == "__main__" :
	main();