# -*- coding: utf-8 -*-
""" An example *.py file.

Some examples of coding in a *.py file as opposed to a Jupyter notebook file.

These examples are meant to be viewed in the Spyder IDE.
The concept of cells as used below is specific to Spyder.
"""

#%% This is a cell similar to a Jupyter notebook cell.
# You can run this cell in the Spyder IDE in the same way (Shift-Enter) when it is selected.
# The end of the cell is determined by the start of the next cell.
favcolor = "green"
favshape = "triangle"

""" After running this cell check out the variable explorer tab.
"""

#%%
print('hi')  # The output should show up in the console tab.

#%% A simple function.
def sayhi(name):
    """ Say hi to someone. """
    print(f"Hi, {name}")

#%% Let's use the function above.
sayhi("Sam")

#%% Create an array and check it out in the Variables tab.
import numpy as np  # typically all imports at top

x = np.random.random((5,5))

""" Double-click it in the Variables tab to get a nice view of it.
"""

#%% Plot the middle row of x.
import matplotlib.pyplot as plt

plt.plot(np.arange(5), x[2], '-o')
plt.xlabel("Column #")
plt.ylabel("x")
