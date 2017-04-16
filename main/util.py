from astropy.io import fits
import pysynphot as S
import numpy as np
#import matplotlib.pyplot as plt


def calColor(model,teff, feh, logg):
  if feh < -4:
    print 'very low feh of ' + `feh` + ', using -4'
    feh = -4
  elif feh > 0.5:
    print 'very high feh of ' + `feh` + ', using 0.5'
    feh = 0.4

  if logg > 5.5:
    print 'very high logg of ' + `logg` + ', using 5.5'
    logg = 5.4
  elif logg < 0:
    print 'very low logg of ' + `logg` + ', using 0'
    logg = 0

  spec = S.Icat(model, teff, feh, logg)
  obs_u = S.Observation(spec, S.ObsBandpass('sdss,u'), spec.GetWaveSet())
  obs_g = S.Observation(spec, S.ObsBandpass('sdss,g'), spec.GetWaveSet())
  obs_r = S.Observation(spec, S.ObsBandpass('sdss,r'), spec.GetWaveSet())
  obs_i = S.Observation(spec, S.ObsBandpass('sdss,i'), spec.GetWaveSet())
  obs_z = S.Observation(spec, S.ObsBandpass('sdss,z'), spec.GetWaveSet())
  u_g = obs_u.effstim('abmag') - obs_g.effstim('abmag')
  g_r = obs_g.effstim('abmag') - obs_r.effstim('abmag')
  r_i = obs_r.effstim('abmag') - obs_i.effstim('abmag')
  i_z = obs_i.effstim('abmag') - obs_z.effstim('abmag')
  return (u_g, g_r,r_i,i_z)


def filterMissing(bhb):
  mask1 = bhb['spp.TEFFANNRR'] > 0
  mask2 = bhb['spp.TEFFANNSR'] > 0
  mask3 = bhb['spp.FEHANNSR'] > -999
  mask4 = bhb['spp.LOGGANNSR'] > -999
  mask5 = bhb['spp.TEFFIRFM'] > 0
  
  return bhb[mask1 & mask2 & mask3 & mask4 & mask5]

def filterInd(bhbs):
  mask1 = bhbs['spp.TEFFANNRRIND'] == 1 #1 is good for teff and logg
  mask2 = bhbs['spp.LOGGANNRRIND'] == 1
  mask3 = bhbs['spp.FEHANNRRIND'] == 2 # 2 is good for fe/h

  # mask4 = bhbs['spp.TEFFANNSRIND'] == 1 #1 is good for teff and logg
  # mask5 = bhbs['spp.LOGGANNSRIND'] == 1
  # mask6 = bhbs['spp.FEHANNSRIND'] == 2 # 2 is good for fe/h

  print sum(mask1&mask2&mask3)
  # print sum(mask4&mask5&mask6)

  return bhbs[mask1 & mask2 & mask3] # & mask4 & mask5 & mask6]

  

# Python Shell Functions

def getCombined():
  return fits.open('combined.fits')[1].data

def getSight():
  return fits.open('Sightline.fits')[1].data

def startps():
  data = filterMissing(getCombined())
  return data

  
