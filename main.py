import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def driven_pendulum(t, y, A, b, g, L):
    '''
    returns first and second derviates of theta using eqn of motion provided
    
    '''
    omega, theta_start = y
    d_theta = omega # time dertivate of theta is omega
    
    # rearragnement of motion equation given to calculate second derivate of theta
    dd_theta = -b*d_theta - (g/L)*np.sin(theta_start) + (A*omega**2/L)*np.sin(omega*t)*np.cos(theta_start)

    return d_theta, dd_theta



def main():

    # switches
    function_test = True # just to check my function returns some dd_theta values
 
    # constants provided
    L = 1.0
    g = 9.81
    m = 1.0
    b = 0.5

    # start values
    A = 0.0 # amplitude of drive
    omega = 0.2 # rate of drive
    theta_start = 0.2 # start angle of pendulum
    y = [omega, theta_start]
    t_0 = 0
    t_end = 200
    n =100
    t = np.linspace(t_0, t_end, n) # time values to evaluate over
    
    #---------------------------------------------------
    if function_test: 

        d_theta, dd_theta = driven_pendulum(t, y, A, b, g, L)

        # check that I get some values back
        print('dd_theta values:')
        print(dd_theta[0:10])
    #---------------------------------------------------


    # integrate to solve for theta with respect to time using scipy.integrate
    sol_obj = solve_ivp(fun=driven_pendulum,
                        t_span=(t_0, t_end),
                        y0=[omega, theta_start],
                        t_eval=t,
                        args=(A, b, g, L)
                        )
    
    print(sol_obj.t)
    print(sol_obj.y[0])
    print(sol_obj.y[1])







   



if __name__ == "__main__":
    main()

