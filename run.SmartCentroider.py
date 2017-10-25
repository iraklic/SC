# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 14:08:21 2016

@author: ichakaberia
"""

import new_functions as nf
import SmartCentroider as SmartC

#path = "c://Users/ichakaberia/Documents/BNL/AstroPhysics/Data/CFN/2016-10-14/Bio/Horizontal-Closer/"
#path = "c://Users/ichakaberia/Documents/BNL/AstroPhysics/Data/CFN/2016-10-14/Bio/Horizontal-0/"
#path = "c://Users/ichakaberia/Documents/BNL/AstroPhysics/Data/CFN/2016-10-14/Bio/Vertical/"
#path = "c://Users/ichakaberia/Documents/BNL/AstroPhysics/Data/CFN/2016-10-12/Perovskite/00-Spot1/"
#path = "c://Users/irakl/Desktop/20171020/Set1"
path = "c://Users/irakl/Desktop/20171020/WithScales-H/01"

#path = "c://Users/ichakaberia/Documents/BNL/AstroPhysics/Data/CFN/2016-10-12/Perovskite/01-Spot2/"
#path = "c://Users/ichakaberia/Documents/BNL/AstroPhysics/Data/CFN/2016-10-12/Perovskite/02-NoSpot/"

fileList = nf.GetFiles(path)

SC = SmartC.SmartCentroider(fileList)
SC.skiplines = 1
#SC.gaussian_size = 10
#SC.npix_per_cluster_cut = (2, 7)
#SC.bands = [(7460, 7490)]

SC.run()