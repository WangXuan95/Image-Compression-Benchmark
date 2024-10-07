## List of the compression formats/codecs/tools participated in this benchmark

Some of the formats are compressed use Windows .EXE files (in [./codec/](./codec/) folder), while others are compressed use Python 3.9 with [Pillow 10.1.0 library](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

|                             Name                             |                         Spec / Paper                         |                 codec used in this benchmark                 |    open source?    |        gray 8-bit ?        |    RGB 24-bit ?    |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------: | :------------------------: | :----------------: |
| [**PNG**](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png) |   [RFC 2083](https://www.rfc-editor.org/rfc/rfc2083.html)    | [python pillow library](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png) | :heavy_check_mark: |     :heavy_check_mark:     | :heavy_check_mark: |
| [**PNG**](https://optipng.sourceforge.net/) ([optipng](https://optipng.sourceforge.net/) 0.7.7) |   [RFC 2083](https://www.rfc-editor.org/rfc/rfc2083.html)    |                         ./codec/PNG/                         | :heavy_check_mark: |     :heavy_check_mark:     | :heavy_check_mark: |
|        [**WEBP**](https://en.wikipedia.org/wiki/WebP)        | [Google website](https://developers.google.com/speed/webp/docs/riff_container) | [python pillow library](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp) | :heavy_check_mark: |     :heavy_check_mark:     | :heavy_check_mark: |
| [**JPEG2000**](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg-2000) |                       ISO/IEC 15444-1                        | [python pillow library](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg-2000) | :heavy_check_mark: |     :heavy_check_mark:     | :heavy_check_mark: |
| [**JPEG-LS**](http://www.stat.columbia.edu/~jakulin/jpeg-ls/mirror.htm) |                          ITU-T T.87                          | [python pillow library](https://pypi.org/project/pillow-jpls/) | :heavy_check_mark: |     :heavy_check_mark:     | :heavy_check_mark: |
| [**JPEG-LS_extension**](https://github.com/WangXuan95/JPEG-LS_extension) |                         ITU-T T.870                          |                  ./codec/JPEG-LS_extension/                  | :heavy_check_mark: |     :heavy_check_mark:     |        :x:         |
| [**JPEG-XL**](https://github.com/libjxl/libjxl/releases) *(\*1)* v0.9.0 |                        ISO/IEC 18181                         |                       ./codec/JPEG-XL/                       | :heavy_check_mark: |     :heavy_check_mark:     | :heavy_check_mark: |
|              [**QOI**](https://qoiformat.org/)               |   [QOI spec](https://qoiformat.org/qoi-specification.pdf)    |                         ./codec/QOI/                         | :heavy_check_mark: |     :heavy_check_mark:     | :heavy_check_mark: |
|     [**fNBLI**](https://github.com/WangXuan95/NBLI) v0.4     |                              -                               |                        ./codec/NBLI/                         |        :x:         |     :heavy_check_mark:     | :heavy_check_mark: |
|     [**NBLI**](https://github.com/WangXuan95/NBLI) v0.4      |                              -                               |                        ./codec/NBLI/                         | :heavy_check_mark: |     :heavy_check_mark:     | :heavy_check_mark: |
|  [**BMF**](http://compression.ru/compression.ru/ds/) v2.01   |                              -                               |                         ./codec/BMF/                         |        :x:         |     :heavy_check_mark:     | :heavy_check_mark: |
| [**GRALIC**](http://www.imagecompression.info/gralic/Gralic111d.zip) v1.11 |                              -                               |                       ./codec/GRALIC/                        |        :x:         |            bug?            | :heavy_check_mark: |
| [**FLIC**](http://www.imagecompression.info/gralic/flic21d.zip) v2.1 |                              -                               |                        ./codec/FLIC/                         |        :x:         |            :x:             | :heavy_check_mark: |
|    [**QLIC2**](http://qlic.altervista.org/qlic2d.zip) v2     |                              -                               |                        ./codec/QLIC2/                        |        :x:         |            :x:             | :heavy_check_mark: |
| [**QIC**](http://www.imagecompression.info/gralic/qic1d.zip) v1 |                              -                               |                         ./codec/QIC/                         |        :x:         |            :x:             | :heavy_check_mark: |
| [**LEA**](https://encode.su/threads/3818-LEA-Lossless-image-compressor) v0.6 beta |                              -                               |                         ./codec/LEA/                         |        :x:         |            :x:             | :heavy_check_mark: |
| [**HALIC**](https://github.com/Hakan-Abbas/HALIC-High-Availability-Lossless-Image-Compression-/releases/tag/0.7.2) 0.7.2 |                              -                               |                        ./codec/HALIC/                        |        :x:         |     :heavy_check_mark:     | :heavy_check_mark: |
|              [**BIM**](https://compressme.net/)              |                              -                               |                         ./codec/BIM/                         |        :x:         |            :x:             | :heavy_check_mark: |
|        [**CALIC**](https://www.ece.mcmaster.ca/~xwu/)        |   see [paper](https://ieeexplore.ieee.org/document/585919)   |                        ./codec/CALIC/                        |        :x:         |     :heavy_check_mark:     |        :x:         |
| [**MRP**](https://www.rs.tus.ac.jp/matsuda-lab/matsuda/mrp/index.html) v0.5 |  see [paper](https://ieeexplore.ieee.org/document/7078076/)  |                         ./codec/MRP/                         | :heavy_check_mark: | :heavy_check_mark: *(\*2)* |        :x:         |

*\*1: The well-known **FLIF** (Free Lossless Image Format) was superseded by **JPEG-XL**.*

*\*2: MRP can only compress gray 8-bit images with size multiple of 8.*

　

To install python Pillow library, run:

```
python -m pip install Pillow        # for PNG, WEBP, JPEG2000
python -m pip install pillow_jpls   # for JPEG-LS
```

