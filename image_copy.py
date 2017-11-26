import os
import sys
import shutil

def move_jpgfile(dest_path,current_path):
	list_file=[]
	for file in os.listdir(current_path):
		file_abs_path=os.path.join(current_path,file)
		if os.path.isfile(file_abs_path):
			if os.path.splitext(file)[1].lower() in ('.png','.PNG'):
				file_path=os.path.join(current_path,file)				
				try:
					shutil.move(file_path,dest_path)
					list_file.append(file_path)
				except Exception as e:
					print(e)
	return list_file
				
def get_child(current_path):
	child_directory=[]
	for directory in os.listdir(current_path):
		full_directory=os.path.join(current_path,directory)
		if os.path.isdir(full_directory):
			child_directory.append(full_directory)
	return child_directory		

destn_path=input("enter destination path")
source_path=[input("Input path of the source")]
queue = []
queue.extend(source_path)
list_file=[]
while not len(queue)==0:
	current_path = queue[0]
	list_file.extend(move_jpgfile(destn_path,current_path))
	queue.remove(queue[0])
	child=get_child(current_path)
	queue.extend(child)

print("Moved files list: ", list_file)

	    
