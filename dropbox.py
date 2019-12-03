import os
import dropbox

def Upload(file):
	client = dropbox.Dropbox('Your Access Token')
	folder = '/Python/Dropbox/'

	for f in file:
		with open('f', 'rb') as ifile:
			filename = os.path.basename(f)
			client.files_upload(ifile.read(), folder + filename)
			print("\n"+filename+" Upload successfully to : "+folder)


if __name__ == '__main__':
	filelist = []
	print("\n Select the files to upload. Enter done once the files are selected \n")
	while True:
		fileinput = input('Filename: ')

		if fileinput.lower() != "done"
			filelist.append(fileinput)
		else:
			Upload(filelist)
			break