#proj1.py
#chesleah kribs 
#1/28/2019

import numpy


C = numpy.empty([0,7], dtype=numpy.int)

with open("proj1_testdata") as f:
	for line in f.readlines():
		line = line.strip()
		words = line.split("     ")
		code_word = numpy.empty(0)
		for word in words:
			code_word = numpy.append(code_word, int(word))
		#print(words)
		C = numpy.append(C, [code_word], 0)
print(C[0])

# the parity check matrix 
parityarr = numpy.asarray([[1,0,1],[1,1,1],[1,1,0],[0,1,1],[1,0,0],[0,1,0],[0,0,1]])

error = numpy.mod(numpy.matmul(C, parityarr), 2)
print(error[0])
for i in range(0, error.shape[0]):
	for j in range(0, parityarr.shape[0]):
		if numpy.array_equal(error[i], parityarr[j]):
			C[i][j] = 1 - C[i][j]
			break

error = numpy.mod(numpy.matmul(C, parityarr), 2)
print(error)

C = C[:,:4].reshape(C.shape[0]/2, 8)
print C.shape
phrase = []
bit_list = C.tolist()
for bits in bit_list:
	bits = [int(i) for i in bits]
	chars = []
	for b in range(len(bits) / 8):
		byte = bits[b*8:(b+1)*8]
		chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
	phrase.append(''.join(chars))
final = [str(f) for f in phrase]
print ''.join(final)




# you may also want to remove whitespace characters like `\n` at the end of each line



