import util
from bhb import BHB

def main():
  # gets data, but filters out -9999 vals, and those with bad indicators
  data = util.filterInd(util.filterMissing(util.getCombined()))
  print data.size

  # this is my hacky way to avoid a reference problem
  tempBinTable = util.fits.BinTableHDU(data=data)
  data = tempBinTable.data

  print 'Starting BHB conversion'

  count = 0

  bhbList = []
  for d in data:
    count += 1
    if count % 500 == 0:
      print 'count: ' + `count`
    bhbList.append(BHB(d,fromFits=True))

  gen_gr = []
  gen_ug = []

  count = 0
  print 'Generating the intrinsic g-r colors for bhbs'
  # this is where we do all the bhb first time prep
  for b in bhbList:
    count += 1
    if count % 100 == 0:
      print 'count: ' + `count`
    b.genColor('k93models')
    gen_gr.append(b.gen_gr)
    gen_ug.append(b.gen_ug)

  print 'Creating the new fits now'
  # saving the generated colors into a master fits file
  oldCols = data.columns
  # print oldCols
  ugCol = util.fits.Column(name='phoenix_u-g', format='D',array=gen_ug)
  grCol = util.fits.Column(name='phoenix_g-r', format='D',array=gen_gr)
  newCols = util.fits.ColDefs([grCol,ugCol])
  newHDU = util.fits.BinTableHDU.from_columns(oldCols + newCols)
  # newHDU.writeto('new_bhb.fits',clobber=True)
  print 'new data size: ' + `newHDU.data.size`
  print len(gen_gr)


  # okay saving the bhb data now
  print 'Converting ' + `len(bhbList)` + ' entries to BHB objects'
  # fileName = 'BHB_DATA_P.txt'
  # fileName = 'BHB_DATA_CK.txt'
  fileName = 'BHB_DATA_K.txt'
  f = open(fileName,'w')
  for b in bhbList:
    f.write(str(b.__dict__) + '\n')
  print 'done'

if __name__ == '__main__':
  main()
