import util
import ast


class BHB:
  def __init__(self, data, fromFits=False):
    if fromFits: # create bhb from fits file
      self.data = data
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

      # generated colors (right now only one model okay)
      self.gen_ug = None
      self.gen_gr = None # default value, as we haven't generated it yet
      self.gen_ri = None
      self.gen_iz = None

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
  bhbs = []
  f = open(filename,'r')
  for line in f:
    bhbs.append(BHB(ast.literal_eval(line)))
  return bhbs
