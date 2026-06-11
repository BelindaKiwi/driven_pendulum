import numpy as np
from scipy.integrate import solve_ivp

def driven_pendulum(omega, A, b, g, L, theta_start, t):
    '''
    returns first and second derviates of theta using eqn of motion provided
    '''
    d_theta = omega # time dertivate of theta is omega
    
    # rearragnement of motion equation given to calculate second derivate of theta
    dd_theta = -b*d_theta - (g/L)*np.sin(theta_start) + (A*omega**2/L)*np.sin(omega*t)*np.cos(theta_start)

    return d_theta, dd_theta



def main():

    # switches
    function_test = True # just to check my function returns some dd_theta values
    use_sol_ivp = True
   
    # constants provided
    L = 1.0
    g = 9.81
    m = 1.0
    b = 0.5
    
    #---------------------------------------------------
    if function_test: 

        # start values
        A = 0.2 # amplitude of drive
        omega = 2 # rate of drive
        theta_start = 0.2 # start angle of pendulum
        t_0 = 0
        t_end = 20
        t = np.linspace(t_0, t_end, 20) # time values to evaluate over

        d_theta, dd_theta = driven_pendulum(omega, A, b, g, L, theta_start, t)

        print('dd_theta values:')
        print(dd_theta)
    #---------------------------------------------------

    if use_sol_ivp:
        print()






   



if __name__ == "__main__":
    main()

