import csv
import sys
with open("tes.csv", 'r') as file:
  csvreader = csv.reader(file)
  allvcf = open('ALL.vcf', 'w') 

  for row in csvreader:
    print(row[0])
                #write in the "ALL.vcf" file.
    allvcf.write( 'BEGIN:VCARD' + "\n")
    allvcf.write( 'VERSION:2.1' + "\n")
    allvcf.write( 'N:' + row[0] + ';' + row[1] + "\n")
    allvcf.write( 'FN:' + "Bootcamp " + row[1] + ' ' + row[0] + "\n") #remember that lastname first
    allvcf.write( 'ORG:' + 'Bootcamp' + "\n")
    allvcf.write( 'TEL;CELL:' + row[2] + "\n")
    allvcf.write( 'EMAIL:' + row[3] + "\n")
    allvcf.write( 'END:VCARD' + "\n")
    allvcf.write( "\n")
allvcf.close()