import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def driven_pendulum(t, y, omega_drive, A, b, g, L):
    '''
    Returns first and second derviates of theta using eqn of motion provided
    y is start values
    
    '''
    theta, d_theta = y
    
    # rearragnement of motion equation given to calculate second derivate of theta
    dd_theta = -b*d_theta - (g/L)*np.sin(theta) + (A*omega_drive**2/L)*np.sin(omega_drive*t)*np.cos(theta)

    return d_theta, dd_theta

def rad2deg(x):
    '''
    Converts radians to degrees
    '''
    return x*180/np.pi

def main():

    # constants provided
    L = 1.0
    g = 9.81
    m = 1.0 
    b = 0.5

    # start values
    theta0 = 0 # start angle of pendulum radians
    d_theta0 = 0 # this is angular velocity of pendulum
    y = [theta0, d_theta0]

    # time space
    t_0 = 0
    t_end = 30
    n = 10000
    t = np.linspace(t_0, t_end, n) # time values to evaluate over
    
    # variables to play with
    A = 0.05 # amplitude of drive
    omega_drive = 2 # drive freq

    # set a range of values for A and omega_drive to explore behaviour and plot
    A_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    omega_values = [2, 4, 6, 8, 10]


    for A, omega_drive in zip(A_values, omega_values):
        # integrate to solve for theta with respect to time using scipy.integrate
        sol_obj = solve_ivp(fun=driven_pendulum,
                            t_span=(t_0, t_end),
                            y0=y,
                            t_eval=t,
                            args=(omega_drive, A, b, g, L)
                            )
        theta = sol_obj.y[0]
        d_theta = sol_obj.y[1]

        # this keeps theta within +/- pi for nicer plotting
        theta_wrapped = (theta + np.pi) % (2 * np.pi) - np.pi

        # plot theta (pendulum angle vs time) and phase space
        fig, axs = plt.subplots(2, layout='constrained')
        axs[0].plot(t, rad2deg(theta_wrapped))
        axs[0].set_xlabel('Time [s]')
        axs[0].set_ylabel('Theta [deg]')
        axs[0].set_title(f'Pendulum angle with A={A} and omega={omega_drive}')
        # and phase space
        axs[1].plot(rad2deg(theta_wrapped), rad2deg(d_theta))
        axs[1].plot(theta0, d_theta0, 'o', c='black', ms=10, label='Start')
        axs[1].set_xlabel('Theta [deg]')
        axs[1].set_ylabel('Pendulum angular velocity [rad/s]')
        axs[1].set_title(f'Phase space plot')
        axs[1].legend()
        plt.show()
        plt.close()










   



if __name__ == "__main__":
    main()

