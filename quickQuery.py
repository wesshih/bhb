from astropy.io import fits
import sqlcl
import sys
import time
import numpy as np

def makeQueries(bhb_fits,fields):
	# make queries, lets start with limit of 1000 bhbs
	queries = []
	index = 0
	step = 13

	while index < len(bhb_fits):
		q_str = 'SELECT ' + fields[0]
		for i in range(len(fields[1:])):
			q_str = q_str + ', ' + fields[i+1]
		q_str = q_str + ' FROM specObjAll spec WHERE '
		q_str = q_str + 'spec.specObjID = ' + `bhb_fits[index]['spec.specObjID']` 
		for bhb in bhb_fits[index + 1:min(index+step, len(bhb_fits))]:
			q_str = q_str + ' OR spec.specObjID = ' + `bhb['spec.specObjID']`
		queries.append(q_str)
		index = index + step

	return queries

def executeQueries(queries, formats):
	#run those queries yo
	first = True
	results = []
	count = 1

	for q in queries:
		print 'running query ' + `count`
		count = count + 1
		lines = sqlcl.query(q).readlines()
		if lines[0][:-1] != '#Table1':
			# the query failed, just print it and exit
			print 'the query failed, moving to next query.'
		else:
			# if first: #add fields
			# 	results.append(lines[1][:-1].split(','))
			# 	first = False
			for l in lines[2:]:
				results.append(map(lambda x,y: x(y), formats ,l[:-1].split(',')))

	return results

def checkCollisions(results):
	# check collisions maybe?
	for i in range(len(results)):
		if i == 0:
			continue
		else:
			ID = results[i][0]
			for r2 in results[i+1:]:
				ID2 = r2[0]
				if ID == ID2:
					print 'collision with ID: ' + `ID` + ', ' + `ID2`
	print 'collision checking done'

def createFits(bhb_fits, results, fields, formats, filename):
	# match the query results to the fits data

	width = len(results[0][1:]) # how many individual fields were queried
	height = len(bhb_fits) # one row for each bhb 

	# a little confusing because i am using rows here, but they actually represent columns in fits
	valCols = []
	for i in range(width):
		valCols.append([-9999]*height)

	names = fields #results[0][2:]
	# results.remove(results[0]) # remove the names row

	indices = []  # array to hold the indices of updated elements. useful for dev

	for i in range(len(bhb_fits)):
		if len(results) == 0:
			break

		for res in results:
			if len(results)%500==0:
				print `len(results)` + ' res left to match'
			if bhb_fits[i]['spec.specObjID'] == res[0]:
				indices.append(i)
				for j in range(width):
					valCols[j][i] = res[j+1]
				results.remove(res)
				break

	formats = map(lambda x: 'D' if x == float else ('K' if x == int else '30A'),formats)

	newCols = []
	for i in range(width):
		col = fits.Column(name=names[i],format=formats[i],array=valCols[i])
		newCols.append(col)

	newColDefs = fits.ColDefs(newCols)
	oldColDefs = bhb_fits.columns
	newHDU = fits.BinTableHDU.from_columns(oldColDefs+newColDefs)
	newHDU.writeto(filename, clobber=True)


# direct copy-pasta from query.py too lazy to put in a centralized place
def readFieldsFile(filename):
  form_dict = {'float':float,'int':int,'str':str}
  f = open(filename,'r')
  fields = []
  formats = []
  for l in f:
    field,form = l[:-1].split(',')
    fields.append(field)
    formats.append(form_dict[form])
  return (fields,formats)

def main():
	startTime = time.time()

	bhb_fits = fits.open('combined_022317.fits')[1].data

	start = 0
	end = len(bhb_fits)

	fields,formats = readFieldsFile('quickFields.txt')

	# fields = ['lines.bestObjID','lines.specObjID','lines.Halpha24cont','lines.Halpha24err',
	# 			'lines.Halpha24mask','lines.Halpha24side']
	# formats = [int,int,float,float,int,float]

	print 'Starting query process'
	queries = makeQueries(bhb_fits[start:end],fields)
	print queries[0]
	print 'Finished making queries: ' + `len(queries)`


	results = executeQueries(queries,formats)
	#checkCollisions(results)

	print 'Finished executing queries'
	print 'Results of length: ' + `len(results)`

	print 'Matching results and making new fits'
	createFits(bhb_fits, results, fields[1:], formats[1:], 'quickQuery_elodie.fits')

	endTime = time.time()
	print 'Finished Execution in ' + `(endTime-startTime)` + ' seconds'




if __name__ == '__main__':
	main()