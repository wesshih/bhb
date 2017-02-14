# import matplotlib.pyplot as plt
# from astropy.io import fits
import numpy as np
import pysynphot as S
import bhb


bhbs = bhb.load('BHB_DATA_P.txt')

pos_gr = [b for b in bhbs if b.dif_gr > 0]

size = 10

# this is for ANNSR
bhb_annsr = [b for b in pos_gr if b.feh_annsr > -4 and b.feh_annsr < 0.5]
gr_annsr = []
count = 0
for b in bhb_annsr[:size]:
	count = count + 1
	if count % 100 == 0:
		print 'on number ' + `count`
	s = S.Icat('phoenix',b.teff_annsr,b.feh_annsr,b.logg_annsr)
	g = S.Observation(s, S.ObsBandpass('sdss,g'),s.GetWaveSet())
	r = S.Observation(s, S.ObsBandpass('sdss,r'),s.GetWaveSet())
	gr = g.effstim('abmag') - r.effstim('abmag')
	gr_annsr.append(gr)

bol_annsr = [g < 0 for g in gr_annsr]
print bol_annsr
print sum(bol_annsr)
print len(bol_annsr)
print gr_annsr


# this is for NGS1
bhb_ngs1 = [b for b in pos_gr if b.feh_ngs1 > -4 and b.feh_ngs1<0.5]
gr_ngs1 = []
count = 0
for b in bhb_ngs1[:size]:
	count = count + 1
	if count % 100 == 0:
		print 'on number ' + `count`
	s = S.Icat('phoenix',b.teff_ngs1,b.feh_ngs1,b.logg_ngs1)
	g = S.Observation(s, S.ObsBandpass('sdss,g'),s.GetWaveSet())
	r = S.Observation(s, S.ObsBandpass('sdss,r'),s.GetWaveSet())
	gr = g.effstim('abmag') - r.effstim('abmag')
	gr_ngs1.append(gr)

bol_ngs1 = [g < 0 for g in gr_ngs1]
print bol_ngs1
print sum(bol_ngs1)
print len(bol_ngs1)
print gr_ngs1


# this is for ki13
bhb_ki13 = [b for b in pos_gr if b.feh_ki13 > -4 and b.feh_ki13<0.5]
gr_ki13 = []
count = 0
for b in bhb_ki13[:size]:
	count = count + 1
	if count % 100 == 0:
		print 'on number ' + `count`
	s = S.Icat('phoenix',b.teff_ki13,b.feh_ki13,b.logg_ki13)
	g = S.Observation(s, S.ObsBandpass('sdss,g'),s.GetWaveSet())
	r = S.Observation(s, S.ObsBandpass('sdss,r'),s.GetWaveSet())
	gr = g.effstim('abmag') - r.effstim('abmag')
	gr_ki13.append(gr)

bol_ki13 = [g < 0 for g in gr_ki13]
print bol_ki13
print sum(bol_ki13)
print len(bol_ki13)
print gr_ki13