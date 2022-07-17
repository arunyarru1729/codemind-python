def convert_to_words(num):
	l = len(num)
	
	ones = ["zero", "one", "two", "three",
					"four", "five", "six", "seven",
					"eight", "nine"]
	teens = ["", "ten", "eleven", "twelve",
				"thirteen", "fourteen", "fifteen",
				"sixteen", "seventeen", "eighteen",
				"nineteen"]
	tens= ["", "", "twenty", "thirty", "forty",
					"fifty", "sixty", "seventy", "eighty",
					"ninety"]
	hundreds = ["hundred", "thousand"]
	if (l == 1):
		print(ones[ord(num[0]) - 48])
		return
	x = 0
	while (x < len(num)):
		if (l >= 3):
			if (ord(num[x]) - 48 != 0):
				print(ones[ord(num[x]) - 48],
					end=" ")
				print(hundreds[l - 3], end=" ")

			l -= 1
		else:
			if (ord(num[x]) - 48 == 1):
				sum = (ord(num[x]) - 48 +
					ord(num[x+1]) - 48)
				print(teens[sum])
				return
			elif (ord(num[x]) - 48 == 2 and
				ord(num[x + 1]) - 48 == 0):
				print("twenty")
				return
			else:
				i = ord(num[x]) - 48
				if(i > 0):
					print(tens[i], end=" ")
				else:
					print("", end="")
				x += 1
				if(ord(num[x]) - 48 != 0):
					print(ones[ord(num[x]) - 48])
		x += 1
a=input()
convert_to_words(a)