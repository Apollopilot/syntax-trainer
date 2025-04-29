fname = input("Enter file name: ")
fh = open(fname)

people = [] # List to hold dictionaries
current_email= None

for line in fh:
    line = line.strip()

    # Look for "From" line and exract email
    if line.startswith("From "): 
        words=line.split()
        if len(words) >=2:
            current_email=words[1]

    #Look for confidence score line
    elif line.startswith("X-DSPAM-Confidence:"):
        parts = line.split(":")
        if len(parts) == 2:
            try:
                score = float(parts[1].strip())
                if current_email:
                    person_record = {
                        "email": current_email,
                        "score": score
                    }
                    people.append(person_record)
                    current_email = None # Reseete for next record
            except ValueError:
                continue #Skip bad data

# View list of people and scores
for person in people:
    print(F"{person["email"]} → {person["score"]}") 

#Average Confidence Score
total = 0
for person in people:
    total += person["score"]

average = total / len(people)
print("Average confidence score:", average)