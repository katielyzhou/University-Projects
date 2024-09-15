# University-Projects
Python code written for use in my studies, usually to analyse data and plot graphs. The codes are not optimised, and are probably (most definitely) not written with the best practices. Apologies in advance for the amateur code.

## UV-Vis
### Background
UV-Vis spectroscopy is a method in analytical chemistry used for recording the absorbance and emission spectra of chemicals. I had a three week experiment on investigating if [RGB colour codes](https://en.wikipedia.org/wiki/RGB_color_model#Numeric_representations) could be extracted from the emission spectra from a computer screen, where I prepared code for extracting the data from a .txt file from SpectraSuite. Three distinct peaks (corresponding to red, green, and blue light) would appear in the spectra. Gaussians are fitted to these peaks and peak intensities are extracted. The ratio of the peak intensities are correlated to RGB colour codes.

### Code
The code takes in a file, and starting parameters may be varied for the fits to the three peaks.

### Examples
#### White on a Phone Screen
Data: phone_white.txt

The below are graphs produced of the colour white on a phone screen. The first is simply just the data, the second showcases the fitting.

![White_Phone](https://github.com/kly-zhou/University-Projects/assets/155482955/c6a28b1f-55fe-43f4-b9c2-ae91c85d3558)
![White_Phone_Fit](https://github.com/kly-zhou/University-Projects/assets/155482955/987304f2-fc92-49ec-a373-3eb72f467109)

The intensities extracted are as follows:
* Red: 36499
* Green: 32614
* Blue: 28427

#### Cyan on a Computer Screen
Data: computer_cyan.txt

Cyan on a computer screen is shown below with the fit as well as individual gaussian components (Note: only two peaks as cyan is comprised of just green and blue).

![Cyan_Computer_Fit](https://github.com/kly-zhou/University-Projects/assets/155482955/11c1abbf-7d2e-414c-bcee-157644c278a3)
![Cyan_Computer](https://github.com/kly-zhou/University-Projects/assets/155482955/ea0629f3-6ca5-456e-8a03-ab0b18708e56)

With the intensities as:
* Red: 434
* Green: 17775
* Blue: 31947

### Comments and Further Work
With more broader spectra, the code can fail to distinguish between the peaks. Spectra are also not perfect gaussians, so there will be some deviation between the data and the fit. For general improvements to the code, using the pandas library may be more efficient.

## Surface Brightness Profiles
### Background
[GAIA](https://astro.dur.ac.uk/~pdraper/gaia/gaia.html) was used for a 6-week astronomy project, where surface photometry was done on images of galaxies using elliptical apertures.

The Sersic function describes the light profile of a galaxy. The code was written to plot the files and fit them to the Sersic function to extract the Sersic index n (degree of curvature of the function). The allows the formation process of a galaxy to be inferred, where a higher Sersic index indicates a more centrally-concentrated light profile and a more violent history, such as formation through galaxy mergers. A smaller Sersic index has a more "smoother" profile, indicating a slower and less violent process, such as through gas accretion.

Galaxies studied in the project were: M81; M94; M101; NGC 2550A; NGC 7331; NGC1573; NGC3379; and NGC 1275.

### Code
As a lot of trial and error was done during the project, there were MANY variations of the code for plotting data (e.g. graph format or to test the effect of different parameters) as well as for error analysis. Three Jupyter Notebooks have been uploaded:

- Sersic_multiple_galaxies: fits the light profile of galaxies to the Sersic function and produces a graph of this with normalised residuals.
- Sersic_NGC2550A: fits the light profile of the bulge and the disc of spiral galaxy NGC2550A to the Sersic function, as well as producing a lag plot.
- Sersic_LagPlots: [Lag plots](https://www.statisticshowto.com/lag-plot/) on the fits to some galaxies.

### Examples
Example data is stored in 'katiestack'.

<img src="https://github.com/user-attachments/assets/99e9f105-8bdc-42d2-91cd-7abca64a7c04" width="400">

Surface brightness profiles of elliptical galaxies and the bulges of spiral galaxies, with their residuals. The error bars represent 3σ. The shaded region represents 1σ. There are anomalous data points towards the centre, where their residuals are greater than the scale shown.


<img src="https://github.com/user-attachments/assets/de7fbb1f-f0f5-4cf4-886f-9af592669b96" width="400">

Comparison of with a logarithmic scale and without for the radius. Orange is the fit for the bulge and green the disc.


<img src="https://github.com/user-attachments/assets/807a9fc8-4e36-4788-bdb8-7edde2410a4a" width="400">

Lag plots for selected galaxies: (a) NGC 2550A bulge; (b) M101 disc; (c) NGC3379; and (d) NGC 1275. The shaded region represents 2σ. *i* and *i - 1* refer to a data point and its previous point. A positive correlation can be seen in (d), indicating the fit was not the best.


### Comments and Further Work
Spiral galaxies have two main components: the bulge and the disc. The code took these two components individually, leading to results that were not perfectly accurate - altering the code such that the function is a sum of the two components (rather than taking each part individually) may improve accuracy.

I learnt a lot more about plotting with matplotlib with this project - the presentation of my graphs have massively improved compared to my previous ones.  There are many improvements I could make to the code though. The code itself is not optimised, and the various notebooks could be merged together into one with a little work. I did not use the pandas library for reading the data files, and I'd imagine that using it would make things a lot easier to work with as well as making the code more readable.
