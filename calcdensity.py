"""

This code contiains the function to calculate traffic denity based on input parameters. It also returns lists of density and speed values for later plotting.

Author: Mallory Justis
Date: May 2022

"""

#imports
import numpy as np

#calculate density function
def calc_traffic_density(rho, boundary, N, v_max, rho_max, name_of_relationship):
  """
  calculates the traffic density

  Parameters:
  -----------
  rho: ARRAY of FLOAT
    initial condition
  boundary: ARRAY OF FLOAT
    boundary condition [L, T]
  N: INT
    number of discretizations
  v_max: FLOAT
    speed limit
  rho_max: FLOAT
    maximum density possible on section of highway
  name_of_relationship: STRING
    which speed-density relationship is being used
  
  Returns:
  --------
  rho: ARRAY OF FLOAT
    density values
  speed: LIST OF FLOAT
    list of speed values to be used for plotting
  rho_list: LIST OF FLOAT
    list of density values to be used for plotting
  """

  #discretizations
  dx = boundary[0]/N
  dt = boundary[1]/N
    
  #create speed density list
  speed = []
  rho_list = []

  if name_of_relationship == "pipes-munjal":
    n = int(input("Enter value of n for pipes-munjal model: "))

  #changing each density value in the time/space array
  for t in range(1,N-1):
    for x in range(0,N):
      #speed density relationship for variable decided by helper function
      if name_of_relationship == "greenshield":
        speed_density = v_max*(1 - rho[x,t]/rho_max)
      elif name_of_relationship == "underwood":
        speed_density = v_max*np.exp(-rho[x,t]/rho_max)
      elif name_of_relationship == "pipes-munjal":
        speed_density = v_max*(1 - (rho[x,t]/rho_max)**n)
      else:
        print("Relationship not found. Please try again.")
        break
      
      #changing values of density plot
      rho[x,t+1] = rho[x,t] + speed_density*dt/dx*(abs(rho[x,t] - rho[x-1,t]))
    
      #adding speed and density values to lists for plotting
      rho_list.append(rho[x,t+1])
      speed.append(speed_density)
    
  return rho, speed, rho_list