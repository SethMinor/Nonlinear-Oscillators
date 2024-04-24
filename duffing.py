# RHS of the Duffing Equation
# Define x'=v, and v'=-d*v-k*x-bx^3+gamma*fcn
# with Y := (x,v,params)
def duffing(t,Y):
    # Initialize params
    params = Y[2:6]
    k,d,b,gamma = params[0],params[1],\
                  params[2],params[3]

    # Compute RHS
    xprime = Y[1]
    vprime = -d*Y[1]-k*Y[0]-b*(Y[0]**3)
    Yprime = [xprime, vprime, 0,0,0,0]
    return Yprime
