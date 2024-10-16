## How to run benchmark

#### Prepare Python in your Windows

The benchmarking script is written in Python3. If you had not install Python3 yet, it is recommended to install Anaconda (It seems that you should fill your email to download now). Just select the newest version for Windows (the version was Python 3.12 when I wrote this document).

In this benchmark, some of the formats are compressed using Windows .EXE files (in [./codec/](./codec/) folder), while others are compressed use Python 3.9 with [Pillow 10.1.0 library](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

Therefore, after installing Anaconda, you need to use CMD (command line) to run following commands to install the required packages:

```powershell
python -m pip install Pillow==10.1.0       # for PNG, WEBP, and JPEG2000 compress/decompress
python -m pip install pillow_jpls==1.3.2   # for JPEG-LS compress/decompress
```

　

#### Run a Simple Test

The benchmarking script is [RunBenchmark.py](./RunBenchmark.py). Use following command to run:

```powershell
python RunBenchmark.py <image_folder>
```

There must be some **.pnm** image files in <image_folder>, either RGB 24bit-images or Gray 8-bit images. The script will benchmark these images.

For example, I provide one image in [example_image](./example_image) folder, so you can run a simple test:

```
python RunBenchmark.py example_image
```

To specify which compression formats to participate in comparison, simply modify the `CODEC_LIST` list in [RunBenchmark.py](./RunBenchmark.py) (just comment/uncomment corresponding lines).

　

#### Run Larger Benchmarks

Just prepare more **.pnm** images in a folder, and run the [RunBenchmark.py](./RunBenchmark.py).

* To get the large RGB 24-bit image benchmark, see [**README_RGB24dataset.md**](README_RGB24dataset.md)
* To get the large Gray 8-bit image benchmark, see [**README_Gray8dataset.md**](README_Gray8dataset.md)

