# Automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt.
# Log.txt file should be created into current directory. 
# Usage : DirectoryDusplicate.py “Demo” 
# Demo is name of directory.



from sys import *;
import os;
import hashlib;



def hashfile(path, blocksize = 1024):
	afile = open(path,'rb');
	hasher = hashlib.md5();
	buf = afile.read(blocksize);

	while len(buf) > 0:
		hasher.update(buf);
		buf = afile.read(blocksize);

	afile.close();

	return hasher.hexdigest();



def DisplayChecksum(path):
	flag = os.path.isabs(path);

	if flag == False :
		path = os.path.abspath(path);

	exists = os.path.isdir(path);

	if exists :

		dups = {};
		for dirName, subdirs, fileList in os.walk(path):

			for filen in fileList:
				path = os.path.join(dirName,filen);
				file_hash = hashfile(path);

				if file_hash in dups :
					dups[file_hash].append(path);
				else :
					dups[file_hash] = [path];

		return dups;

	else :
		print("Invalid path");



def Duplicate(dict1):
	
	dict1 = list(filter(lambda x : len(x)>1 , dict1.values()));

	file = open('log.txt','w');
	file.write("******************** Duplicate files are ******************** \n");
	for i in dict1 :
		inc = 0;
		for j in i :
			inc = inc+1;

			if (inc > 1) :
				file.write(j + '\n');

	file.close();



def main():
	
	print("******** Script by Vishwajeet Patil *******");
	print("Application name :",argv[0]);

	if len(argv) != 2 :
		print("Error : Invalid Number of elements");
		exit();

	if (argv[1] == "-h") or (argv[1] == "-H") :
		print("This script is used create log file of duplicate files");
		exit();

	if (argv[1] == "-u") or (argv[1] == "-U") :
		print("How to run : python file_name path");
		print("File name : Name of file i.e. DirectoryDusplicate.py");
		print("path : Path of directory");
		print("Example : python DirectoryDusplicate.py Demo ");
		exit();

	try :
		arr = DisplayChecksum(argv[1]);
		Duplicate(arr);

	except ValueError:
		print("Error : Invalid datatype of input");

	except Exception as E:
		print("Error : Inavlid input",E);



if __name__ == "__main__":
	main();