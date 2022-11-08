 # Write a Python function that takes a list of words and returns the length of the longest one.

def longest_Length(x):
	max1 = len(x[0])
	temp = x[0]


	for i in x:
		if(len(i) > max1):

			max1 = len(i)
			temp = i

	print("longest length is:", temp,
		"length is ", max1,)

x = ["Pyhton", "JAVA", "C++", ".Net Asp"]
longest_Length(x)

