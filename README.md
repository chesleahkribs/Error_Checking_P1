# Error_Checking_P1
Recovering data that was corrupted by errors with a (7,4) Hamming code. 

Chesleah Kribs 
In this project, you are asked to recover the data that have been corrupted by errors, where the data is coded according to the (7, 4) Hamming code we discussed in the class.

The corrupted data file can be found on Canvas under files named proj1_testdata. In the file, each line has 7 binary numbers, which is originally a codeword, but with one random bit flipped.

You should implement the decoding program that decodes each line in the input file into 4 bits. You can join every 2 lines of the decoding results into one byte, which can be interpreted as an ascii code, and print out the ascii string.
