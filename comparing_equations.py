from diffusionpotential import DiffusionPotential
from diffpot_and_psd import scenario1

# Calculating the potential with the Goldman equation, the Henderson equation
# and the approximated sigma equation

potassium = [2, 4, 6, 9]  # delta K change from baseline of 3 mM
models = []

for k in potassium:
    c = scenario1(k=k, kbase=3.0, nabase=149.0)
    model = DiffusionPotential(conc=c, tau=None, delta_t=None, t_end=None,
                               name='K+ = +'+str(k))
    models.append(model)

for model in models:
    print(model.name)
    model.goldman_eq()
    model.henderson_eq()
    model.delta_phi_eq()
    print(model.goldman)
    print(model.henderson)
    print(model.delta_phi)
