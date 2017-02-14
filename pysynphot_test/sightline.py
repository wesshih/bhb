from astropy.io import fits

# take the entire combined catalog and filter out along some sight line

index = 1625 #this is the bhb that we will put at the center of sightline

data = fits.open('../combined.fits')[1].data

cen_ra = data[index]['spec.ra']
cen_de = data[index]['spec.dec']
width = 5

mask_ra1 = data['spec.ra'] > cen_ra - width
mask_ra2 = data['spec.ra'] < cen_ra + width
mask_de1 = data['spec.dec'] > cen_de - width
mask_de2 = data['spec.dec'] < cen_de + width

mask_full = mask_ra1 & mask_ra2 & mask_de1 & mask_de2

new_data = data[mask_full]

print `new_data.size` + ' bhbs'

hdu = fits.BinTableHDU(data=new_data)
hdu.writeto('Sightline.fits', clobber=True)
