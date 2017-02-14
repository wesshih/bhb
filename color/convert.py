import os
import math

# import filter data
u_file = open('u.dat','r')
u_sen = []
for l in u_file:
  sen = l[:-1].split(',')
  u_sen.append({'wvln':float(sen[0]),'f1':float(sen[1]),'f2':float(sen[2]),'f3':float(sen[3]),'f4':float(sen[4])})

# import flux data
f_file = open('test_fluxes.flx','r')
raw = []
for l in f_file:
  raw.append(float(l))
f_min,f_max = 1300,200000
f_step = (f_max-f_min)*1.0/len(raw)
fluxes = []
for i in range(len(raw)):
  fluxes.append({'wvln':(f_min + (i*f_step)),'flux':raw[i]})

ptr_f,ptr_s = 0,0
res = []
start = True

wf = 'f3'
count = 0
for flux in fluxes:
  if start:
    #if flux['wvln'] < u_sen[ptr_s]['wvln']:
      # do nothing
    #else:
    if flux['wvln'] >= u_sen[ptr_s]['wvln']:
      print flux['wvln']
      start = False
      res.append(u_sen[ptr_s][wf]*flux['flux']) # must do the first one
    else:
      ptr_f += 1
  elif ptr_s < len(u_sen)-1:
    if flux['wvln'] < u_sen[ptr_s+1]['wvln']:
      res.append(u_sen[ptr_s][wf]*flux['flux'])
      count += 1
    else:
      print count
      count = 0
      ptr_s += 1
      res.append(u_sen[ptr_s][wf]*flux['flux'])


#for sen in u_sen:
#  if fluxes[ptr_f]['wvln'] < sen['wvln']:
#    print 'case1: ' + `fluxes[ptr_f]['wvln']` + ', ' + `sen['wvln']`
#    ptr_f += 1
#  elif (fluxes[ptr_f]['wvln'] > sen['wvln']+25) and ptr_s < len(u_sen):
#    print 'case2'
#    ptr_s += 1
#  else:
#    print 'case3'
#    sum = 0
#    while fluxes[ptf_f]['wvln'] < sen['wvln']+25:
#      sum += sen['f1']*fluxes[ptr_f]
#      ptr_f += 1
#    res.append({'wvln':sen['wvln'],'sum':sum})
print len(res)
print res[0:25]

print sum(res)
print (-2.5 * math.log(sum(res),10))

print fluxes[0]
print u_sen[0]
