# UV-Vis Project
Academic project was on investigating optical spectroscopy. This code was written up to analyse the emission spectra of electronic screens (e.g. computer, phone), where three distinct peaks would appear (corresponding to red, green, and blue light). Gaussians were fitted to these peaks and their peak intensities were extracted.
Data was from using SpectraSuite software (results as a .txt file).

## Examples
### White on a Phone Screen
Data: phone_white.txt

The below are graphs produced of the colour white on a phone screen. The first is simply just the data, the second showcases the fitting.

![White_Phone](https://github.com/kly-zhou/University-Projects/assets/155482955/c6a28b1f-55fe-43f4-b9c2-ae91c85d3558)
![White_Phone_Fit](https://github.com/kly-zhou/University-Projects/assets/155482955/987304f2-fc92-49ec-a373-3eb72f467109)

The intensities extracted are as follows:
* Red: 36499
* Green: 32614
* Blue: 28427

### Cyan on a Computer Screen
Data: computer_cyan.txt

Cyan on a computer screen is shown below with the fit as well as individual gaussian components (Note: only two peaks as cyan is comprised of just green and blue).

![Cyan_Computer_Fit](https://github.com/kly-zhou/University-Projects/assets/155482955/11c1abbf-7d2e-414c-bcee-157644c278a3)
![Cyan_Computer](https://github.com/kly-zhou/University-Projects/assets/155482955/ea0629f3-6ca5-456e-8a03-ab0b18708e56)

With the intensities as:
* Red: 434
* Green: 17775
* Blue: 31947

With more broader spectra, the code can fail to distinguish between the peaks. Spectra are also not perfect gaussians, so there will be some deviation between the data and the fit.
