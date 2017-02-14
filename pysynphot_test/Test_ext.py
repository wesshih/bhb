from astropy.io import fits
import pysynphot as S
import matplotlib.pyplot as plt
import numpy as np


def cal_color(sp):
  obs_g = S.Observation(sp, S.ObsBandpass('sdss,g'))
  obs_r = S.Observation(sp, S.ObsBandpass('sdss,r'))
  return obs_g.effstim('abmag') - obs_r.effstim('abmag')

data = fits.open('../combined.fits')[1].data

bhb = data[1045]

teff = bhb['spp.TEFFANNRR']
logg = bhb['spp.LOGGANNRR']
feh = bhb['spp.FEHANNRR']
z = 0.000017

sp = S.Icat('phoenix', teff, feh, logg)
syngr = cal_color(sp)

obsgr = bhb['photo.g'] - bhb['photo.r']
redgr = bhb['photo.dered_g'] - bhb['photo.dered_r']

print 'feh ' + `feh`
print 'syngr ' + `syngr`
print 'obsgr ' + `obsgr`
print 'redgr ' + `redgr`

delta = syngr - obsgr
deltar = syngr - redgr

print delta
print deltar

print 'distance: ' + `bhb['d']`
