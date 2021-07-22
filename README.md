
# Electrochemical ORR reaction fit tools in Python

# Overview

ORR reaction is one of the most important of all electrochemical reactions. Unfortunately, experimental research of this reaction is really complicated due to lack of standardization and processing data time involved. 

This project aims to provide quick-tools developed in Python for ORR data treatment. These tools are based on data acquisition recommendations described in the [Kocha et. al. 2017](https://doi.org/10.1007/s12678-017-0378-6) . 
Main tools consist in obtain following parameters: 

- Stacked plots associated to nitrogen analysis.
- Stacked plots associated to oxygen analysis.
- Stacked plots associated to ORR analysis.
- Koutecky-levich plots (linealiced).
- Bode and Nyquist plots for nitrogen (0 rpm, 1000 rpm and 2000 rpm) and oxygen (1600 rpm) experiments. 
- Number of electrons involved in ORR.
- Limiting current (onset potential) for ORR.
- Halfway potential for ORR. 


# ORR reaction in electrochemistry

Oxygen reduction reaction (ORR) is also the most important reaction in life processes. In aqueous media occurs mainly by two pathways: the direct 4-electron reduction pathway from O2 to H2O, and the 2-electron reduction pathway from O2 to hydrogen peroxide (H2O2).

# ORR reaction in the laboratory

Most common technique for ORR studies is cyclic voltammetry using a rotating disk electrode (RDE), and rotating ring-disk electrode (RRDE). 
Here I used experimental protocol described in readme_experimental_protocol.md and provide an example of kind of data and results obtained by this project in the folder carbon_superP.

# Python modules required for running script

Prior to run the ORR script, install following python packages 

Matplotlib

    python -m pip install -U pip
    python -m pip install -U matplotlib

Numpy

    pip install numpy
    
Pandas

    pip install pandas
    
Glob

    pip install glob3
    
Shutil  

    pip install pytest-shutil   
    
Astropy 

    pip install astropy
    
# Bibliography



[Song C., Zhang J. (2008) Electrocatalytic Oxygen Reduction Reaction. In: Zhang J. (eds) PEM Fuel Cell Electrocatalysts and Catalyst Layers. Springer, London.](https://link.springer.com/chapter/10.1007/978-1-84800-936-3_2)

[Kocha, S.S., Shinozaki, K., Zack, J.W. et al. Best Practices and Testing Protocols for Benchmarking ORR Activities of Fuel Cell Electrocatalysts Using Rotating Disk Electrode. Electrocatalysis 8, 366–374 (2017). ](https://link.springer.com/article/10.1007/s12678-017-0378-6


# Additional coments

The Electrochemical ORR reaction fit tools in the Python version are still in it's beta state. This means that it can have some bugs and issues. However, testing and contributing is very welcome.

# Contributors

[gcarrascohuertas](https://github.com/gcarrascohuertas)
