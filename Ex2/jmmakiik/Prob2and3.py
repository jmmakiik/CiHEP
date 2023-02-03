import re

with open(r"brilcalc.log") as f: #Reading the file
    lines = f.readlines()

reg_totrec = r"\btotrecorded\(\/pb\)" #Defining regular expressions for totrecorded(/pb), recorded(/pb) and for | (since | only presents in lines with values)
reg_record = r"\brecorded\(\/pb\)"
valuelines = r"\|"

values = []
found_totrec = 0 #Defining list for recorded values and for if the match for previous two first regex have been found
found_record = 0

for line in lines:
    matchtotrec = re.search(reg_totrec, line)
    matchrecord = re.search(reg_record, line) #Searching for the match for all regex line by line
    matchvalue = re.search(valuelines, line)
    if matchtotrec != None:
        found_totrec += 1
        totstart = int(matchtotrec.start())-1 #If totrecorded regex (i.e. the header for the summed luminosity in summary) has been found, it takes the indices between the two | lines for totrecorded
        totend = int(matchtotrec.end())+1
        continue
    elif found_totrec == 1 and matchvalue != None:
        sum_value = "%.1f" % float(float(line[totstart:totend].strip())/1000) #Takes the totrecorded value between the indices defined before and makes it a float in fb^-1
        continue
    elif matchrecord != None:
        found_record += 1
        recstart = int(matchrecord.start())-1 #If recorded regex (i.e. the header for all the values to be summed) has been found, it takes the indices between the two | lines for recorded
        recend = int(matchrecord.end())+1
        continue
    elif found_record == 1 and matchvalue != None:
        value = float(float(line[recstart:recend].strip())/1000) #Takes the recorded value between the indices defined before and makes it a float in fb^-1
        values.append(value)
        continue
    continue

#The indices are convenient because the header and the values are aligned from the start at least. The ending index might not be the same for every value.
#That is why the extra leeway for the indices and stripping is needed for every value to not lose any information (though some may be different because
# of what Python is doing when dividing he values to get the wanted unit)

sum_of_values = "%.1f" % sum(values) #One decimal accuracy for the summed value of all the recorded values

#print(values)
print("Sum of recorded luminosities is",sum_of_values,"fb^-1") #Printing the values
print("Summary luminosity (totrecorded) is",sum_value,"fb^-1")

if sum_of_values == sum_value: #Checking if the luminosity values are the same
    print("The values are the same for the summed luminosities")
elif sum_of_values != sum_value:
    print("Summed values are not the same")
