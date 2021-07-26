# About

Here I provided a short-guide of experimental acquisition data. I summarized the main things you need to take into account but [gcarrascohuertas]( https://github.com/gcarrascohuertas) is not responsible for the bad use of this guide and its consequences over materials and people involved. Please, be careful and document all steps you perform. 

# Electrochemical setup


First you need following materials in order to perform experiments:

- Nitrogen and Oxygen gas cylinder with appropriate security system (e.g. https://www.airliquide.com )
- Rotating disk electrode equipment (e.g.[RDE Metrohm](https://www.metrohm.com/en/products/AUTRDES) )
- Three-electrode jacket cell with two-way gas purge (gas-inflow and gas-outflow) ([Scheme](https://www.researchgate.net/figure/Schematic-of-a-typical-water-jacketed-RDE-cell_fig8_324230952))
-  [Laboratory  water chiller](https://www.ika.com/en/Products-Lab-Eq/Temperature-Control-Circulation-and-Immersion-thermostat-csp-272/ICC-basic-pro-12-cpdt-10000414/) connected to jacket cell at 298 K.
- Potentiostat which can perform Cyclic voltammetry, Chronoamperometry and Electrochemical impedance spectroscopy (e.g. [Autolab PGSTAT302N - High Performance](https://www.metrohm-autolab.com/Products/Echem/NSeriesFolder/PGSTAT302N) )
- PC with electrochemical acquisition software (e.g. [NOVA software](https://metrohm-autolab.com/Products/Echem/Software/Nova.html ))

- Three-electrode cell

    - Platinum mesh as counter electrode (CE)
    - Ag/AgCl/KCl (3.5M) as reference electrode (RE)
    - Your working electrode (WE). Here I used a [Carbon Super P](https://www.alfa.com/es/catalog/H30253/) slurry deposited over a polished rotating-glassy carbon electrode (GC, 4 mm diameter, Metrohm). Carbon slurry consists of 5 mg (carbon  material after going through a 150 microns sieve), ethanol (170 µl, Merck) and Nafion 117 (5 wt%, 47.5 µl, Merck). Slurry was sonicated for 5 minutes and then was drop-coated (7 µl of the slurry) over a rotating-disk tip (try to fulfill all the glassy carbon active area).


- Electrolyte
    - Here you can use different electrolytes depeding on your WE material (e.g. 0.1 M KOH, 0.5 M H<sub>2</sub>SO<sub>4</sub> , 0.1 M HClO<sub>4</sub>, etc..). In the example provided here contained in folder carbon_superP  0.1 M KOH was used.


# Electrochemical techniques

Electrochemical techniques performed are cyclic voltammograms with a staircase profile (CV), Chronoamperometry (CA) and Electrochemical impedance spectroscopy (EIS).

   - Cyclic voltammograms with a staircase profile (CV) parameters: Potential windows have to be ranged in the optimum potential windows of your electrode-electrolyte system. In the example provided here I used a potential window which varies from 0.1 to -0.9 V  vs. V<sub>Ref</sub> repeated 3 times at 10 mV/s fixed scan rate. Upper vertex and Lower vertex were set to 0.11 V and -0.9 V vs. V<sub>Ref</sub> . Step was set to -0.00244 V

   - Chronoamperometry (CA) parameters: This analysis was performed only for 1600 rpm in a O<sub>2</sub> saturated electrolyte.
   
   - Electrochemical impedance spectroscopy (EIS): First activate the cell and measure OCP  with 10 seconds duration, interval time of 0.1, time to average 5 seconds and dE/dt limit of 1E-06 V/s. Second step is to apply 10 mV perturbation vs. OCP measured previously. Third step is to wait 5 seconds. Four step is to perform EIS measurement with following parameters: (First applied frequency: 1E+05 Hz, last applied frequency 0.1 Hz, Number of points of freq per decade 10, Amplitude 10 and wave type sine with internal correction. 

# Electrochemical measurements

In order to follow recomendatios of [Kocha et.al., 2017](https://link.springer.com/article/10.1007/s12678-017-0378-6#citeas) , first the electrolyte is thermostated at 298 K and then purged with high purity Nitrogen for at least 30 min before each N<sub>2</sub> measurements  at 0 rpm, 1000 rpm and 2000 rpm. 
Once nitrogen measurements are achieved electrolyte is purged with Oxygen for at least 30 min prior to O<sub>2</sub> measurements at 0 rpm, 250 rpm, 500 rpm, 750 rpm, 1000 rpm , 1200 rpm,  1400 rpm, 1600 rpm, 1800 rpm and 2000 rpm. For purging you can use a large stainless steel needle inserted into a septum (see [scheme](https://www.researchgate.net/figure/Schematic-of-a-typical-water-jacketed-RDE-cell_fig8_324230952)).

WARNING:  Save experimental ORR-results files as following examples in order to avoid problems with cronological order:
            - In case of nitrogen analysis:  N2_2000rpm   for 2000 rpm analysis 
            - In case of oxygen analysis:  O2_0250rpm  for 250 rpm analysis 

# Experimental NOVA software routine 

Once you finish setting-up all the electrochemical cell components. Create two experimental sequences (one for nitrogen and one for oxygen) with the parameteres displayed in the  screenshots attached in this project.  

WARNING: Due to NOVA software is licensed I can not upload sequence (.nox file). If you want NOVA software sequence for Nitrogen also Oxygen measurements (.nox files) do no hesitate to contact me at :  gasparcarrascohuertas@gmail.com


# Data treatment. First step: Reference data to RHE 

All tools cretaed in this project are refered to RHE as reference scale potential . In order to obtain referenced potential to RHE, first see :

   - http://www.consultrsr.net/resources/ref/refpotls3.htm
   - http://www.consultrsr.net/resources/ref/refpotls.htm#ssce

Applying  E(RHE)  equation:

E(RHE) = E(Ag/AgCl) + 0.059*(pH) + Eo(Ag/AgCl)

with following parameters for our electrode used in this project (Ag/AgCl , 3.5M KCl):

   - Eo(Ag/AgCl) = 0.1976 V at 298 K.
   - E(Ag/AgCl) = Working potential = Ag/AgCl (3.5M KCl) +0.205 V.
   - pH = pH of solution , in our case was 12.8 for KOH 0.1 M.
   
# Data treatment. Second step: Proccesing ORR curves 

Data from nitrogen 0 rpm analysis will be substrated to oxygen 0 rpm analysis (O2_0rpm - N2_0rpm)

Data from nitrogen 1000 rpm analysis will be substrated to oxygen 250 , 500 , 750 and 1000 rpm analysis:

   - O2_250rpm - N2_1000rpm
   - O2_500rpm - N2_1000rpm
   - O2_750rpm - N2_1000rpm
   - O2_1000rpm - N2_1000rpm

Data from nitrogen 2000 rpm analysis will be substrated to oxygen 1200 , 1400 , 1600 and 2000 rpm analysis:

   - O2_1200rpm - N2_2000rpm
   - O2_1400rpm - N2_2000rpm
   - O2_1600rpm - N2_2000rpm
   - O2_2000rpm - N2_2000rpm

# Data treatment. Third step: Koutecky-Levich Analysis

Before you obtain results from data read this website for undestand Koutecky-Levich Analysis:

https://pineresearch.com/shop/kb/theory/hydrodynamic-electrochemistry/koutecky-levich-analysis/

The Koutecký–Levich equation models the measured electric current at an electrode from an electrochemical reaction in relation to the kinetic activity and the mass transport of reactants. The Koutecky-Levich (K-L) analyses of the RDE data derived from the limiting current measured at various potentials. The number of electrons transferred per O2 molecule (n) was calculated from these plots using the K-L equation. 

Following parameters were used in data contained in folder carbon_superP:

- Scan rate (ν):     0.01004 cm<sup>2</sup>/s
- Concentration of O2 at 298 K (C-0<sub>2</sub>):     1.39e-3 mol L<sup>-1</sup> (KOH 0.1 M at 298 K)
- Diffusion constant of O<sub>2</sub> (D-O<sub>2</sub>):     1.9e-5 cm<sup>2</sup>/s (KOH 0.1 M at 298 K)
- Faraday constant : 96485 C / mol



 
