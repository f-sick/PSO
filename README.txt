This is a particle swarm optimization (PSO) implementation to find
the max value of the function:
    f(x,y) = sin(2/x)+sin(2*x)+cos(x)+sin(20/y)

pso.py contains the actual implementation of the PSO and surface.py
will generate an interactive html file the displays the surface.

pso.py only requires python3 and the std lib.

surface.py requires plotly and numpy, both of which can be installed
with pip.