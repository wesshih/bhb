;+
;PURPOSE
;	convert a spectrum to an sdss magnitude... note always does
;	AB magnitudes... none of that asinh stuff
;SYNTAX
;	mags=spec2mag(wave, flux[, totflux=totflux, filtfile=filtfile,
;			filtwave=filtwave, filt_thru=filt_thru])
;INPUTS
;	wave: wavelength in angstroms
;	flux: flux in 10^(-17) ergs/s/cm^2/ang
;	filtfile: if you don't want sdss magnitude then provide a filter file
;		of the filter you want
;	filtwave: filter wavelength (alternative to filtfile inputs)
;	filt_thru: filter thru-put (alternatuve to filtfile inputs)
;KEYWORDS
;	careful: set to a value between 0 and 1. This is the fraction of
;		the integral of the filter function that must be covered
;		spectrally for this to output a magnitude [default=1]
;OUTPUTS
;	mags: 5 sdss magnitudes
;	totflux: the total flux prior to conversion to magnitudes
;	frac_filt: the fraction of the integral of the filter function
;		that you had spectral coverage of
;NOTES: 
;	portions hacked from filter_thru.pro
;	only calculates the pogson magnitude. this version doesn't deal with 
;	that asinh mess
;Written by R. da Silva, UCSC
;-
FUNCTION spec2mag, wave, flux, totflux=totflux, filtfile=filtfile, $
	filtwave=filtwave, filt_thru=filt_thru, quiet=quiet, careful=careful,$
	frac_filt=frac_filt

if keyword_set(careful) EQ 0 then careful=1.
if careful LT 0 OR careful GT 1. then begin
	print, 'SPEC2MAG; ***Careful must be set between 0 and 1***'
	print, 'SPEC2MAG: returning'
	return, -1
endif

c=double( 2.9979000e+10);the speed of light
wave=double(wave)
flux=double(flux)
;read in names of filer files
   if (NOT keyword_set(filter_prefix)) then filter_prefix='sdss_jun2001'
   ffiles = [filter_prefix+'_u_atm.dat', filter_prefix+'_g_atm.dat', $
             filter_prefix+'_r_atm.dat', filter_prefix+'_i_atm.dat', $
             filter_prefix+'_z_atm.dat']
   nfiles=n_elements(ffiles)
;   lambda=float([3543,4770,6231,7625,9134])   

mags=dblarr(nfiles)
totflux=dblarr(nfiles)
frac_filt=dblarr(nfiles)
for ifile=0, nfiles-1 do begin ;grab sdss filters
if not keyword_set(filtfile) then begin
   filename = filepath(ffiles[ifile], $
       root_dir=getenv('IDLUTILS_DIR'), subdirectory=['data','filters'])
endif else filename=filtfile
if not keyword_set(filtwave) then $	
      readcol, filename, fwave, fthru, /silent else begin
fwave=filtwave
fthru=filt_thru
endelse
   wh=where(fwave GE min(wave) AND fwave LE max(wave), ct)
   if ct EQ 0 then continue
   frac_filt[ifile]=tsum(fwave, fthru, min(wh), max(wh))/tsum(fwave, fthru)
   if tsum(fwave, fthru, min(wh), max(wh))/tsum(fwave, fthru) LT double(careful) then continue
   lambda=tsum(fwave, fthru*fwave)/tsum(fwave, fthru)
   linterp, fwave, fthru, wave, interpfilt, missing=0
				;added this line aboue missing
				;had to convert everything to doubles
   totfilt=tsum(wave, interpfilt)
   totflux[ifile]=1d-17*lambda^2*1d-8*$
	tsum(wave, flux*interpfilt)/totfilt/c
	; flux convolved with filter/ integral over filter
	;times lambda^2/c
	;factor of 1d-17 for the initial units
	;factor of 1d-8 to convert from angstroms
endfor

mags=-2.5*alog10(totflux)-48.6
;if total(finite(mags)) NE 5 AND keyword_set(quiet) EQ 0 then begin
;splog, 'mag caclulated to not be real'
;STOP
;return, -1
;endif

return, mags
end
