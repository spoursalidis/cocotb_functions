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

Install:
```
python3 -m pip install -e .
```

# 2 Usage in python script
```
import cocotb_functions
from cocotb_functions.testbench import set_rstn, wait_n_cycles, check_value
```
