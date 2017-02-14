import bhb
import matplotlib.pyplot as plt

bhbs = bhb.load('BHB_DATA_P.txt')

# should get the bhbs that are in this particular range
bs = [b for b in bhbs if b.teff > 7875 and b.teff < 8125 and b.feh > -1.5 and b.feh < -1.0 and b.logg > 2.75 and b.logg < 3.25]
print len(bs)




plt.subplot(311).scatter([b.obs_ug for b in bs],[b.obs_gr for b in bs])
plt.subplot(312).scatter([b.gen_ug for b in bs],[b.gen_gr for b in bs])

plt.show()