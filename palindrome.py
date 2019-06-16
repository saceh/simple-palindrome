import sys

# function which return reverse of a string 
def reverse(s): 
	return s[::-1] 

def isPalindrome(s): 
	# Calling reverse function 
	rev = reverse(s) 

	# Checking if both string are equal or not 
	if (s == rev): 
		return True
	return False


# Driver code 
s = sys.argv[1]
ans = isPalindrome(s) 

if ans == 1: 
	print("Provided string \"" + s + "\" is palindrome") 
else: 
	print("Provided string \"" + s + "\" is not palindrome") 

