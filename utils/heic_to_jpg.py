import pyheif
import PIL
import os
import exifread
import io
from PIL import Image
import whatimage

def read_heic(path: str):
	with open(path, 'rb') as file:
		image = pyheif.read_heif(file)
		for metadata in image.metadata or []:
			if metadata['type'] == 'Exif':
				fstream = io.BytesIO(metadata['data'][6:])

	# now just convert to jpeg
	pi = PIL.Image.open(fstream)
	pi.save("new_boxes/"+path+".jpg", "JPEG")

	# or do EXIF processing with exifread
	tags = exifread.process_file(fstream)
	return

def decodeImage(filename, bytesIo):
	image_name = filename.split('.')[0]
	image_name = image_name.split('/')[1]
	image_type = filename.split('.')[1]
	if image_type in ['heic', 'HEIC']:
		i = pyheif.read_heif(bytesIo)

		#  # Extract metadata etc
		# for metadata in i.metadata or []:
		# 	if metadata['type']=='Exif':
		# 		 # do whatever

		 # Convert to other file format like jpeg
		s = io.BytesIO()
		pi = Image.frombytes(
				mode=i.mode, size=i.size, data=i.data)

		writepath = image_name+".jpg"

		# try:
		#     fp = open(writepath)
		# except IOError:
		#     # If not exists, create the file
		#     fp = open(writepath, 'w')

		# if not os.path.exists(writepath):
		# 	os.mknod(writepath)

		# mode = 'a' if os.path.exists(writepath) else 'w+'
		# f = open(writepath, 'wt')
		# with open(writepath, mode) as save_loc:
		pi.save(writepath, format="jpeg")
	return

if __name__ == '__main__':
	path = 'boxes/'

	for file in os.listdir(path):
		print('.')
		filename = path+file
		with open(filename, 'rb') as f:
			decodeImage(filename=filename, bytesIo=f)
