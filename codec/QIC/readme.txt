QIC is a quick lossless image compressor, v. 1.dem
(c) Alexander Rhatushnyak
Please feel free to send an email to qlic@live.com for more info.

To compress|decompress a PPM file: QIC.exe c|d archive file
Examples:
QIC.exe c example.qic1 example.ppm
QIC.exe d example.qic1 example_decompressed.ppm

The 1.dem executable is for 24-bit images with both width and height <=32768.
It does not check whether the output is smaller or bigger than input.

This 32-bit Windows executable was compiled with MinGW 4.5.2 and MinGW 4.7.2:
cd \mingw452\bin
g++ -O3 -mtune=atom   -mmmx -fomit-frame-pointer -fno-exceptions QIC_enc.cpp -S
cd \mingw472\bin
g++ -O3 -mtune=corei7 -mmmx -fomit-frame-pointer -fno-exceptions -ffast-math -s -static QIC_main.cpp \MinGW452\bin\QIC_enc.s QIC_dec.cpp -o QIC.exe

No profiling data usage, no assembly instructions.
