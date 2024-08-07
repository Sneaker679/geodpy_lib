import numpy as np
from kerr import kerr, circ

# Initial values
rs = 1 
ro = 2
a = 0.495
σ = -1 #1 or -1
assert a < rs/2
k, h = 1, 0

output_kwargs = {
    "orbit_plot_title" : "Trajectory of a star falling into a rotating blackhole",
    "orbit_pdf_name"   : "o_kerr.pdf",
    "orbit_mp4_name"   : "o_kerr.mp4",
    "velocity_pdf_name": "v_kerr.pdf",
    "plot_orbit"       : True,
    "animate"          : True,
    "plot_velocity"    : False,
    "save_pdf"         : False,
    "save_mp4"         : False,
    "v_save_pdf"       : False  
}

kerr(rs=rs, ro=ro, h=h, k=k, a=a, θ_init=0.00001, T=500, output_kwargs=output_kwargs, verbose=1, dim=3)
