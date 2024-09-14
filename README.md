# University-Projects
Python code written for use in my studies, usually to analyse data and plot graphs. The codes are not optimised, and are probably not written with the best practices. 

## UV-Vis
For use when extracting data from UV-Vis spectroscopy. Data was from SpectraSuite. The experiment was on investigating the emission spectra resulting from computer and phone screens, where three distinct peaks (corresponding to red, green, and blue light) would appear. Gaussians are fitted to these three peaks and peak intensities are extracted.

## Surface Brightness Profiles
#### Background
[GAIA](https://astro.dur.ac.uk/~pdraper/gaia/gaia.html) was used for a 6-week astronomy project, where surface photometry was done on images of galaxies using elliptical apertures.

The Sersic function describes the light profile of a galaxy, and is given by


The code was written to plot the files and fit them to the above function to extract the Sersic index n (degree of curvature of the function). The allows the formation process of a galaxy to be inferred, where a higher Sersic index indicates a more centrally-concentrated light profile and a more violent history, such as formation through galaxy mergers. A smaller Sersic index has a more "smoother" profile, indicating a slower and less violent process, such as through gas accretion.

#### Code
Multiple variations of the code allow for either plotting of multiple files or to plot different fits across a specific range. Some code is for error analysis.


#### Results and Further Work
It was found that elliptical galaxies and the bulges of spiral galaxies tended to have higher Sersic values than the outskirts of spirals, indicating different formstion processes. When comparing to literature, many values of the Sersic index agreed (especially for ellipticals and the outskirts). However, the bulges of spirals have different values depending on their classification, and the code here cannot distinguish between them. Altering the code such that the function is a sum of the bulge and outskirt components (rather than taking each part individually) may resolve this.

I learnt a lot more about plotting with matplotlib with this project - the presentation of my graphs have massively improved compared to my previous ones.  There are many improvements I could make to the code though.

The code itself is not optimised, and the various notebooks could be merged together into one with a little work. I did not use the pandas library for reading the data files, and I'd imagine that using it would make things a lot easier to work with as well as making the code more readable.
