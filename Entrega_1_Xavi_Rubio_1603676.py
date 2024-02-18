# Modific. "Example parabolic motion" Xavi Rubio
#https://github.com/xrubio4
#LLista de modificacions:
#Canvi en el metode de calcul afegint condicions per a poder acceptar valors d'angles entre 0 i 180 graus (M1)
#Afegir missatge d'alerta en cas d'introduir un angle >180 graus (M2)
#Afegir capacitat de poder triar el modul de la velocitat inicial. (M4)
#Afegir missatge d'alerta en cas d'introduir una resposta que no sigui un valor de velocitat positiu. (M5)

import numpy as np
import matplotlib.pyplot as plt
 
#
# FUNCTION DRAW A TRAJECTORY FOR PARABOLIC MOTION
# Input: velocity and angle 
#
def draw_trajectory(u, angle):

    theta = np.radians(angle)

    g = 9.8

    # (M1 inici)
    t_flight = np.abs(2*u*np.sin(theta)/g)
    # find time intervals
    intervals = np.arange(0, t_flight, 0.001)
    # create an empty list of x and y coordinates
    x = []
    y = []
    #Plot the results
    if (0 <= theta <= np.pi/2):
        #Do a loop over time calculating the coordinates
        for t in intervals:
            x.append(u*np.cos(theta)*t)
            y.append(u*np.sin(theta)*t - 0.5*g*t*t)
        plt.plot(x, y)
        plt.xlabel('Distance (m)')
        plt.ylabel('Height (m)')
        plt.title('Projectile motion')
    elif (np.pi/2 < theta <= np.pi):
        #Do a loop over time calculating the coordinates
        for t in intervals:
            x.append(-np.abs(u*np.cos(theta)*t))
            y.append(u*np.sin(theta)*t - 0.5*g*t*t)
        plt.plot(x, y)
        plt.xlabel('Distance (m)')
        plt.ylabel('Height (m)')
        plt.title('Projectile motion')
    # (M1 final)

#--------------------------------------------------------------------------------
# Main Program: give specific values and call to the function draw_trajectory
#--------------------------------------------------------------------------------

print("Calculadora de trajectories")


print("Introdueix el valor de l'angle inicial en graus (0-180)")
angle=float(input())
# (M2 inici)
if (0 <= angle <= 180):
    u_list = []
    print("Introdueix el nombre de velocitats inicials per a les que vols calcular la trajectoria:")
    num=float(input())

    # (M5 inici)
    if num > 0:
        # (M4 inici)
        i=0
        while i < num:
            print("Introdueix el valor de velocitat inicial num. " + str(i+1) + " en m/s")
            vel=float(input())
            if vel > 0:
                u_list.append(vel)
                i = i+1
            else:
                i = num
                print("Siusplau introdueix un valor de velocitat inicial positiu")
                                
        # (M4 final)
        for u in u_list:
                draw_trajectory(u, angle)
                
        # Add a legend and show the graph
        plt.legend([str(u) +" m/s" for u in u_list])
        plt.show()
    else:
        print("Siusplau introdueix un nombre velocitats positiu.")
    # (M5 final)
    # (M6 inici)

else:
    print("Cal introduir un valor d'angle inicial adequat, revisa la teva resposta.")
# (M2 final) 


