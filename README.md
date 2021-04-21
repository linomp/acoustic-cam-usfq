# Dependencies

**Important**: Install all of these packages/tools **in the same order** as they appear.

### Python
- [Anaconda3 (2019.07 build)](https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe)
- [The acoular library](http://www.acoular.org/)
  - Note: make sure you go through their `Installation` and `Getting Started` sections to verify your installation is correct.

### LabView 
- LabView 2017 SP1 
  - Note: uncheck the VI Package Manager 2017 option; the latest version directly from their website works better.  
- [VI Package Manager (VIPM)](https://www.vipm.io/download/)
  - Note: hit the button that looks like a "refresh" icon, to update the package repository so VIPM will work correctly.   

It is recommended to install these packages with VIPM, in this exact order:
- [OpenG Libraries](https://www.vipm.io/package/openg.org_lib_openg_toolkit/)   
- [LiveHDF by UPVI](https://www.vipm.io/package/lvhdf5/) ([documentation](http://www.upvi.net/main/index.php/products/lvhdf5))

At this point, your installed package listing should contain at least all these:

<img src="./readme_img/vipm_packages.PNG" width="60%">

These ones are installed from outside VIPM:
- [NI DAQmx](https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html#348669) for microphone data acquisition
- [VAS](https://www.ni.com/en-us/support/downloads/drivers/download.vision-acquisition-software.html#367318) for LabView to webcam interfacing

### Recommended
- [HDFView](https://www.hdfgroup.org/downloads/hdfview/) to inspect HDF5 files of your audio recordings and their metadata.



# Testing the VI

## Verify Acoular installation
After going through the [installation described here](http://www.acoular.org/install/index.html), you should be able to open the Anaconda prompt, input these commands and get the following results:

![acoular_example](./readme_img/acoular_test.PNG)

## Run the provided example

// TO-DO add instructions & screenshots
Switch from the Measurement tab to the Processing tab...
- Image File: `development_version/experiments/example_1.bmp`
- Audio File: `development_version/experiments/example_1.h5`
