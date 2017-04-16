import util
import ast


class BHB:
  def __init__(self, data, fits_names = None, fromFits=False):
    if fromFits: # create bhb from fits file
      self.fits_data = data
      self.fits_names = fits_names
      self.valid = True #This is the general flag to tell if good bhb
      self.objID = data['spec.bestObjID']
      self.glat = data['GLAT']
      self.glon = data['GLON']
      self.gmag = data['gmag']
      self.ra = data['spec.ra']
      self.dec = data['spec.dec']
      self.d = data['d']
      self.flag = data['spp.FLAG'] # this is the flag value coming from sspp

      self.teff = data['spp.TEFFANNRR']
      self.logg = data['spp.LOGGANNRR']
      self.feh = data['spp.FEHANNRR']

      self.teff_annsr = data['spp.TEFFANNSR']
      self.logg_annsr = data['spp.LOGGANNSR']
      self.feh_annsr = data['spp.FEHANNSR']

      self.teff_ngs1 = data['spp.TEFFNGS1']
      self.logg_ngs1 = data['spp.LOGGNGS1']
      self.feh_ngs1 = data['spp.FEHNGS1']

      self.teff_ki13 = data['spp.TEFFki13']
      self.logg_ki13 = data['spp.LOGGki13']
      self.feh_ki13 = data['spp.FEHki13']

      self.teff_irfm = data['spp.TEFFIRFM']
      self.logg_irfm = data['spp.LOGGNGS1IRFM']
      self.feh_irfm = data['spp.FEHNGS1IRFM']

      # balmer series data
      self.teff_ha24 = data['spp.TEFFHA24']
      self.teff_hd24 = data['spp.TEFFHD24']

      self.ha24_cont = data['lines.Halpha24cont']
      self.ha24_side = data['lines.Halpha24side']
      self.ha24_cont_gen_gr = 0.818 - 0.092*self.ha24_cont
      self.ha24_side_gen_gr = 0.818 - 0.092*self.ha24_side
      self.ha24_cont_gen_teff = 4133 + 371*self.ha24_cont
      self.ha24_side_gen_teff = 4133 + 371*self.ha24_side
      
      self.hb24_cont = data['lines.Hbeta24cont']
      self.hb24_side = data['lines.Hbeta24side']
      
      self.hg24_cont = data['lines.Hgamma24cont']
      self.hg24_side = data['lines.Hgamma24side']
      
      self.hd24_cont = data['lines.Hdelta24cont']
      self.hd24_side = data['lines.Hdelta24side']
      self.hd24_cont_gen_gr = 0.469 - 0.058*self.hd24_cont
      self.hd24_side_gen_gr = 0.469 - 0.058*self.hd24_side
      self.hd24_cont_gen_teff = 5449 + 206*self.hd24_cont
      self.hd24_side_gen_teff = 5449 + 206*self.hd24_side

      # observed u,g,r,i,z
      self.u = data['photo.u']
      self.g = data['photo.g']
      self.r = data['photo.r']
      self.i = data['photo.i']
      self.z = data['photo.z']

      # observed dered u,g,r,i,z
      self.dered_u = data['photo.dered_u']
      self.dered_g = data['photo.dered_g']
      self.dered_r = data['photo.dered_r']
      self.dered_i = data['photo.dered_i']
      self.dered_z = data['photo.dered_z']

      # observed colors
      self.obs_ug = self.u - self.g
      self.obs_gr = self.g - self.r
      self.obs_ri = self.r - self.i
      self.obs_iz = self.i - self.z

      # observed dered colors
      self.red_ug = self.dered_u - self.dered_g
      self.red_gr = self.dered_g - self.dered_r
      self.red_ri = self.dered_r - self.dered_i
      self.red_iz = self.dered_i - self.dered_z

      # generated colors for ANNRR SSPP
      self.gen_ug_annrr = None
      self.gen_gr_annrr = None # default value, as we haven't generated it yet
      self.gen_ri_annrr = None
      self.gen_iz_annrr = None

      # generated colors using different sppParams (keep to ug and gr for now)
      self.gen_ug_annsr = None
      self.gen_gr_annsr = None
      self.gen_ug_ngs1 = None
      self.gen_gr_ngs1 = None
      self.gen_ug_ki13 = None
      self.gen_gr_ki13 = None

      # generated colors using irfm
      self.gen_ug_irfm = None
      self.gen_gr_irfm = None

      # difference between generated and observed colors
      self.dif_ug = None 
      self.dif_gr = None
      self.dif_ri = None
      self.dif_iz = None

      # difference between alt-sppParams gen and obs
      self.dif_ug_annsr = None
      self.dif_gr_annsr = None
      self.dif_ug_ngs1 = None
      self.dif_gr_ngs1 = None
      self.dif_ug_ki13 = None
      self.dif_gr_ki13 = None

      # dif between irfm gen and obs
      self.dif_ug_irfm = None
      self.dif_gr_irfm = None

      # difference between generated and dered
      self.dif_ug_dered = None
      self.dif_gr_dered = None
      self.dif_ri_dered = None
      self.dif_iz_dered = None

    else: # import from bhb txt file
      self.__dict__ = data


  def genColor(self,model):
    self.gen_ug, self.gen_gr, self.gen_ri, self.gen_iz = util.calColor(model,self.teff,self.feh,self.logg)
    self.dif_ug = self.gen_ug - self.obs_ug
    self.dif_gr = self.gen_gr - self.obs_gr
    self.dif_ri = self.gen_ri - self.obs_ri
    self.dif_iz = self.gen_iz - self.obs_iz
    self.dif_ug_dered = self.gen_ug - self.red_ug
    self.dif_gr_dered = self.gen_gr - self.red_gr
    self.dif_ri_dered = self.gen_ri - self.red_ri
    self.dif_iz_dered = self.gen_iz - self.red_iz

    # now other sppParams
    self.gen_ug_annsr, self.gen_gr_annsr, temp_ri, temp_iz = util.calColor(model, self.teff_annsr, self.feh_annsr, self.logg_annsr)
    self.dif_ug_annsr = self.gen_ug_annsr - self.obs_ug
    self.dif_gr_annsr = self.gen_gr_annsr - self.obs_gr

    self.gen_ug_irfm, self.gen_gr_irfm, temp_ri, temp_iz = util.calColor(model, self.teff_irfm, self.feh_irfm, self.logg_irfm)
    self.dif_ug_irfm = self.gen_ug_irfm - self.obs_ug
    self.dif_gr_irfm = self.gen_gr_irfm - self.obs_gr



def load(filename='BHB_DATA.txt'):
  print 'Loading BHBs from ' + filename
  bhbs = []
  f = open(filename,'r')
  for line in f:
    bhbs.append(BHB(ast.literal_eval(line)))
  return bhbs

# save list of bhbs to text file
def save(filename, bhbList):
  print 'Saving BHBs to ' + filename
  f = open(filename, 'w')
  for b in bhbList:
    f.write(str(b.__dict__) + '\n')
  print 'Done Saving bhbList'