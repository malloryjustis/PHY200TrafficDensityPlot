"""

This code generates plots for user to compare speed, density, and flow.

Author: Mallory Justs
Date: May 2022

"""

#imports
import numpy as np
import matplotlib.pyplot as plt

def plotting(speed, rho_list):
  """
  creates plots of speed, density and flow
    
  Parameters:
  -----------
    speed: LIST OF FLOAT
      speed values
    rho_list: LIST OF FLOAT
      list of density values
  Returns:
  --------
  """

  #plotting speed vs. density
  y = np.array(speed)
  x = np.array(rho_list)
  plt.plot(x,y, '.')
  plt.xlabel('Density (cars/mile)')
  plt.ylabel('Speed (miles/hr)')
  plt.show()

  #solving flow = rho*v to find flow values
  flow_list = []
  for i in range(len(speed)):
    flow_list.append(speed[i]*rho_list[i])
    
  #plotting speed vs flow
  f = np.array(flow_list)
  plt.plot(f, y, '.')
  plt.xlabel('Flow (cars/hr)')
  plt.ylabel('Speed (miles/hr)')
  plt.show()

  #plotting flow vs density
  plt.plot(x, f, '.')
  plt.xlabel('Density (cars/mile)')
  plt.ylabel('Flow (card/hr)')
  plt.show()
