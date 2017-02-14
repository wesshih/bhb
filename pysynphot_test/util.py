from astropy.io import fits
import pysynphot as S
import numpy as np


def cal_color(teff, feh, logg):
  spec = S.Icat('phoenix', teff, feh, logg)
  obs_g = S.Observation(spec, S.ObsBandpass('sdss,g'), spec.GetWaveSet())
  obs_r = S.Observation(spec, S.ObsBandpass('sdss,r'), spec.GetWaveSet())
  return obs_g.effstim('abmag') - obs_r.effstim('abmag')


def compare_color(bhb):
  gen_gr = cal_color(bhb['spp.TEFFANNRR'],bhb['spp.FEHANNRR'],bhb['spp.LOGGANNRR'])
  obs_gr = bhb['photo.g'] - bhb['photo.r']
  red_gr = bhb['photo.dered_g'] - bhb['photo.dered_r']
  return (obs_gr, red_gr, gen_gr)

def print_bhb(bhb, num):
  print 'BHB #' + `num`
  print 'teff: ' + `bhb['spp.TEFFANNRR']`
  print 'fe/h: ' + `bhb['spp.FEHANNRR']`
  print 'logg: ' + `bhb['spp.LOGGANNRR']`

def filterMissing(bhb):
  mask = bhb['spp.TEFFANNRR'] > 0
  return bhb[mask]

# Python Shell Functions

def getCombined():
  return fits.open('../combined.fits')[1].data

def getSight():
  return fits.open('Sightline.fits')[1].data

def startps():
  data = filterMissing(getCombined())
  return data

  
