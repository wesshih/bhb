from astropy.io import fits

# This is where any secondary filtering will happen. If the data needs to be cleaned up more, then that should be done here.

# should this be a util file?

# The only filtering done in query.py is those in bhbcatlog.fit that don't return results for the ra/dec region. These bhbs probably lie just outside the 1 arsecond radius region. for now we will just remove them from the fits tables

# filter out BHBs with teff < 0. 

def filter_missing(data):
  teff_raw = data['spp.TEFFANNRR']
  teff_raw_ind = data['spp.TEFFANNRRIND']
  logg_raw = data['spp.LOGGANNRR']
  logg_raw_ind = data['spp.LOGGANNRRIND']
  feh_raw = data['spp.FEHANNRR']
  feh_raw_ind = data['spp.FEHANNRRIND']
  dist = data['d']

  teff = [e for e in teff if e > 0] # must have pos temp
  teff_fil = [e[0] for e in zip(tmp_dat,tmp_dat_ind) if e[1]==1]

  print teff_raw.size
  print teff.size
  print teff_fil.size


#tmps = [e for e in teff if e > 0] # must have pos temp
#fil_tmps = [e[0] for e in zip(tmp_dat,tmp_dat_ind) if e[1]==1]
#
#gs = [e for e in g_dat if e > -9999]
#fil_gs = [e[0] for e in zip(g_dat,g_dat_ind) if e[1]==1]
#
#fes = [e for e in fe_dat if e > -9999]
#fil_fes = [e[0] for e in zip(fe_dat,fe_dat_ind) if e[1]==2]
#
#fes_dist = [(e[0],e[2]) for e in zip(fe_dat,fe_dat_ind,dist) if e[1] == 2]
#fedist_fe,fedist_dist = zip(*fes_dist)

#print len(fes)
#print len(fil_fes)

