This repository contains some helpful cocotb functions.
----
# 1 Package installation
Clone github repository:
```
git clone https://github.com/spoursalidis/cocotb_functions.git
```

Change to directory:
```
cd cocotb_functions/
```

Run setup.py:
```
python setup.py sdist
```

Move source files to python package library:
```
mv cocotb_functions/ /usr/local/lib/python3.10/dist-packages/
```

# 2 Usage in python script
```
import cocotb_functions
from cocotb_functions.testbench import set_rstn, wait_n_cycles, check_value
```
