# About

Here I provided a short-guide of experimental acquisition data. I summarized the main things you need to take into account but https://github.com/gcarrascohuertas is not responsible for the bad use of this guide and its consequences over materials and people involved. Please, be careful and document all steps you perform. 

# Electrochemical setup


First you need following materials in order to perform experiments:

- Nitrogen and Oxygen gas cylinder with appropriate security system (e.g. https://www.airliquide.com )
- Rotating disk electrode equipment (e.g. https://www.metrohm.com/en/products/AUTRDES )
- Three-electrode jacket cell with two-way gas purge
- Potentiostat which can perform Cyclic voltammetry, Chronoamperometry and Electrochemical impedance spectroscopy (e.g. Autolab PGSTAT302N - High Performance , https://www.metrohm-autolab.com/Products/Echem/NSeriesFolder/PGSTAT302N )
- PC with electrochemical acquisition software (e.g. NOVA software,  https://metrohm-autolab.com/Products/Echem/Software/Nova.html )

- Three-electrode cell

    - Platinum mesh as counter electrode (CE)
    - Ag/AgCl/KCl (3.5M) as reference electrode (RE)
    - Your working electrode (WE). Here I used a carbon slurry deposited over a polished rotating-glassy carbon electrode (GC, 4 mm diameter). Carbon slurry consists of 5 mg (carbon  material after going through a 150 microns sieve), ethanol (170 µl) and Nafion 117 (5 wt%, 47.5 µl). Slurry was sonicated for 5 minutes and then was drop-coated (7 µl of the slurry) over a rotating-disk tip (try to fulfill all the glassy carbon active area.


- Electrolyte
    - Here you can use different electrolytes (e.g. 0.1 M KOH, 0.5 M H2SO4 , 0.1 M HClO4, etc..). In the example provided here contained in folder carbon_superP I used 0.1 M KOH.


# Electrochemical techniques

Electrochemical techniques performed are cyclic voltammograms with a staircase profile (CV), Chronoamperometry (CA) and Electrochemical impedance spectroscopy (EIS).

   - Cyclic voltammograms with a staircase profile (CV) parameters: Potential windows have to be ranged in the optimum potential windows of your electrode-electrolyte system. In the example provided here I used a potential window which varies from 0.1 to -0.9 V  vs. VRef repeated 3 times at 10 mV/s fixed scan rate. Upper vertex and Lower vertex were set to 0.11 and -0.9 V vs. VRef. Step was set to -0.00244 V

   - Chronoamperometry (CA) parameters: Analysis only for 1600 rpm in a O2 saturated electrolyte.
   
   - Electrochemical impedance spectroscopy (EIS): First activate the cell and measure OCP  with 10 seconds duration, interval time of 0.1, time to average 5 seconds and dE/dt limit of 1E-06 V/s. Second step is to apply 10 mV perturbation vs. OCP measured previously. Third step is to wait 5 seconds. Four step is to perform EIS measurement with following parameters: (First applied frequency: 1E+05 Hz, last applied frequency 0.1 Hz, Number of points of freq per decade 10, Amplitude 10 and wave type sine with internal correction. 

# Electrochemical measurements

In order to follow recomendatios of https://link.springer.com/article/10.1007/s12678-017-0378-6#citeas , first the electrolyte is thermostated at 298 K and then purged with high purity Nitrogen for at least 30 min prior to Nitrogen measurement. Once nitrogen measurements are achieved electrolyte is purged with Oxygen for at least 30 min prior to Oxygen measurements. For purging you can use a large stainless steel needle. 

# Data treatment. Koutecky-Levich Analysis

Before you obtain results from data read this website for undestand Koutecky-Levich Analysis:

https://pineresearch.com/shop/kb/theory/hydrodynamic-electrochemistry/koutecky-levich-analysis/

The Koutecký–Levich equation models the measured electric current at an electrode from an electrochemical reaction in relation to the kinetic activity and the mass transport of reactants. The Koutecky-Levich (K-L) analyses of the RDE data derived from the limiting current measured at various potentials. The number of electrons transferred per O2 molecule (n) was calculated from these plots using the K-L equation. 

Following parameters were used in data contained in folder carbon_superP:

- Scan rate (ν):     0.01004 cm2/s
- Concentration of O2 at 298 K (C-02):     1.39e-3 mol L-1 (KOH 0.1 M at 298 K)
- Diffusion constant of O2 (D-O2):     1.9e-5 cm2/s (KOH 0.1 M at 298 K)
- Faraday constant : 96485 

# Experimental NOVA software routine 

Experimental sequence screenshots are attached in this project.  Due to NOVA software is licensed if you want NOVA software sequence for Nitrogen also Oxygen measurements do no hesitate to contact me at :  gasparcarrascohuertas@gmail.com



 
