# Author(s):
#   - Spyridon Poursalidis <s.poursalidis@gmail.com>
#
# Description:
#
# Basic test bench functions
#
import cocotb
from cocotb.triggers import Timer, RisingEdge
from random import randint

@cocotb.coroutine
def wait_n_cycles(clk, n_cycles):
    # Wait a specific number of rising clock events
    for _ in range(n_cycles):
        yield RisingEdge(clk)

@cocotb.coroutine
def set_rst(clk, rst):
    # Trigger the reset signal of the DuT for 5 clock cycles. 
    # Provided reset signal must be active high.
    yield RisingEdge(clk)
    rst.value = 1
    yield wait_n_cycles(clk, 5)
    rst.value <= 0
    yield RisingEdge(clk)

@cocotb.coroutine
def set_rstn(clk, rstn):
    # Trigger the reset signal of the DuT for 5 clock cycles. 
    # Provided reset signal must be active low.
    yield RisingEdge(clk)
    rstn.value = 0
    yield wait_n_cycles(clk, 5)
    rstn.value = 1
    yield RisingEdge(clk)

@cocotb.coroutine
def toggle_signal(clk, sig):
    # Randomly toggle the value of a one bit signal
    while True:
        yield wait_n_cycles(clk, randint(1, 25))
        if int(sig) == 0:
            sig.value = 1
        else:
            sig.value = 0

def check_value(name, val1, val2):
    # Check whether two values are equal. Throw error if not
    if val1 == val2:
        return

    msg = "Incorrect value '%s': 0x%x != 0x%x" % (name, val1, val2)
    raise cocotb.result.TestFailure(msg)

def swp_byte_order(data, bytelen):
    # Return the input data in reversed byte order
    h = '%x' % data
    s = ('0'*(len(h) % 2) + h).zfill(bytelen*2).decode('hex')
    return int(s[::-1].encode('hex'), 16)
