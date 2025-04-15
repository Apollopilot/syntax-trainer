#Assignment 7.1.1 a little more refined
fname = input("Please enter file name:")
try: # opens the file name
    fh=open(fname)
except FileNotFoundError: # if file doesn't exist, this block catches the error. Error Handling
    print("File cannot be opened:", fname)
    quit()

count = 0 # to keep track of how many lines match what looking for
total = 0.0 # add up all float numbers

for line in fh: # starts loop that reads the file line by line
    if line.startswith("X-DSPAM-Confidence:"): #check if line starts with "", if not, skip line
        parts = line.split(":") #use split() instead of find(), which is cleaner and easier to read
        if len(parts) !=2: #safety check. if split didn't give exactly 2 parts, somethings wrong - skip it
            continue
        try:
            number = float(parts[1].strip()) #try float() in case there's some unexpected garbage after :. .strip() removes extra spaces. This block is wrapped in a try: in case something goes wrong
            total += number # add number to our running total
            count += 1 # increase our count of how many valid lines found
        except ValueError: # if float() fails (bad format, etc), we skip line
            continue
if count >0: # if we find any valid lines, we compute the average and print
    average = total/count
    print("Average spam confidence:", average)
else: # if no lines matched, we inform user
    print("No valid 'X-DSPAM-Confidence' lines found") 