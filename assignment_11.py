#assignment_11.4
import re
import urllib.request

# Define URL
url = 'http://py4e-data.dr-chuck.net/regex_sum_2202376.txt'

# Fetch and decode data
response = urllib.request.urlopen(url)
contents = response.read().decode()

# Find numbers, convert to integers, and sum
numbers = re.findall('[0-9]+', contents)
int_numbers = [int(num) for num in numbers]
total_sum = sum(int_numbers)

# Display result
print("Sum:", total_sum)