with open('/Users/dsrinath/Desktop/Dbig.txt') as infile, open('/Users/dsrinath/Desktop/output.csv', 'w') as outfile:
    outfile.write(infile.read().replace(" ", ","))