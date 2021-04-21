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
  - Note: after installing, hit the button that looks like a "refresh" icon to update the package repository so VIPM will work correctly.   

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
  - Note: If the program fails to launch, [try the solution mentioned here](https://portal.hdfgroup.org/display/support/HDFView+3.1.2#HDFView3.1.2-knownprobs). 
   
    To make the HDFViewApp-3.1.2 work on Windows 10 (64 bits), they ask you to download and paste the `hdfview.bat` file here:

      <img src="./readme_img/hdf_fix.PNG" width="60%">

    Then the app can be opened by double clicking on that `hdfview.bat` file.

# Testing the VI

## Verify Acoular installation
After going through the [installation described here](http://www.acoular.org/install/index.html), you should be able to: 
- open the Anaconda prompt
- type `python` to open the python interpreter
- type the statements shown here and get the following results:

![acoular_example](./readme_img/acoular_test.PNG)

## Run the provided example

To test your environment, an example measurement is provided. This includes an image and a white-noise recording in an hdf5 file.

- Open the project **`development_version/Beamforming_0_0_1.lvproj`**. In there open the VI called **`BeamformerGUI_GivenFreqs.vi`** and execute it.

- Switch from the `Measurement` tab to the `Processing` tab.
  
  - The Python server should be started in the background, give it some time. When the VI is ready to perform an analysis, it looks like this:
  
    <img src="./readme_img/ready.PNG" width="80%"> 

  - By default, the VI already searches for the microphone geometry file `16_mics_geom.xml` in the `development_version/xml` folder. If you ever need to include another microphone geometry file, that is the place to add it.

  - For the `Audio Data File (HDF5)` option, make sure it points to: `development_version/experiments/example_1.h5` (should be done by default too, but please double check).
  
    - Inspecting it with HDFView:
    
      <img src="./readme_img/hdf_view.PNG" width="70%">
    
    - Inspecting it with the `Inspect Signal` function:
  
      <img src="./readme_img/inspect.PNG" width="80%">

    - Click on `Run Analysis` and you should get this message:
  
      <img src="./readme_img/success.PNG" width="80%">

      And the following plot:

      <img src="./readme_img/example_plot.PNG" width="80%">
