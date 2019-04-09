import numpy as np



def main():

	train_file= open('train_various_patches-rotation.txt')
	test_file= open('test_various_patches-rotation.txt')
	validation_file= open('validation_various_patches-rotation.txt')

	tr= open('PatchFiles/train.txt','w')
	ts= open('PatchFiles/test.txt','w')
	val= open('PatchFiles/val.txt','w')
	
	train_line= train_file.readline()
	y=np.random.randint(0,512)
	dy=np.random.randint(0,512)
	train_line=train_line[0:-1]+"#"+str(y)+"#"+str(dy)
	print(train_line)	
	tr.write(train_line+'\n')

	test_line=test_file.readline()
	y=np.random.randint(0,512)
	dy=np.random.randint(0,512)
	test_line=test_line[0:-1]+"#"+str(y)+"#"+str(dy)
	print(test_line)
	ts.write(test_line+'\n')
	
	validation_line=validation_file.readline()
	y=np.random.randint(0,512)
	dy=np.random.randint(0,512)
	validation_line=validation_line[0:-1]+"#"+str(y)+"#"+str(dy)
	print(validation_line)
	val.write(validation_line+'\n')
	
	while train_line:
		train_line=train_file.readline()
		if not train_line:
			break
		y=np.random.randint(0,512)
		dy=np.random.randint(0,512)
		train_line=train_line[0:-1]+"#"+str(y)+"#"+str(dy)
		print(train_line)
		tr.write(train_line+'\n')	

	while test_line:
		test_line=test_file.readline()
		if not test_line:
			break
		y=np.random.randint(0,512)
		dy=np.random.randint(0,512)
		test_line=test_line[0:-1]+"#"+str(y)+"#"+str(dy)
		print(test_line)	
		ts.write(test_line+'\n')

	while validation_line:
		validation_line=validation_file.readline()
		if not validation_line:
			break
		y=str(np.random.randint(0,512))
		dy=str(np.random.randint(0,512))
		validation_line=validation_line[0:-1]+"#"+y+"#"+dy
		print(validation_line)
		val.write(validation_line+'\n')






















if __name__=="__main__":
	main()