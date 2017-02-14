import bhb

bhbs = bhb.load('BHB_DATA_P.txt')
print len(bhbs)

# restrict to high galactic latitudes
bhbs = [b for b in bhbs if b.glat > 75]
print len(bhbs)

bhbs = [b for b in bhbs if b.d < 10]
print len(bhbs)

bhbs = [b for b in bhbs if abs(b.obs_gr-b.red_gr) < 0.02]
print len(bhbs)

pos = 0
for b in bhbs:
	print 'obs: ' + `b.obs_gr`
	print 'red: ' + `b.red_gr`
	print 'gen: ' + `b.gen_gr`
	print ''
	if b.dif_gr > 0:
		pos += 1

print pos