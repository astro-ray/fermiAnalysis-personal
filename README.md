# Instructions to Run Fermi Analysis Software Tools

### <u>Choosing Sources</u>:

Our recommendation for choosing sources is as follows:

There are two types of catalogue for Gamma-Ray sources

* [FAVA Catalogue:](https://arxiv.org/pdf/1612.03165.pdf) An all sky Gamma ray source catalogue published my Fermi LAT.
* [TeV Catalogue:](http://tevcat.uchicago.edu/) This is a catalogue for the TeV energy sources in extragalactic space.

We will follow the steps listed below:

1. We will mark all the sources in FAVA catalogue that shows high activity ( I choose a threshold of $N^f>35$ )
2. Match the FAVA sources against the TeV catalogue
3. From there we will preferably choose sources that are either FRSQ or BL Lac
4. We will then extract the data from Fermi Servers

Here is a table of all the sources

<table class="styled-table" summary="Preferred Sources" width="100%">
    <tbody>
        <tr>
            <th>Name</th>
            <th>RA</th>
            <th>Dec</th>
            <th>Date</th>
            <th>Type</th>
        </tr>
        <tr>
            <td>3C 279</td>
            <td>194.05</td>
            <td>-5.78</td>
            <td>2007.08</td>
            <td>FRSQ</td>
        </tr>
        <tr>
            <td>4C +21.35</td>
            <td>186.23</td>
            <td>21.38</td>
            <td>2010.06</td>
            <td>FRSQ</td>
        </tr>
        <tr>
            <td>PKS 1441+25</td>
            <td>220.99</td>
            <td>25.03</td>
            <td>2015.04</td>
            <td>FRSQ</td>
      </tr>
    </tbody>
</table>

#### <u>Why High Activity Sources:</u>

Higher activity implies more events. More events means the likelihood analysis giving more accurate results and also more scope to identify more correlation between events.

### <u>Extracting Data</u>:

To extract data we have to first visit the [client side web application of Fermi LAT server](https://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi). There we will have to fill up the expected information. Like in the following form.

<form method="post" action="/cgi-bin/ssc/LAT/LATDataQuery.cgi" enctype="multipart/form-data">
<input value="query" name="destination" type="hidden"><table><tbody><tr><td><a target="HelpWindow" href="http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#objectNameOrCoordinates"><b>Object name or coordinates:</b></a></td><td><input value="" name="coordfield" type="text"></td></tr><tr><td><a target="HelpWindow" href="http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#coordinateSystem"><b>Coordinate system:</b></a></td><td><select name="coordsystem"><option>J2000</option><option>B1950</option><option>Galactic</option></select></td></tr><tr><td><a target="HelpWindow" href="http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#searchRadius"><b>Search radius (degrees):</b></a></td><td><input value="" name="shapefield" type="text"></td></tr><tr><td><a target="HelpWindow" href="http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#observationDates"><b>Observation dates:</b></a></td><td><input value="" name="timefield" type="text"></td></tr><tr><td><a target="HelpWindow" href="http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#timeSystem"><b>Time system:</b></a></td><td><select name="timetype"><option>Gregorian</option><option>MET</option><option>MJD</option></select></td></tr><tr><td><a target="HelpWindow" href="http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#energyRange"><b>Energy range (MeV):</b></a></td><td><input value="" name="energyfield" type="text"></td></tr><tr><td><a target="HelpWindow" href="http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#LATdataType"><b>LAT data type:</b></a></td><td><select name="photonOrExtendedOrNone"><option>Photon</option><option>Extended</option><option>None</option></select></td></tr><tr><td><a target="HelpWindow" href="http://fermi.gsfc.nasa.gov/ssc/LATDataQuery_help.html#spacecraftData"><b>Spacecraft data:</b></a></td><td><input checked="checked" name="spacecraft" id="spacecraft" type="checkbox"></td></tr></tbody></table></form>

#### <u><b>Explanation</b></u>:

Here we can see different objects require different measurement system.  <b>J2000</b> refers to the celestial RA/Dec coordinate system for measuring position of the stars and astronomic/astrophysical objects modified after Gregorian calendar year 2000. <b>B1950</b> is for the same but for the period of 1950-1999. <b>Galactic</b> refers to the galactic latitude and longitude positioning system. <b>MJD</b> is <b>Modified Julian Dates</b>, where Julian dates are converted to seconds. <b>MET</b> is <b>Mission Elapse Time</b> i.e. the time elapse since the Fermi LAT started it's orbit in seconds. MET is the standard time measurement unit for Fermi Analysis.

This tool called [xTime](https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/xTime/xTime.pl) can help convert between different time units.

<mark style="background-color: #89b4fa">N.B.- you should keep a record of your search query, like the following.</mark>

<table class="center" summary="Query  Data for 4C +21.35" width="100%">
    <tbody>
    <tr>
        <th colspan="2">Query  Data for 4C +21.35</th>
        <tr>
            <td>Equatorial coordinates (degrees)</td>
            <td>(186.23,21.83)</td>
        </tr>
        <tr>
            <td>Time range (MET)</td>
            <td>(239557417,346982402)</td>
        </tr>
        <tr>
            <td>Time range (Gregorian)</td>
            <td>(2008-08-04 15:43:36,2011-12-31 00:00:00)</td>
        </tr>
        <tr>
            <td>Energy range (MeV)</td>
            <td>(100, 500000)</td>
        </tr>
        <tr>
            <td>Search radius (degrees)</td>
            <td>15</td>
        </tr>
    </tr>
    </tbody>
</table>

### <u>Analysis:</u>

To run the analysis, you obviously need the Fermi software tools. You can download it using conda. To install, run the following:

```shell
$ conda create -n fermi -c conda-forge -c fermi fermitools
```

To activate Fermitools use
`conda activate fermi`
And to exit Fermi use
`conda deactivate`
To work more efficiently you need a few more tools like

* To run in Jupyter notebooks, you will need the nb_conda package
  
  ```shell
  $ conda install -c conda-forge nb_conda
  ```

* To create XML files of your data for model likelihood analysis on Fermitools you will need [make4FGLxml.py](https://fermi.gsfc.nasa.gov/ssc/data/analysis/user/make4FGLxml.py)

* We should also install ds9 to view the fits files. To install the ds9 software first go to the [SAOImageDS9](https://sites.google.com/cfa.harvard.edu/saoimageds9) site and download the TAR file. As the version for Ubuntu 22 is not released yet, you can just download the file for version 20. For Fedora, it's only been updated till Fedora 33, let's try Fedora 37 when it's released. Extract the TAR file. In your command line go to the extracted directory and give sudo permission
  
  ```shell
  $ sudo -s
  $ mv ds9 /usr/local/bin
  $ chmod +x /usr/local/bin/ds9
  ```
  
  Then run the program from command line
  
  ```shell
  $ ds9
  ```

* If you want a more advanced likelihood option, you can also use [Fermipy](https://fermipy.readthedocs.io/en/latest/)
  
  ```shell
  $ conda install -c conda-forge fermipy
  ```

#### Using CLI:

When we extract the data from Fermi LAT servers, we might get several photon files, in that case, we have to do the following:

```shell
$ ls *_PH* > events.txt
```

Choose the filename based on your preference and context. E.g.- for binned analysis it can be

```shell
$ ls *_PH* > binned_events.txt
```

or for unbinned analysis

```shell
$ ls *_PH* > unbinned_events.txt
```

When analyzing point sources, it is recommended that you include events with high probability of being photons. To do this, you should use gtselect to cut on the event class, keeping only the SOURCE class events. In addition, since we do not wish to cut on any of the three event types (conversion type, PSF, or EDISP), we will use evtype=3. <mark style="background-color: #89b4fa">Note that "INDEF" is the default for evtype in gtselect.</mark>

<table class="styled-table" summary="Standard Hierarchy for LAT Event Classes" width="100%">
    <tbody>
        <tr>
            <th class="center" colspan="5" width="100%">Standard Hierarchy for LAT Event Classes</th>
        </tr><tr>
        </tr><tr>
            <th width="16%">Event Class</th>
            <th width="8%">evclass</th>
            <th width="10%">Photon File</th>
            <th width="12%">Extended File</th>
            <th width="40%">Description</th>
        </tr>
<!--        <tr>
            <td>P8R3_TRANSIENT100</td>
            <td>4</td>
            <td class="center"> </td>
            <td class="center"> </td>
            <td>Loosest transient event class with background rate equal to ten times the A10 reference spectrum. This event class has a residual background rate that is comparable to P7REP_TRANSIENT. This event class is not included in either the Extended or Photon data files.</td>
        </tr>  -->
        <tr>
            <td>P8R3_TRANSIENT020</td>
            <td>16</td>
            <td class="center"> </td>
            <td class="center">X</td>
            <td>Transient event class with background rate equal to two times the A10 IGRB reference spectrum.</td>
        </tr>
        <tr>
            <td>P8R3_TRANSIENT010</td>
            <td>64</td>
            <td class="center"> </td>
            <td class="center">X</td>
            <td>Transient event class with background rate equal to one times the A10 IGRB reference spectrum.</td>
        </tr>
        <tr>
            <td>P8R3_SOURCE</td>
            <td>128</td>
            <td class="center">X</td>
            <td class="center">X</td>
            <td>This event class has a residual background rate that is comparable to P7REP_SOURCE. This is the recommended class for most analyses and provides good sensitivity for analysis of point sources and moderately extended sources.</td>
        </tr>
        <tr>
            <td>P8R3_CLEAN</td>
            <td>256</td>
            <td class="center">X</td>
            <td class="center">X</td>
            <td>This class is identical to SOURCE below 3 GeV. Above 3 GeV it has a 1.3-2 times lower background rate than SOURCE and is slightly more sensitive to hard spectrum sources at high galactic latitudes.</td>
        </tr>
        <tr>
            <td>P8R3_ULTRACLEAN</td>
            <td>512</td>
            <td class="center">X</td>
            <td class="center">X</td>
            <td>This class has a background rate very similar to ULTRACLEANVETO.</td>
        </tr>
        <tr>
            <td>P8R3_ULTRACLEANVETO</td>
            <td>1024</td>
            <td class="center">X</td>
            <td class="center">X</td>
            <td>This is the cleanest Pass 8 event class.  Its background rate is 15-20% lower than the background rate of SOURCE class below 10 GeV, and 50% lower at 200 GeV. This class is recommended to check for CR-induced systematics as well as for studies of diffuse emission that require low levels of CR contamination.</td>
        </tr>
        <tr>
            <td>P8R3_SOURCEVETO</td>
            <td>2048</td>
            <td class="center">X</td>
            <td class="center">X</td>
            <td>This class has the same background rate than the SOURCE class background rate up to 10 GeV but, above 50 GeV, its background rate is the same as the ULTRACLEANVETO one while having 15% more acceptance.</td>
        </tr>        
        <tr>
            <th class="center" colspan="5">Extended Hierarchy</th>
        </tr><tr>
        </tr><tr>
            <th>Event Class</th>
            <th>evclass</th>
            <th>Photon File</th>
            <th>Extended File</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>P8R3_TRANSIENT020E</td>
            <td>8</td>
            <td class="center"> </td>
            <td class="center">X</td>
            <td>Extended version of the P8R3_TRANSIENT020 event class with a less restrictive fiducial cut on projected track length through the Calorimeter.</td>
        </tr>
        <tr>
            <td>P8R3_TRANSIENT010E</td>
            <td>32</td>
            <td class="center"> </td>
            <td class="center">X</td>
            <td>Extended version of the P8R3_TRANSIENT010 event class with a less restrictive fiducial cut on projected track length through the Calorimeter.</td>
        </tr>
        <tr>
            <th class="center" colspan="5">NON-ACD Hierarchy</th>
        </tr><tr>
        </tr><tr>
            <th>Event Class</th>
            <th>evclass</th>
            <th>Photon File</th>
            <th>Extended File</th>
            <th>Description</th>
        </tr>
<!--        <tr>
            <td>P8R3_TRANSIENT100S</td>
            <td>32768</td>
            <td class="center"> </td>
            <td class="center"> </td>
            <td>Transient event class designed for analysis of prompt solar flares in which pileup activity may be present. This event class has a residual background rate that is comparable to P7REP_TRANSIENT. This event class is not included in either the Extended or Photon data files.</td>  -->
        <tr>
            <td>P8R3_TRANSIENT015S</td>
            <td>65536</td>
            <td class="center"> </td>
            <td class="center">X</td>
            <td>Transient event class designed for analysis of prompt solar flares in which pileup activity may be present. This class has a background rate equal to 1.5 times the A10 reference spectrum.</td>
        </tr>
    </tbody>
</table>

<table class="styled-table" summary="Event Type Partitions" width="100%">
    <tbody>
        <tr>
            <th class="center" colspan="3" width="100%">Conversion Type Partition</th>
        </tr>
        <tr>
            <th width="16%">Event Type</th>
            <th width="8%">evtype</th>
            <th width="76%">Description</th>
        </tr>
        <tr>
            <td>FRONT</td>
            <td>1</td>
            <td>Events converting in the Front-section of the Tracker. Equivalent to convtype=0.</td>
        </tr>
        <tr>
            <td>BACK</td>
            <td>2</td>
            <td>Events converting in the Back-section of the Tracker. Equivalent to convtype=1.</td>
        </tr>
        <tr>
            <td>FRONT & BACK</td>
            <td>3</td>
            <td>Events converting in the Front-and-Back section of the Tracker.</td>
        </tr>
        <tr>
            <th class="center" colspan="3" width="100%">PSF Type Partition</th>
        </tr>
        <tr>
            <th>Event Type</th>
            <th>evtype</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>PSF0</td>
            <td>4</td>
            <td>First (worst) quartile in the quality of the reconstructed direction.</td>
        </tr>
        <tr>
            <td>PSF1</td>
            <td>8</td>
            <td>Second quartile in the quality of the reconstructed direction.</td>
        </tr>
        <tr>
            <td>PSF2</td>
            <td>16</td>
            <td>Third quartile in the quality of the reconstructed direction.</td>
        </tr>
        <tr>
            <td>PSF3</td>
            <td>32</td>
            <td>Fourth (best) quartile in the quality of the reconstructed direction.</td>
        </tr>
        <tr>
            <th class="center" colspan="3" width="100%">EDISP Type Partition</th>
        </tr>
        <tr>
            <th>Event Type</th>
            <th>evtype</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>EDISP0</td>
            <td>64</td>
            <td>First (worst) quartile in the quality of the reconstructed energy.</td>
        </tr>
        <tr>
            <td>EDISP1</td>
            <td>128</td>
            <td>Second quartile in the quality of the reconstructed energy.</td>
        </tr>
        <tr>
            <td>EDISP2</td>
            <td>256</td>
            <td>Third quartile in the quality of the reconstructed energy.</td>
        </tr>
        <tr>
            <td>EDISP3</td>
            <td>512</td>
            <td>Fourth (best) quartile in the quality of the reconstructed energy.</td>
        </tr>
    </tbody>
</table>

Check out this <a href="https://fermi.gsfc.nasa.gov/ssc/data/analysis/documentation/Cicerone/Cicerone_Data/LAT_DP.html"><b>website</b></a> for any kind of confusion.

#### Making cuts using the events file keywords

Applying selection cuts to the LAT data is typically performed using select, and is documented in detail within the data exploration analysis thread. Typically cuts are made to bound the dataset's time range, energy range, position, region of interest radius, and maximum zenith angle. The maximum zenith angle selection is designed to exclude time periods when any portion of the region of interest is too close to the Earth's limb, resulting in elevated background levels. The Earth's limb lies at a zenith angle of 113 degrees, so a suggested value of 90 provides protection against significant contamination by atmospheric gammas. (NOTE: This cut requires careful handling when calculating livetime, which is discussed in detail in the Likelihood Livetime and Exposure section.).

Additionally, gtselect can be used to include/exclude events which have a higher/lower probability of being photons. The recommended class of events to use depends on the analysis in question. The LAT teams recommendations are listed in the "Event Selection Recommendations" table above. The instrument response functions used in the analysis tools must match the event classes selected.

The reconstruction and classification of LAT events is performed by the LAT instrument team as part of the Level 1 science data processing. The version of the event reconstruction algorithms used is referred to as Pass N. Currently, the LAT data pipeline uses Pass 8 (P8R3) algorithms. This processing is inherent in the science data, and cannot be changed. For a given reconstruction, the LAT team generates an accompanying set of parameterized <u>instrument response functions</u> (IRFs) that are designed for analysis of that particular dataset, these are labeled VN (where N is the version of the IRF). There may be several updates of IRFs for a given reconstruction, with one recommended for analysis (currently P8R3_CLASS_V3). The IRFs selected later in the analysis chain must match the data reconstruction version (currently Pass 8) and the event class selected at this stage, i.e. P8R3_SOURCE_V3 for a point source analysis. A more detailed discussion can be found in the LAT Response Functions section of the Cicerone.

The acceptance cone radius will vary with analysis type and source location. Performing a spectral analysis on a point source in the galactic plane will require a larger initial analysis region than for a source off the plane, to allow for fitting of multiple nearby sources. An acceptance cone radius of 10 deg is appropriate for spectral analysis of point sources off the Galactic plane, while 10-20 deg may be necessary for point sources located near the Galactic Plane. A timing analysis that does not use spectral modelling (for example, pulsar lightcurves) might select a smaller region to reduce background levels. These studies (timing analysis, GRB spectral analysis, extended source analysis, and others) require optimization of the acceptance cone on a case-by-case basis. Such optimization will need to consider the largest PSF of the LAT in the energy range of interest, as well as providing sufficient statistics to account for the surrounding sky structure. An all-sky analysis does not require this selection.

#### Event Selection Recommendations (P8R3)

<table class="styled-table" summary="Recommended Parameter Values for LAT Data Selection" width="100%">
    <tbody>
        <tr>
            <th width="16%">Analysis Type</th>
            <th width="14%">Minimum Energy<br>(emin)</th>
            <th width="14%">Maximum Energy<br>(emax)</th>
            <th width="14%">Max Zenith Angle<br>(zmax)</th>
            <th width="14%">Event Class<br>(evclass)</th>
            <th width="14%">IRF Name</th>
        </tr>
        <tr>
            <td>Galactic Point Source Analysis</td>
            <td class="center">100 (MeV)</td>
            <td class="center">1000000 (MeV)</td>
            <td class="center">90 (degrees)</td>
            <td class="center">128</td>
            <td class="center">P8R3_SOURCE_V3</td>
        </tr>
        <tr>
            <td>Off-plane Point Source Analysis</td>
            <td class="center">100 (MeV)</td>
            <td class="center">1000000 (MeV)</td>
            <td class="center">90 (degrees)</td>
            <td class="center">128</td>
            <td class="center">P8R3_SOURCE_V3</td>
        </tr>
        <tr>
            <td>Burst and Transient Analysis (<200s)</td>
            <td class="center">100 (MeV)</td>
            <td class="center">1000000 (MeV)</td>
            <td class="center">100 (degrees)</td>
            <td class="center">16</td>
            <td class="center">P8R3_TRANSIENT020_V3</td>
        </tr>
        <tr>
            <td>Galactic Diffuse Analysis</td>
            <td class="center">100 (MeV)</td>
            <td class="center">1000000 (MeV)</td>
            <td class="center">90 (degrees)</td>
            <td class="center">128</td>
            <td class="center">P8R3_SOURCE_V3</td>
        </tr>
        <tr>
            <td>Extra-Galactic Diffuse Analysis</td>
            <td class="center">100 (MeV)</td>
            <td class="center">1000000 (MeV)</td>
            <td class="center">90 (degrees)</td>
            <td class="center">1024</td>
            <td class="center">P8R3_ULTRACLEANVETO_V3 or P8R3_SOURCEVETO_V3 (when interested in E>1 GeV energy range)</td>
        </tr>
        <tr>
            <td>Impulsive Solar Flare Analysis</td>
            <td class="center">100 (MeV)</td>
            <td class="center">1000000 (MeV)</td>
            <td class="center">100 (degrees)</td>
            <td class="center">65536</td>
            <td class="center">P8R3_TRANSIENT015S_V3</td>
        </tr>
    </tbody>
</table>

We will now apply the [gtselect](https://raw.githubusercontent.com/fermi-lat/fermitools-fhelp/master/fhelp_files/gtselect.txt) tool to the data files.
```shell
$ gtselect evclass=128 evtype=3
Input FT1 file[] @binned_events.txt
Output FT1 file[] 3C279_binned_filtered.fits
RA for new search center (degrees) (0:360) [] INDEF
Dec for new search center (degrees) (-90:90) [] INDEF
radius of new search region (degrees) (0:180) [] INDEF
start time (MET in s) (0:) [] INDEF
end time (MET in s) (0:) [] INDEF
lower energy limit (MeV) (0:) [] 100
upper energy limit (MeV) (0:) [] 500000
maximum zenith angle value (degrees) (0:180) [] 90
Done.
```

#### Making cuts using the spacecraft file keywords
The spacecraft files are used to select the good time intervals (GTIs) for data analysis by using gtmktime. Selecting times when the data quality is good (DATA_QUAL>0) will exclude time periods when some spacecraft event has affected the quality of the data. gtmktime can be used to generate and combine GTIs for any logical expression of keywords in the spacecraft file. Contamination from albedo gamma rays from the Earth is reduced by applying an additional timing selection to the maximum zenith angle cut made with gtselect. Excluding time intervals when the Earth's limb intersects the selected region of interest is one method of correcting the exposure for the zenith cut. This is accomplished by using the ROIcut=yes option in gtmktime. For other exposure correction options, see the Likelihood Livetime and Exposure section.

##### Some possible quantities for filtering data are:
- DATA_QUAL - quality flag set by the LAT instrument team (1 = ok, 2 = waiting review, 3 = good with bad parts, 0 = bad)
- LAT_CONFIG - instrument configuration (0 = not recommended for analysis, 1 = science configuration)
- ROCK_ANGLE - can be used to eliminate pointed observations from the dataset.

#### Time Selection Recommendations
<table class="styled-table" summary="Recommended Parameter Values for LAT Data Selection" bwidth="100%">
	<tbody>
		<tr>
			<th width="34%">Analysis Type</th>
			<th width="25%">ROI-Based Zenith Angle Cut<br>(roicut)</th>
			<th width="41%">Relational Filter Expression<br>(filter)</th>
		</tr>
		<tr>
			<td>Galactic Point Source Analysis</td>
			<td class="center">no</td>
			<td class="center">(DATA_QUAL&gt;0)&amp;&amp;(LAT_CONFIG==1)</td>
		</tr>
		<tr>
			<td>Off-plane Point Source Analysis</td>
			<td class="center">no</td>
			<td class="center">(DATA_QUAL&gt;0)&amp;&amp;(LAT_CONFIG==1)</td>
		</tr>
		<tr>
			<td>Burst and Transient Analysis</td>
			<td class="center">yes</td>
			<td class="center">(DATA_QUAL&gt;0)&amp;&amp;(LAT_CONFIG==1)</td>
		</tr>
		<tr>
			<td>Galactic Diffuse Analysis</td>
			<td class="center">no</td>
			<td class="center">(DATA_QUAL&gt;0)&amp;&amp;(LAT_CONFIG==1)</td>
		</tr>
		<tr>
			<td>Extra-Galactic Diffuse Analysis</td>
			<td class="center">no</td>
			<td class="center">(DATA_QUAL&gt;0)&amp;&amp;(LAT_CONFIG==1)</td>
		</tr>
		<tr>
			<td>Burst and Transient Analysis</td>
			<td class="center">yes</td>
			<td class="center">(DATA_QUAL&gt;0||DATA_QUAL==-1)&amp;&amp;(LAT_CONFIG==1)</td>
		</tr>
	</tbody>
</table>

Now we will perform the the ***good time interval*** using [gtmktime](https://raw.githubusercontent.com/fermi-lat/fermitools-fhelp/master/fhelp_files/gtmktime.txt) tool.
```shell
$ gtmktime
Spacecraft data file[] L181126210218F4F0ED2738_SC00.fits
Filter expression[] (DATA_QUAL>0)&&(LAT_CONFIG==1)
Apply ROI-based zenith angle cut[] no
Event data file[] 3C279_binned_filtered.fits
Output event file name[] 3C279_binned_gti.fits
```

To view the DSS keyword, you can use the [gtvcut](https://raw.githubusercontent.com/fermi-lat/fermitools-fhelp/master/fhelp_files/gtvcut.txt) tool and review the datacuts.
```shell
$ gtvcut 3C279_binned_gti.fits
Extension name[EVENTS]
DSTYP1: BIT_MASK(EVENT_CLASS,128,P8R3)
DSUNI1: DIMENSIONLESS
DSVAL1: 1:1

DSTYP2: POS(RA,DEC)
DSUNI2: deg
DSVAL2: CIRCLE(193.98,-5.82,15)

DSTYP3: TIME
DSUNI3: s
DSVAL3: TABLE
DSREF3: :GTI

GTIs: (suppressed)

DSTYP4: BIT_MASK(EVENT_TYPE,3,P8R3)
DSUNI4: DIMENSIONLESS
DSVAL4: 1:1

DSTYP4: ENERGY
DSUNI4: MeV
DSVAL4: 100:500000

DSTYP5: ZENITH_ANGLE
DSUNI5: deg
DSVAL5: 0:90
```

We will now make a counts map using [gtbin](https://raw.githubusercontent.com/fermi-lat/fermitools-fhelp/master/fhelp_files/gtbin.txt)
```shell
$ gtbin
Type of output file (CCUBE|CMAP|LC|PHA1|PHA2|HEALPIX) [PHA2] CMAP
Event data file name[] 3C279_binned_gti.fits
Output file name[] 3C279_binned_cmap.fits
Spacecraft data file name[] NONE
Size of the X axis in pixels[] 150
Size of the Y axis in pixels[] 150
Image scale (in degrees/pixel)[] 0.2
Coordinate system (CEL - celestial, GAL -galactic)[] CEL
First coordinate of image center in degrees (RA or galactic l)[] 193.98
Second coordinate of image center in degrees (DEC or galactic b)[] -5.82
Rotation angle of image axis, in degrees[] 0.0
Projection method Projection method e.g. AIT|ARC|CAR|GLS|MER|NCP|SIN|STG|TAN:[] AIT
gtbin: WARNING: No spacecraft file: EXPOSURE keyword will be set equal to ontime.
```

```shell
$ ds9 3C279_binned_cmap.fits
```
With this we can view the fits file in a GUI.

![fits preview](/home/ray/Documents/Fermi/ds9_pre.png)

#### Using Python Library
