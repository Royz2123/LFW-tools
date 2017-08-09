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

'''
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
'''

To execute the toolbox:

'''bash
cd /path/to/master

python LFW_tools.py /faces
'''

Allowed commands + description appear in the terminal

### Future work

~ Add support for multiple paths

~ Create a csv file

### Conclusions

Learnt a lot about the python os and shutil libraries.
