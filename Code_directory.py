import os





path = "//storage//emulated//0"


Music = []
Music1 = []
for root, dirs, files in os.walk(path):
	for file in files:
		if file.endswith(".mp3") or file.endswith(".m4a"):
			Music.append( os.path.join(root, file) )
			Music1.append(file)
					
x = Music[89]

path_dir = []
for root, dirs, files in os.walk(path):
	for dir in dirs:
		root_dir= os.path.join(root, dir)
		for v in os.listdir(root_dir):
			if v.endswith(".mp3") or v.endswith(".m4a"):
				if root_dir in path_dir:
					pass
				else:
					path_dir.append(root_dir)
		
print(len(path_dir))	

		
def get_image_from_path(file_path, album_cover=False):
    try:
        metadata_retriever = MediaMetadataRetriever()
        metadata_retriever.setDataSource(file_path)
        img_byte = metadata_retriever.getEmbeddedPicture()
        if img_byte:
            with open(img_file_path, 'wb') as f:
                f.write(bytearray(img_byte.png))
                print(img_byte.png)
                
                
            return img_file_path

    except Exception:  # NOQA
        pass
    return "img/cd.png"
    
			
print(get_image_from_path(x) )