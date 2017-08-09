# LFW tools

## Summary

A collection of tools for reorganizing directories. The project was initially created in order to organize faces from...

http://conradsanderson.id.au/lfwcrop/

...So that they match the format for the script offered in this OpenCV tutorial:

http://docs.opencv.org/2.4/modules/contrib/doc/facerec/tutorial/facerec_video_recognition.html

Hope this helps someone!

## Prequesites

~ Need to check path format for non-linux machines (will fix for generic in the future)

~ Python2.7

## Execution

Assume the following directory tree, where faces are the faces from the LFW database:

```
  .
  |-- LFW_tools.py
  |-- faces
  |   |-- Brad_Pitt_0001.pgm
  |   |-- Brad_Pitt_0002.pgm
  |   |-- ...
  |   |-- Brad_Pitt_0012.pgm
  |   |-- Johnny_Depp_0001.pgm
  |   |-- Johnny_Depp_0002.pgm
  |   |-- ...
  |   |-- Johnny_Depp_00017.pgm
  |   |-- ...
```

To execute the toolbox:

```bash
cd /path/to/master
python LFW_tools.py /faces
```

/faces is (in this example) the path to all of the faces from LFW

Allowed commands + description appear in the terminal

For example, command no.1 will change the tree to the following structure:

```
  .
  |-- LFW_tools.py
  |-- faces
  |   |-- res
  |   |   |-- s0
  |   |   |   |-- 1.pgm
  |   |   |   |-- 2.pgm
  |   |   |   |-- ...
  |   |   |   |-- 12.pgm
  |   |   |-- s1  
  |   |   |   |-- 1.pgm
  |   |   |   |-- 2.pgm
  |   |   |   |-- ...
  |   |   |   |-- 17.pgm
  |   |   | ...
  |   |-- Brad_Pitt_0001.pgm
  |   |-- Brad_Pitt_0002.pgm
  |   |-- ...
  |   |-- Brad_Pitt_0012.pgm
  |   |-- Johnny_Depp_0001.pgm
  |   |-- Johnny_Depp_0002.pgm
  |   |-- ...
  |   |-- Johnny_Depp_0017.pgm
  |   |-- ...
```

Where s0/1.pgm corresponds to Brad_Pitt_0001.pgm

### Future work

~ Add support for multiple paths

~ Create a csv file

### Conclusions

Learnt a lot about the python os and shutil libraries.
