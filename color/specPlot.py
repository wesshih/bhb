import matplotlib.pyplot as plt

# i guess just do 1 angstrom?
#def avg_flux(wv,fx):
#  counts = []
#  start = wv[0]
#  index = 0
#  while index < len(wv):
#    ift


def main():  
  f_file = open('test_fluxes.flx','r')
  fluxes = []
  count = 0
  limit = -1
  start = 30000
  stop = 30300
  
  low = 2000
  high = 10000
  for l in f_file:
    if limit > 0 and count > limit:
      break
    fluxes.append(float(l[:-1]))
    count += 1
  f2 = open('flx_wavelengths.vac','r')
  wvln = []
  count = 0
  for l in f2:
    if limit > 0 and count > limit:
      break
    wvln.append(float(l[:-1]))
    count += 1
  
  if len(fluxes) != len(wvln):
    print 'we have an issue, exiting'
  else:
    dat = {}
    for i in range(len(wvln)):
      dat[wvln[i]]=fluxes[i]
  
    plt_wvln = filter(lambda x: x > low and x < high,wvln)
  
    plt_flxs = map(lambda x: dat.get(x),plt_wvln)
  
    #f_min,f_max = 1300,200000
    #f_step = (f_max-f_min)*1.0/len(raw)
    #wvs = []
    #fxs = []
    #for i in range(len(raw)):
    #  wvs.append((f_min + (i*f_step)))
    #  fxs.append(raw[i])
    #
    #print(wvs[0])
    #print(fxs[0])
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.scatter(wvs,fxs,c='b',marker='.')
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    #ax1.scatter(wvln[start:stop],fluxes[start:stop],c='b',marker='.')
    ax1.scatter(plt_wvln,plt_flxs,c='b',marker='.')
    ax2 = fig.add_subplot(212)
    #ax2.plot(wvln[start:stop],fluxes[start:stop])
    ax2.plot(plt_wvln,plt_flxs)
   
  
    plt.show()

if __name__ == '__main__':
  main()
