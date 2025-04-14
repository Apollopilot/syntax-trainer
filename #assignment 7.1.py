#assignment 7.1 
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        parts = line.split(":")
        if len(parts) !=2:
            continue
        try:
            number = float(parts[1].strip())
            total += number
            count += 1
        except ValueError:
            continue
if count > 0:
   average=total/count
   print("Average spam confidence:", average)
else:
    print("No valid 'X-DSPAM-Confidence'lines found.")