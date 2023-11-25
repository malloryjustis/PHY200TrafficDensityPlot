"""

This code contains a function that returns a user specified choice of speed-density relationship to be used for calculating traffic density.

Author: Mallory Justs
Date: May 2022

"""

#choose speed-density relationship function
def choose_speed_density():
  """
  Defines which speed-density relationship will be used based on user input.
  
  Parameters:
  -----------
  
  Returns:
  --------
  name_of_relationship: STRING
    speed density relationship
  """

  name_of_relationship = input("Enter speed-density relationship (greenshield, underwood, pipes-munjal): ")

  return name_of_relationship