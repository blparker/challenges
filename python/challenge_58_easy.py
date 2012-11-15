import sys
import math

def main():
	toConvert = float(sys.argv[1])	# The number we are converting
	base = int(sys.argv[2])			# To base

	if base < 2 or base > 36:
		raise Exception('Base must be between 2 and 36')
	
	# New base list
	nums = buildBaseNumList(base)

	result = []
	
	res = toConvert / base				# Step 1: Divide number by base
	rem = int((res - int(res)) * 16)	# Step 2: Get remainder and multiple by base
	res = math.floor(res)				# Step 3: Take the ceiling of res
	result.append(str(nums[rem]))		# Step 4: Convert remainder into base
	# Repeat until 'res' is less than 1

	while (res >= 1):
		res = res / base
		rem = int((res - int(res)) * base)
		result.append(str(nums[rem]))
	
	result.reverse()
	print toConvert, 'in base', base, '=', (''.join(result))
	

# Build our base list
def buildBaseNumList(base):
	nums = []
	for i in range(0, base):
		if i >= 10:
			nums.append(chr(i + 55))	# 55 represents the ascii offset (e.g., add 10 + 55 to get 'A')
		else:
			nums.append(i)
	
	return nums

# Main method to kick things off
if __name__ == '__main__':
	main()

