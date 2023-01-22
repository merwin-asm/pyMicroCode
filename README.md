# pyMicroCode 7.0.0

It's a module to generate microcode(these are sort of like qrcode but have someother uses)

<p align="right"> <img src="https://komarev.com/ghpvc/?username=meriwn-py-micro-code&label=Project%20views&color=0e75b6&style=flat" alt="darkmash-org" /> </p>


## Features

- Easy to use.
- Have a lot of customisation freedom.
- Secure(AES).
- Data Compression.


## Examples

```python
import pyMicroCode

mc = pyMicroCode.MicroCode()
```

Write :
write()

args :
       
       file_name = > name of the file to save. 
       data_ = > data which will be saved.
       password = > password to read the file.
       mode="normal" = > mode (safe/normal).
       size=(200,200) = > size of the MicroCode.
       start_pos=(0,0) = > where to start the data writing.
       dim_brightness=0 = > to decrease the color brightness.
       brightness=0 = > to increase the color brightness.
       vertical_spacing=0 = > to add spacing vertically.
       spacing=0 = > horizontal spacing. 

```python
mc.write("Hello_world.png","HI","my_pass")
```

Read :

args :
       
       file_name = > file to read.
       password = > password of the MicroCode.
       mode="normal" = > mode in which the MicroCode was created.
       start_pos=(0,0) = > at which pos the msg starts.
       dimed_brightness=0 = > decreased brightness.
       brightness=0 = > increased brightness.

Read()
```python
mc.Read("Hello_world.png","my_pass")
```
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Author

- [@Merwin](https://github.com/mastercodermerwin)
