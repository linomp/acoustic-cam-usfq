Live HDF5 Toolkit Version 1.1.1.86
Copyright (c) 2005-2013 by Jason D. Sommerville
Copyright (c) 2014-2015 by UPVI, LLC.
www.upvi.net

PLEASE SEE "6. UPGRADE FROM PRIOR VERSION" IF UPGRADING THE TOOLKIT.

0. Introduction

This toolkit provides a (nearly) complete interface between LabVIEW and the HDF5 scientific data format. The toolkit will analyze the LabVIEW data types connected to the write functions and create corresponding HDF5 datatypes in which to store the wired data. During read, the data may be read back into the same datatype or, alternatively, into a LabVIEW variant. With care and a deep understanding of LabVIEW memory, the data may also be read into a different, compatible datatype.

The library provides both high-level read and write functions which handle most of the HDF5 nitty-gritty and lower-level functions for those with particular needs. It also provides a few utility functions, e.g. a VI to populate a LabVIEW Tree control with the directory structure of an HDF5 file. Beyond the high-level functions this library provides interfaces to most of the other HDF5 functions. For full details on the HDF5 format and its functions, please visit the HDF5 website at http://www.hdfgroup.org.

To get started using the toolkit, please see the User Manual in the detailed help file for the VIs and make use of the examples in the example folder (<LabVIEW directory>\examples\UPVI\LVHDF5).

1. License

See LICENSE.txt. Basically, you are allowed to use and modify this toolkit however you like within your organization. However, you may not distribute it for profit either as the toolkit or when included in an application. For such for-profit use, please contact UPVI to make arrangements. Distribution of any modified version of the toolkit, whether for profit or not is not allowed.

2. Philosophy and Technology

This toolkit attempts to make it as easy as possible to use the HDF5 library. It follows the standard paradigm of "open, read/write, close." Open a file, write a dataset, read a dataset, close the file. The magic happens during the reads and writes. During writes, the library will attempt to map the LabVIEW data type to a corresponding HDF5 data type. Integers -> integers, floats -> floats, clusters -> compounds, etc. If the library is unable to handle a particular data type, the write node will not allow you to wire the data type to the node--the wire will be broken. (If using the variant version of the node, a run-time error will occur.) The library is able to handle arbitrarily complex data types, including clusters, strings, clusters of clusters of strings, etc.

During read operations, much like a LabVIEW primitive node, the dataset and attribute nodes take a datatype input. If the datatype input is wired, the toolkit will attempt to cast the data in the HDF5 file to the datatype wired to the node. If it is unable to do so, a runtime error (or possibly crash) will occur. Typically, the same datatype used to write the dataset should be used on the read node input.

HDF5 is able to handle partial dataset reads (e.g., a portion of an array). Version 1.0 of the toolkit supports this feature. If a non-empty array is passed to the read node input, only the elements selected will be overwritten. Read up on HDF5 dataspaces for more information.

If the read node input is not wired, the toolkit will create the best LabVIEW data type match and return it in a variant containing that type. If an empty array is passed, LVHDF5 will allocate an array which matches the dataspace of the dataset or attribute being read.

LVHDF5 1.0 is currently only available for 32-bit Windows versions of LabVIEW. With assistance from those with access to other version of LabVIEW and a matching C compiler, support for other versions could be added.

3. Getting Started

The best way to get started is to read the User Manual portion of the help file. The help file is in Microsoft HTML Help format and is installed at

<LabVIEW>\help\UPVI\lvhdf5.chm

It is also accessible by pressing the detailed help button on the floating Context Help for any of the VIs.

After reading the User Manual, look at the examples in the <LabVIEW>\examples\UPVI\LVHDF5 directory. Start with these three:

basic\HDF5 Read and Write.vi 
basic\HDF5 Read and Write with Attributes.vi 
basic\HDF5 Logging with Unlimited Datasets.vi

then look at the rest. Also, please be sure to read up on the file format itself at www.hdfgroup.org/hdf5. It is also helpful to have HDFView, the HDF file viewer which can be downloaded from the same website.

4. A Note For People Familiar with the HDF5 C Library

To be "Compatible with LabVIEW" the functions appear in the palette and the help file with proper English names rather than the HDF5 function names. For example, "Write Dataset" rather than "H5Dwrite". If you are looking for a specific HDF5 function, the easiest way to find the function is to search the index of the help file. Additionally, most of the actual VI file names directly reflect the HDF5 function names.

5. Supported Datatypes

The following LabVIEW datatypes are supported in datasets and attributes:

Booleans (Stored as U8-derived committed datatype)
Integers (I8, I16, I32, I64, U8, U16 U32, U64)
Enumerations (U8, U16, U32 and U64)
Floating point (SGL, DBL, EXT)
Physical Quantity (SGL PQ, DBL PQ, EXT PQ: stored as committed datatype with unit information attached to type)
Complex (CSG, CDB, CXT: stored as compounds with real and imaginary members)
Complex Physical Quantities
Strings (May be stored as variable or fixed len. Defaults to variable length.)
Timestamps
HDF5 References
Clusters of the above types or 1-D arrays of the above types. Clusters may be nested.

6. Upgrading from prior versions

6.1 Upgrading from version 1.0

Greater effort was exerted to maintain compatibility between the 1.1 series and the 1.0 series. However, users of the 1.0 series will likely find two changes that lead to broken wires and annoyance.

1) Changes made in the connector panes of the xnodes (e.g. Simple H5Dwrite, etc.) may lead to broken VIs when the VIs developed with the old version are updated to use 1.1. Typically, these broken wires will remain exactly where they should be, but are simply not connected to the xnode. This makes fixing these issues easy--simply reconnect the wires.

2) Typedefs have been added to all File, Dataset, and Attribute behavior inputs (e.g. "Open, create, replace" etc.). Also, the terms "Replace or Create" and "Replace or Create with Confirmation" have been changed to the more correct and consistent "Create or Replace" and "Create or Replace with Confirmation". This may result in broken wires between operation constants or controls created with prior versions of the toolkit. Simply replace with the new constants or controls.

6.2 Upgrading from the version 0.9 series toolkit

Little effort was made to make this toolkit backwards compatible with the version 0.9 toolkit. While the vast majority of the VIs are identical, nearly all of the really important VIs have undergone changes, or been replaced by adaptive nodes. Thus, some amount of rework will be necessary, e.g. replacing the old "Simple H5Dwrite.vi" with the new "Simple H5Dwrite" node, etc. Additional changes are also imposed in some enumerations because of the change from version 1.6 of HDF5 to version 1.8. Most data files written with the 0.9 series should be readable by the 1.0 series toolkit.

The version 1.0 series solves the inefficiency problems of the version 0.9 series of the toolkit. Version 0.9 required that all data be flattened to strings before being written to HDF5 (and read operations created flattened strings), a process which was deleterious to both memory usage and speed. Version 1.0 avoids this and works directly with the raw data.

The other major change, of course, is the use of adaptive nodes which can check the compatibility of the wired datatype at edit time rather than run time.

7. HDF5 Version

The library ships with HDF5 version 1.8.13. You may upgrade this to later versions by replacing the files hdf5.dll and hdf5_hl.dll in the vi.lib/UPVI/lvhdf5 directory. Of course, such an upgrade is not guaranteed to function, but it probably will.

8. Known Issues

The following issues are known:

a) Due to a name conflict, this toolkit is incompatible with the h5labview toolkit. The two toolkits cannot be installed on the same version of LabVIEW simultaneously. Attempting to do so will result in broken VIs as one toolkit attempts to load identically-named but incompatible VIs from the other.

b) LabVIEW may need to be restarted after installing the toolkit before all datatypes (especially strings and
array datatypes) will work.

c) The toolkit does not work on Windows XP. Both h5helper.dll and the hdf5.dll (as built by the HDF Group) require GetTickCount64 from kernel32.dll, which only exists in Windows Vista and higher.

d) Occasionally xnodes will not properly maintain their state, leading to broken "ghost" code (broken
code that, when highlighted by the broken VI run arrow, highlights invisible code). Typically, rewiring
the xnodes will put the nodes back into an internally consistent state.

9. Debugging/Reporting bugs

To report bugs, please use the contact the author via the LVHDF5 forum at

http://www.upvi.net/main/index.php/forum/

Note that a more formal forum or bug tracking system may be in place in the future, so if such a thing is available on the UPVI website, please make use of that instead. Prior to reporting bugs, please do the following:

a) Set the environment variable "LVHDF5Debug=1" and restart LabVIEW. Reproduce the error. A log file "LVHDF5Debug.log" should be generated in the working directory of LabVIEW (the current directory when the VI is run, which may not be the VI directory). If you cannot find this file, try explicitly running LabVIEW from the command line in a directory in which you have write access. 

b) Please attach the LVHDF5Debug.log file to your bug report.

