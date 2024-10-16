# Get RGB 24-bit dataset

The RGB 24-bit image benchmark data set has 585 images totaling 4GB from [CLIC2021 competition](https://clic.compression.cc/2021/tasks/index.html).

To get the benchmark images, you should download them as follow steps:

- Download  https://data.vision.ee.ethz.ch/cvl/clic/professional_train_2020.zip

- Extract the zip, getting 585 .png image files.

- Then, convert all the downloaded images to <b>24-bit RGB .ppm format</b> using <a href="https://www.xnview.com/en/nconvert/#downloads">NConvert 7.163</a>.
  The method is to run the following command in the directory where the image is located:
  
  ```
  nconvert.exe  -out ppm *.png
  ```
  
- Then, rename these .ppm files to 001.pnm, 002.pnm, 003.pnm, ..., 585.pnm.
  You can do this by running the following Python script:
  
  ```python
  import os
  import shutil
  for (i, fname) in enumerate(list(os.listdir('.'))) :
      if fname.endswith('.ppm') :
          dst_fname = '%03d.pnm' % i+1
          shutil.move(fname, dst_fname)
  ```
  
  <i>Note: .pnm is a simple uncompressed image format. Many compressors support .pnm format as input.</i> 
  
- Then, put these 585 .pnm files to a folder, then run the benchmark. See [README_Run.md](./README_Run.md)
  
