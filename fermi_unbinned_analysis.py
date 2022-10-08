import gt_apps as gt
from make4FGLxml import *
import pyLikelihood
from UnbinnedAnalysis import *
import numpy as np
import matplotlib.pyplot as plt
import json

print("________________________________________")
print("****************************************")
print("This program is strictly for unbinned analysis")
print("****************************************")
print("________________________________________\n")

#The source name input should not contain spaces
name = input("Enter the name of the source (without spaces): ")

data = open(name + "_data.txt", "r")
print(data.read()) #Prints the info in the data.txt file

#cat_id = input("Enter the FAVA catalogue id of the source: ")
f = open('catalogue.json')
catalogue = json.load(f)
cat_id = catalogue[name]["Gamma_ID"]

"""
Filter the data files according to the following conditions:
"""
print("____________________________")
print("Enter the following field")
print("____________________________\n")

gt.filter['evclass'] = 128                                                       #NOTE: This event class has a residual background rate
gt.filter['evtype']  = 3                                                         #NOTE: Both front and back convertion
gt.filter['ra']      = catalogue[name]["RA"]                                     #NOTE: RA coordinate in degrees
gt.filter['dec']     = catalogue[name]["Dec"]                                    #NOTE: Dec coordinate in degrees
gt.filter['rad']     = float(input("Enter the search radius of the source: "))   #TODO: Search radius around the source
gt.filter['tmin']    = int(input("Enter the Start time in MET format: "))        #TODO: MET Start time in seconds
gt.filter['tmax']    = int(input("Enter the End time in MET format: "))          #TODO: MET End time in seconds
gt.filter['emin']    = float(input("Enter the lower limit of energy in MeV: "))  #TODO: Minimum energy search in MeV
gt.filter['emax']    = float(input("Enter the upper limit of energy in MeV: "))  #TODO: Maximum energy search in MeV
gt.filter['zmax']    = 90                                                        #Maximum zenith angle, recommended angle is 90 degrees
gt.filter['infile']  = '@'+ name +'_events.list'                                 #REVIEW: make it so that for a single photon file it's "name_PH.fits"
gt.filter['outfile'] = name + '_filtered.fits'                                   #the name of the output filtered file

print("\n")
print("______________________________________")
print("Event class:         \t 128 (residual background model)")
print("Event type:          \t 3 (both front and back conversion)")
print("Position:            \t (", gt.filter['ra'], ", ", gt.filter['dec'], ")")
print("Search radius:       \t", gt.filter['rad'])
print("Energy:              \t", gt.filter['emin'], ", ", gt.filter['emax'])
print("Time [MET]:          \t", gt.filter['tmin'], ", ", gt.filter['tmax'])
print("Maximum Zenith Angle:\t", gt.filter['zmax'])
print("The input file name: \t", gt.filter['infile'])
print("The output file name:\t", gt.filter['outfile'])
print("______________________________________")
print("\n")

print("Running the selection protocol of the data....\n")

gt.filter.run() #command to run the filter protocol

print("Done.........!!!!!!!!!!")

"""
Make a good-time interval using the spacecraft file data
"""

gt.maketime['scfile']  = name +'_SC00.fits' #Enter the spacecraft file
gt.maketime['filter']  = '(DATA_QUAL>0) && (LAT_CONFIG==1)'
gt.maketime['roicut']  = 'no' #ROI-Based Zenith Angle Cut(roicut)
gt.maketime['evfile']  = name + '_filtered.fits' #the event data file
gt.maketime['outfile'] = name +'_filtered_gti.fits' #the name of output file

print("\n")
print("______________________________________")
print("Spacecrapt file:           \t", gt.maketime['scfile'])
print("Filter:                    \t", gt.maketime['filter'])
print("ROI-Based Zenith Angle Cut:\t", gt.maketime['roicut'])
print("Event file:                \t", gt.maketime['evfile'])
print("Output file:               \t", gt.maketime['outfile'])
print("______________________________________")
print("\n")

print("Running the maketime protocol forgood time interval....\n")

gt.maketime.run() #command to run the time selection protocol

print("Done.........!!!!!!!!!!")

"""
Creating a livetime cube
"""

gt.expCube['evfile']    = name + '_filtered_gti.fits'                     #the event data file
gt.expCube['scfile']    = name + '_SC00.fits'                             #the spacecraft file
gt.expCube['outfile']   = name + '_ltcube.fits'                           #the name of the output file
gt.expCube['zmax']      = 90                                              #the maximum zenith angle
gt.expCube['dcostheta'] = float(input("Enter the step size in cos(θ): ")) #TODO: step size in cos(\theta)
gt.expCube['binsz']     = int(input("Enter the bin-size: "))              #TODO: Size of bins

print("\n")
print("______________________________________")
print("Event file:          \t", gt.expCube['evfile'])
print("Spacecraft file:     \t", gt.expCube['scfile'])
print("Output file:         \t", gt.expCube['outfile'])
print("Maximum zenith angle:\t", gt.expCube['zmax'])
print("Step size in cos(θ): \t", gt.expCube['dcostheta'])
print("Bin size:            \t", gt.expCube['binsz'])
print("______________________________________")
print("\n")

print("Running the expCube protocol to create livetime cube.....\n")

gt.expCube.run()

print("Done.........!!!!!!!!")

""" 
Creating an exposure map
"""

gt.expMap['evfile']    = name + '_filtered_gti.fits' #the event data file
gt.expMap['scfile']    = name + '_SC00.fits'         #the spacecraft file
gt.expMap['expcube']   = name + '_ltcube.fits'       #the livetime-cube file
gt.expMap['outfile']   = name + '_expmap.fits'       #name of the output file
gt.expMap['irfs']      = 'P8R3_SOURCE_V3'            #input("Enter the response function [recommended: CALDB/P8R3_SOURCE_V3]: ")
gt.expMap['srcrad']    = gt.filter['rad'] + 10       #Choose (search-radius + 10)
gt.expMap['nlong']     = 120
gt.expMap['nlat']      = 120
gt.expMap['nenergies'] = int(input("Enter the energy bins[37]: ")) #TODO: Energy bin size

print("\n")
print("______________________________________")
print("Event file:        \t", gt.expMap['evfile'])
print("Spacecraft file:   \t", gt.expMap['scfile'])
print("Livetime cube file:\t", gt.expMap['expcube'])
print("Output file:       \t", gt.expMap['outfile'])
print("Response function: \t", gt.expMap['irfs'])
print("Axis segments:     \t", gt.expMap['nlong'], ", ", gt.expMap['nlat'])
print("Energy bin:        \t", gt.expMap['nenergies'])
print("______________________________________")
print("\n")

print("Running the expMap protocol for exposure map\n")

gt.expMap.run()

print("Done..........!!!!!!!!!")

#REVIEW: what this part of the code doing?
print("Running......") 
mymodel = srcList('gll_psc_v28.xml', name + '_filtered_gti.fits', name + '_model.xml')
mymodel.makeModel('/home/ray/miniconda3/envs/fermi/share/fermitools/refdata/fermi/galdiffuse/gll_iem_v07.fits', 'gll_iem_v07', '/home/ray/miniconda3/envs/fermi/share/fermitools/refdata/fermi/galdiffuse/iso_P8R3_SOURCE_V3_v1.txt', 'iso_P8R3_SOURCE_V3_v1')
print("Done..........!!!!!!!!")

gt.diffResps['evfile'] = name + '_filtered_gti.fits'
gt.diffResps['scfile'] = name + '_SC00.fits'
gt.diffResps['srcmdl'] = name + '_model.xml'
gt.diffResps['irfs']   = 'P8R3_SOURCE_V3'

print("\n")
print("______________________________________")
print("Event file:       \t", gt.diffResps['evfile'])
print("Spacecraft file:  \t", gt.diffResps['scfile'])
print("Source model:     \t", gt.diffResps['srcmdl'])
print("Response function:\t", gt.diffResps['irfs'])
print("______________________________________")
print("\n")

print("Running the diffResps protocol\n")

gt.diffResps.run()

print("Done........!!!!!!!!!")

obs = UnbinnedObs(name + '_filtered_gti.fits',name + '_SC00.fits',expMap=name + '_expmap.fits',
expCube=name + '_ltcube.fits',irfs='P8R3_SOURCE_V3')
like = UnbinnedAnalysis(obs, name + '_model.xml',optimizer='NewMinuit')

print("\nThe obs object:")
print(obs)
print("\nThe like object:")
print(like)
print("\n")

print(like.tol)

if like.tolType == 1:
    print("Tolerance type: Absolute\n")
else:
    print("Tolerance type: Relative\n")

like.tol = float(input("Enter the preferred tolerance value: ")) #TODO: Enter the preffered tolerance value
likeobj = pyLike.NewMinuit(like.logLike)
print("Running the fit protocol........")
print(like.fit(verbosity = 0, covar = True, optObject = likeobj)) #NOTE: This step is running the model fitting

like.plot() #NOTE: Plot the data

#NOTE: The section below plots the data using matplotlib
# E = (like.energies[:-1] + like.energies[1:]) / 2
# plt.figure(figsize=(5,5))
# plt.ylim((0.4, 1e4))
# plt.xlim((100, 500000))
# sum_model = np.zeros_like(like._srcCnts(like.sourceNames()[0]))
# for sourceName in like.sourceNames():
#     sum_model = sum_model + like._srcCnts(sourceName)
#     plt.loglog(E, like._srcCnts(sourceName), label=sourceName[1:])
# plt.loglog(E,sum_model,label='Total Model')
# plt.errorbar(E,like.nobs,yerr=np.sqrt(like.nobs), fmt='o',label='Counts')
# ax = plt.gca()
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width * 0.5, box.height])
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.show()

if likeobj.getRetCode() == 0:
    print("The likelihood analysis didn't converge\n")
else:
    print("The likelihood analysis converged succesfully\n")

print("Model fit parameters: ")
print(like.model[cat_id])
print("The flux value: ")
print(like.flux(cat_id, emin = gt.filter['emin']))
# like.flux(cat_id, emin = gt.filter['emin'])
print("The flux error: ")
print(like.fluxError(cat_id, emin = gt.filter['emin']))
print("The Test statistics of the source: ")
print(like.Ts(cat_id))
print("The standard deviation ( TS value is ~ σ^2): ")
print(np.sqrt(like.Ts(cat_id)))

print("Writing the model fit results in an XML file......")
like.logLike.writeXml(name + '_fit.xml')
print("Done........!!!!!")
