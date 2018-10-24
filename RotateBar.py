# Author: Anastasios Tzanidakis




def rotate_me(x,y,z, radius_orbit=-8):
    from galpy.util import bovy_coords
    import numpy as np
    import matplotlib.pyplot as plt
    """Given cartesian points <X,Y,Z> of reference we will rotate you around the
    the galactic center with line of sight of always centered on the Galactic Bar"""


    phi = np.arange(0, 2*np.pi, 0.001) # steps might need more tuning

    # Apply polar transformations
    x_transform = radius_orbit * np.cos(phi)
    y_transform = radius_orbit * np.sin(phi)


    for i in range (0, len(phi)-1):
        
        # Convert physical coordinates to observational coordinates (l, b, distance)
        g_coords = bovy_coords.XYZ_to_lbd((x + radius_orbit), y, z, degree=True)




    # Firs test is to see if we can see the X shape bar with respect
