
#arrObjID = []

#t3 = curT()
#for i in range(len(data)):
#  objID = 0
#  for j in range(len(res[1:])):
#    if pointWithinRegion(data[i]['RAJ2000'],data[i]['DEJ2000'],res[j][1], res[j][2], region):
#      # then the points are the same
#      objID = res[j][0]
#      break
#  print "on data elem " + `i` + ", adding ID " + `objID`
#  arrObjID.append(objID)
#t4 = curT()
#print "copy time: " + `t4-t3`
#print "hopefully coppied ok?"

curT = lambda: int(round(time.time()))

#region = 0.0002777 # half square width in degrees
#printQueries = True
#printResults = True
#executeQuery = True
#hdus = fits.open('bhbcatlog.fit')
#data = hdus[1].data

#res = []
#count = 0 # from
#size = data.size # to
#queryLimit = 10 # step --> 14 is the largest reliable size
#
#if len(sys.argv) > 1:
#  count = int(sys.argv[1])
#  size = int(sys.argv[2])
#  queryLimit = int(sys.argv[3])
#
#t1 = curT()
#
#while count < size:
#  print "Progress: " + `count` + "/" + `size`
#  query = "SELECT specObjID, ra, dec, plate, fiberID\nFROM specObj\nWHERE"
#  needOR = False #Need to add ORs for multiple BHBss
#  if size - count < queryLimit:
#    queryLimit = size - count
#  for i in range(count, count + queryLimit):
#    ra = data[i]['RAJ2000']
#    dec = data[i]['DEJ2000']
#    plate = data[i]['PLATE']
#    fiber = data[i]['FIBER']
#    if needOR:
#      query = query + "\nOR"





# this method creates arrays that will become columns for the new data.
# these arrays will have the same ordering as the data from the fits file
def matchEntries(data, results, region):
  #arr_sID = []
  #arr_bID = []
  #arr_eBV = []
  #arr_eTEff = []
  #arr_eLogG = []
  #arr_eFeH = []
  #arr_eZ = []
  #arr_eZErr = []

  #arr_tup = (arr_sID, arr_bID, arr_eBV, arr_eTEff, arr_eLogG, arr_eFeH, arr_eZ, arr_eZErr) = ([],[],[],[],[],[],[],[])
  arr_tup = (arr_sID, arr_bID, arr_eBV, arr_eTEff, arr_eLogG, arr_eFeH, arr_eZ, arr_eZErr) = tuple([[] for i in range(8)])
  print arr_tup

  count = 0

  #for i in range(len(data)): # for each data entry look for an entry in result
  for d in data: # for each data entry look for an entry in result
    # set the default values --> use -9999 as it is sufficiently different from any regular value for all fields
    #sID = bID = eBV = eTEff = eLogG = eFeH = eZ = eZErr = -9999
    val_tup = (sID, bID, eBV, eTEff, eLogG, eFeH, eZ, eZErr) = tuple([-9999 for i in range(8)])
    if count == 25: print val_tup
    #bID = -9999
    #eBV = -9999
    #eTEff = -9999
    #eLogG = -9999
    #eFeH = -9999
    #eZ = -9999
    #eZErr = -9999

    #for j in range(len(results)):
    for r in results:
      if isInRegion(r[1],r[2],d['RAJ2000'],d['DEJ2000'],region):
        # then these two points are the same
	# there is definitely some cool way to do this with map and lambda functions but I can't remember

        val_tup = (r[0],r[3],r[4],r[5],r[6],r[7],r[8],r[9])
	if count == 25: print val_tup

       # sID = r[0]
       # bID = r[3]
       # eBV = r[4]
       # eTEff = r[5]
       # eLogG = r[6]
       # eFeH = r[7]
       # eZ = r[8]
       # eZErr = r[9]
	results.remove(r)
