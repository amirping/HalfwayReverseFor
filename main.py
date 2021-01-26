def revOptimal(inData):
	s = ""
	for i in range((len(inData))//2):
		s = s[:len(s)//2] + inData[(len(inData)-1)-i] + inData[i] + s[len(s)//2:]
	if(len(inData) % 2) != 0:
		s = s[:len(s)//2] + inData[len(inData)//2] + s[len(s)//2:]
	return s

tests = [
	"",
	"a",
	"ab",
	"abc",
	"abcd",
	"abcde"
	"ftbollfizw",
	"can you reverse me"
]

for x in tests: 
	print("{} -> {}".format(x,revOptimal(x)))