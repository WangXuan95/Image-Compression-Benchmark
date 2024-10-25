# -*- coding: utf-8 -*-
# Python3
# only for Windows !!!

import sys
import os
import shutil
import time
import datetime

from PIL import Image   # some image format is encoded/decoded using this library
import pillow_jpls      # to encode/decode JPEG-LS


# NOTE: uncomment lines to select which format to participate in benchmark
CODEC_LIST = [
 #    codec_name, support , fsuffix  , encode_command_format                                                   , decode_command_format
 #                        0b11 = this codec support both Gray8 and RGB888
 #                        0b10 = this codec support RGB888 only
 #                        0b01 = this codec support Gray8 only
    [ 'fNBLI v0.4'      , 0b11    , '.fnbli' , r'codec\NBLI\fNBLI.exe -f   {0} -o {1}'                                 , r'codec\NBLI\fNBLI.exe   -f   {0} -o {1}'                 ],
 #  [ 'NBLI v0.4 -g'    , 0b11    , '.nbli'  , r'codec\NBLI\NBLI.exe  -fg  {0} -o {1}'                                 , r'codec\NBLI\NBLI.exe    -f   {0} -o {1}'                 ],
 #  [ 'NBLI v0.4 -ga'   , 0b11    , '.nbli'  , r'codec\NBLI\NBLI.exe  -fga {0} -o {1}'                                 , r'codec\NBLI\NBLI.exe    -f   {0} -o {1}'                 ],
 #  [ 'HALIC v0.7.2'    , 0b11    , '.halic' , r'codec\HALIC\HALIC072e.exe     {0} {1}'                                , r'codec\HALIC\HALIC072d.exe     {0} {1}'                  ],
 #  [ 'HALIC v0.7.2f'   , 0b11    , '.halicf', r'codec\HALIC\HALIC072fe.exe    {0} {1}'                                , r'codec\HALIC\HALIC072fd.exe    {0} {1}'                  ],
 #  [ 'KVICK'           , 0b10    , '.kvick' , r'codec\KVICK\kvick.exe c i     {1} {0}'                                , r'codec\KVICK\kvick.exe d i     {0} {1}'                  ],
 #  [ 'QIC v1'          , 0b10    , '.qic'   , r'codec\QIC\QIC.exe           c {1} {0}'                                , r'codec\QIC\QIC.exe           d {0} {1}'                  ],
 #  [ 'QLIC2'           , 0b10    , '.qlic2' , r'codec\QLIC2\QLIC2.exe       c {1} {0}'                                , r'codec\QLIC2\QLIC2.exe       d {0} {1}'                  ],
 #  [ 'FLIC v2.1'       , 0b10    , '.flic'  , r'codec\FLIC\FLIC.exe         c {1} {0}'                                , r'codec\FLIC\FLIC.exe         d {0} {1}'                  ],
 #  [ 'GRALIC v1.11'    , 0b10    , '.gralic', r'codec\GRALIC\Gralic111d.exe c {1} {0}'                                , r'codec\GRALIC\Gralic111d.exe d {0} {1}'                  ],
 #  [ 'LEA v0.6b'       , 0b10    , '.lea'   , r'codec\LEA\clea.exe            {0} {1}'                                , r'codec\LEA\dlea.exe            {0} {1}'                  ],
 #  [ 'EMMA'            , 0b10    , '.emma'  , r'codec\EMMA\emma_c.exe         {0} {1}'                                , r'codec\EMMA\emma_d.exe         {0} {1}'                  ],
 #  [ 'BMF v2.01'       , 0b11    , '.bmf'   , r'codec\BMF\BMF.exe           -O{1} {0}'                                , r'codec\BMF\BMF.exe -pnm      -O{1} {0}'                  ],
 #  [ 'BMF v2.01 -s'    , 0b11    , '.bmf'   , r'codec\BMF\BMF.exe -s        -O{1} {0}'                                , r'codec\BMF\BMF.exe -pnm      -O{1} {0}'                  ],
 #  [ 'BIM v0.3'        , 0b10    , '.bim3'  , r'codec\BIM\bim.exe           c {0} {1}'                                , r'codec\BIM\bim.exe           d {0} {1}'                  ],
 #  [ 'QOI'             , 0b10    , '.qoi'   , r'codec\QOI\ImCvt.exe     -f {0} -o {1}'                                , r'codec\QOI\ImCvt.exe     -f {0} -o {1}'                  ],
 #  [ 'QOIR'            , 0b10    , '.qoir'  , r'codec\QOIR\QOIR.exe        {0}    {1}'                                , r'codec\QOIR\QOIR.exe        {0}    {1}'                  ],
 #  [ 'ZPNG -1'         , 0b11    , '.zpng'  , r'codec\ZPNG\ZPNG.exe -c     {0}    {1}'                                , r'codec\ZPNG\ZPNG.exe -d     {0}    {1}'                  ],
 #  [ 'ZPNG -19'        , 0b11    , '.zpng'  , r'codec\ZPNG\ZPNG.exe -19    {0}    {1}'                                , r'codec\ZPNG\ZPNG.exe -d     {0}    {1}'                  ],
 #  [ 'PNG'             , 0b11    , '.png'   , r'Image.open(r"{0}").save(r"{1}", optimize=False)'                      , r'Image.open(r"{0}").save(r"{1}")'                        ],
 #  [ 'PNG o'           , 0b11    , '.png'   , r'Image.open(r"{0}").save(r"{1}", optimize=True)'                       , r'Image.open(r"{0}").save(r"{1}")'                        ],
 #  [ 'PNG optipng -o2' , 0b11    , '.png'   , r'codec\PNG\optipng.exe -o2 -quiet -force -out {1} {0}'                 , r'Image.open(r"{0}").save(r"{1}")'                        ],
 #  [ 'JPEG-XL -e1'     , 0b11    , '.jxl'   , r'codec\JPEG-XL\cjxl.exe {0} {1} -q 100 -e 1 --num_threads=0 --quiet'   , r'codec\JPEG-XL\djxl.exe {0} {1} --num_threads=0 --quiet' ],
 #  [ 'JPEG-XL -e2'     , 0b11    , '.jxl'   , r'codec\JPEG-XL\cjxl.exe {0} {1} -q 100 -e 2 --num_threads=0 --quiet'   , r'codec\JPEG-XL\djxl.exe {0} {1} --num_threads=0 --quiet' ],
 #  [ 'JPEG-XL -e3'     , 0b11    , '.jxl'   , r'codec\JPEG-XL\cjxl.exe {0} {1} -q 100 -e 3 --num_threads=0 --quiet'   , r'codec\JPEG-XL\djxl.exe {0} {1} --num_threads=0 --quiet' ],
 #  [ 'JPEG-XL -e4'     , 0b11    , '.jxl'   , r'codec\JPEG-XL\cjxl.exe {0} {1} -q 100 -e 4 --num_threads=0 --quiet'   , r'codec\JPEG-XL\djxl.exe {0} {1} --num_threads=0 --quiet' ],
 #  [ 'JPEG-XL -e5'     , 0b11    , '.jxl'   , r'codec\JPEG-XL\cjxl.exe {0} {1} -q 100 -e 5 --num_threads=0 --quiet'   , r'codec\JPEG-XL\djxl.exe {0} {1} --num_threads=0 --quiet' ],
 #  [ 'JPEG-XL -e6'     , 0b11    , '.jxl'   , r'codec\JPEG-XL\cjxl.exe {0} {1} -q 100 -e 6 --num_threads=0 --quiet'   , r'codec\JPEG-XL\djxl.exe {0} {1} --num_threads=0 --quiet' ],
 #  [ 'JPEG-XL -e7'     , 0b11    , '.jxl'   , r'codec\JPEG-XL\cjxl.exe {0} {1} -q 100 -e 7 --num_threads=0 --quiet'   , r'codec\JPEG-XL\djxl.exe {0} {1} --num_threads=0 --quiet' ],
 #  [ 'JPEG-XL -e8'     , 0b11    , '.jxl'   , r'codec\JPEG-XL\cjxl.exe {0} {1} -q 100 -e 8 --num_threads=0 --quiet'   , r'codec\JPEG-XL\djxl.exe {0} {1} --num_threads=0 --quiet' ],
 #  [ 'WEBP -1'         , 0b10    , '.webp'  , r'Image.open(r"{0}").save(r"{1}",lossless=True,quality=100,method=1)'   , r'Image.open(r"{0}").save(r"{1}")'                        ],
 #  [ 'WEBP -5'         , 0b10    , '.webp'  , r'Image.open(r"{0}").save(r"{1}",lossless=True,quality=100,method=5)'   , r'Image.open(r"{0}").save(r"{1}")'                        ],
 #  [ 'JPEG2000'        , 0b11    , '.j2k'   , r'Image.open(r"{0}").save(r"{1}",format="JPEG2000",irreversible=False)' , r'Image.open(r"{0}").save(r"{1}")'                        ],
 #  [ 'JPEG-LS'         , 0b11    , '.jls'   , r'Image.open(r"{0}").save(r"{1}", spiff=None)'                          , r'Image.open(r"{0}").save(r"{1}")'                        ],
 #  [ 'JPEG-LS'         , 0b11    , '.jls'   , r'codec\JPEG-LS\JPEGLSenc.exe {0} -o{1}'                                , r'codec\JPEG-LS\JPEGLSdec.exe -P {0} -o{1}'               ],
 #  [ 'JLS-ext'         , 0b01    , '.jlsxn' , r'codec\JPEG-LS_extension\JLSx.exe {0} {1}'                             , r'codec\JPEG-LS_extension\JLSx.exe {0} {1}'               ],
 #  [ 'CALIC'           , 0b01    , '.calic' , r'python codec\CALIC\calic.py -e {0} {1} 0'                             , r'python codec\CALIC\calic.py -d {0} {1}'                 ],
 #  [ 'agiannis_image'  , 0b10    , '.aim'   , r'codec/agiannis_image/agiannis_image c {0} {1}'                        , r'codec/agiannis_image/agiannis_image d {0} {1}'          ],  # need to run on Linux
 #  [ 'PGLZ'            , 0b10    , '.pglz'  , r'codec/PGLZ/pglz -c        {0} {1}'                                    , r'codec/PGLZ/pglz -d        {0} {1}'                      ],  # need to run on Linux
]


CHECK_DISTORTION = True     # check if the decoded file same as the original file



# return: (type, data_array)
#          type=0 : not a valid pnm file
#          type=1 : gray8  pnm/pgm file
#          type=2 : rgb888 pnm/ppm file
def parsePNMFile (fname) :
    def readUntilSpace (fp) :
        string = b''
        c = fp.read(1)
        while c!=b'' and (not c in b' \r\n\t\v') :
            string += c
            c = fp.read(1)
        return string
    
    try :
        with open(fname, 'rb') as fp :
            mark   = readUntilSpace(fp)
            assert mark in [b'P5', b'P6']
            n_channel = 3 if (mark==b'P6') else 1
            width  = int(readUntilSpace(fp))
            height = int(readUntilSpace(fp))
            depth  = int(readUntilSpace(fp))
            data   = fp.read()
            assert depth < 256
            assert width > 0
            assert height> 0
            assert len(data) == (n_channel * width * height)
        return (0b10 if (mark==b'P6') else 0b01), (width*height), data
    except :
        return  0b00, 0, b''



def ccolor (color_code, string) :
    "Construct color string"
    if 31<=color_code and color_code<=37 :
        return ('\033[1;%dm' % color_code) + string + '\033[0m'
    else :
        return string



if __name__ == '__main__' :
    os.system('')   # after running a empty command, it will support printing color characters
    
    #-------------------------------------------------------------------------------
    # parse command line
    try :
        src_path = sys.argv[1]
        assert os.path.isdir(src_path)
    except :
        print(ccolor((31, 'Usage: python %s <src_path>' % sys.argv[0])))
        exit(1)
    
    try :
        log_path = sys.argv[2]
    except :
        log_path = None
    
    #-------------------------------------------------------------------------------
    # prepare output directory. If already exists, delete it
    dst_path = 'RunBenchmark_output'
    if os.path.exists(dst_path) :
        if input('output directory %s already exists, overwrite it? (y|n) ' % dst_path) in ['y','Y'] :
            if os.path.isdir(dst_path) :
                shutil.rmtree(dst_path) # remove directory
            else :
                os.remove(dst_path)     # remove file
        else :
            exit(1)
    
    
    #-------------------------------------------------------------------------------
    # determine what color type is supported in this test (Gray8, RGB888, or both)
    support_code = 0b11
    for (codec_name, support, fsuffix, enc_cmd_fmt, dec_cmd_fmt) in CODEC_LIST :
        support_code &= support
    
    if len(CODEC_LIST)==0 or support_code==0 :
        print(ccolor((31, '***Error: select codecs must support at least one color type')))
        exit(1)
    
    
    #-------------------------------------------------------------------------------
    # makeup image file names
    src_fname_list = []
    n_pixels = 0           # pixel count of all input images
    n_bytes  = 0           # byte count of all input images
    for fname in os.listdir(src_path) :
        if os.path.splitext(fname)[1] in ['.pgm', '.ppm', '.pnm'] :
            src_fname = os.path.join(src_path, fname)
            color_code, n_pixel, data = parsePNMFile(src_fname)
            if (color_code & support_code) != 0 :
                src_fname_list.append(src_fname)
                n_pixels += n_pixel
                n_bytes  += len(data)
    
    if len(src_fname_list) <= 0 :
        print(ccolor(31, '***Error: no PNM/PGM/PPM image to be tested in %s' % src_path))
        exit(1)
    
    base_string = 'total %d files with %d bytes of pixels' % (len(src_fname_list), n_bytes)
    
    
    
    #-------------------------------------------------------------------------------
    # makeup encode/decode commands
    command_list = []
    for (codec_name, support, fsuffix, enc_cmd_fmt, dec_cmd_fmt) in CODEC_LIST :
        dec_fname_list, enc_cmd_list, dec_cmd_list = [], [], []
        for src_fname in src_fname_list :
            _, fname  = os.path.split(src_fname)
            enc_fname = os.path.join(dst_path, os.path.splitext(fname)[0]+fsuffix)
            dec_fname = os.path.join(dst_path, fname)
            dec_fname_list.append(dec_fname)
            enc_cmd = enc_cmd_fmt.format(src_fname, enc_fname)
            dec_cmd = dec_cmd_fmt.format(enc_fname, dec_fname)
            #if enc_cmd.startswith('wsl') : enc_cmd = enc_cmd.replace('\\', '/')  # for Linux command (run in windows subsystem of linux (WSL))
            #if dec_cmd.startswith('wsl') : dec_cmd = dec_cmd.replace('\\', '/')  # for Linux command (run in windows subsystem of linux (WSL))
            enc_cmd_list.append(enc_cmd)
            dec_cmd_list.append(dec_cmd)
        command_list.append((codec_name, dec_fname_list, enc_cmd_list, dec_cmd_list))
    
    
    #-------------------------------------------------------------------------------
    # run encode/decode commands
    report_string = ''
    for (codec_name, dec_fname_list, enc_cmd_list, dec_cmd_list) in command_list :
        # mkdir dst_path --------------------
        os.mkdir(dst_path)
        
        # if enc_cmd_list[0].startswith('wsl') : os.system('wsl cd .')  # if this codec uses WSL, touch WSL, protect the codec from being affected by the additional startup overhead of WSL --------------------
        
        error_msg = None    # whether the codec exit normally
        
        # encode ----------------------------------
        if (error_msg is None) : 
            enc_time = time.time()
            if enc_cmd_list[0].startswith('Image.open') :
                for command in enc_cmd_list :
                    print(ccolor(33, 'python>%s' % command))
                    try :
                        exec(command)
                    except :
                        error_msg = '***Error: command "%s" exit with error' % command
                        print(ccolor(31, error_msg))
                        break
            else :
                for command in enc_cmd_list :
                    print(ccolor(33, '>%s' % command))
                    if os.system(command) != 0 :
                        error_msg = '***Error: command "%s" exit with error' % command
                        print(ccolor(31, error_msg))
                        break
            enc_time = time.time() - enc_time
        
        # get encoded file size -------------------
        if (error_msg is None) : 
            enc_size = 0
            for fname in os.listdir(dst_path) :
                enc_size += os.path.getsize(os.path.join(dst_path, fname))
        
        # decode ----------------------------------
        if (error_msg is None) : 
            dec_time = time.time()
            if dec_cmd_list[0].startswith('Image.open') :
                for command in dec_cmd_list :
                    print(ccolor(33, 'python>%s' % command))
                    try :
                        exec(command)
                    except :
                        error_msg = '***Error: command "%s" exit with error' % command
                        print(ccolor(31, error_msg))
                        break
            else :
                for command in dec_cmd_list :
                    print(ccolor(33, '>%s' % command))
                    if os.system(command) != 0 :
                        error_msg = '***Error: command "%s" exit with error' % command
                        print(ccolor(31, error_msg))
                        break
            dec_time = time.time() - dec_time
        
        # calculate distortion --------------------
        if (error_msg is None) and CHECK_DISTORTION :
            list1 = []
            list2 = []
            for (src_fname, dec_fname) in zip(src_fname_list, dec_fname_list) :
                c1, _, data1 = parsePNMFile(src_fname)
                c2, _, data2 = parsePNMFile(dec_fname)
                if c1!=c2 or len(data1)!=len(data2) :
                    print(ccolor(31, '***Error in %s: %s and %s have different colortype or size' % (codec_name, src_fname, dec_fname)))
                    exit(1)
                if data1 != data2 :
                    import numpy as np
                    data1 = np.frombuffer(data1, dtype='<u1')
                    data2 = np.frombuffer(data2, dtype='<u1')
                    abs_diff = np.abs(np.int16(data1) - np.int16(data2))
                    list1.append(np.max(abs_diff))
                    list2.append(np.mean(np.float32(abs_diff)))
                else :
                    list1.append(0)
                    list2.append(0.0)
            max_abs_diff  = max(list1)
            mean_abs_diff = sum(list2) / len(list2)
        else :
            max_abs_diff  = 0
            mean_abs_diff = 0.0
        
        # remove dst_path --------------------
        shutil.rmtree(dst_path)
        
        # makeup report log --------------------
        title_string = '\n# %s, log at %s ---------\n' % (base_string, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if (error_msg is None) :
            report_string += ccolor(32, '%-24s:  enc_size=%-11d  BPP=%-6.3f  enc_time=%.3f (%.0fkB/s)  dec_time=%.3f (%.0fkB/s)' % (codec_name, enc_size, 8.0*enc_size/n_pixels, enc_time, (n_bytes/1000)/(enc_time+0.00001), dec_time, (n_bytes/1000)/(dec_time+0.00001)))
        else :
            report_string += ccolor(31, '%-24s:  %s' % (codec_name, error_msg))
        if max_abs_diff > 0 :
            report_string += ccolor(31, '   max_diff=%d  mean_diff=%.3f' % (max_abs_diff, mean_abs_diff))
        report_string += '\n'
        
        # print log --------------------
        print(title_string, end='')
        print(report_string)
        
        # write log --------------------
        try :
            if not log_path is None:
                with open(log_path, 'wt') as fp :
                    fp.write(title_string)
                    fp.write(report_string)
        except :
            pass


