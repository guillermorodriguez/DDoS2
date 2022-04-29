# Project
Project to simulate the simulation of the data from a DDoS attack via a Linux VM. The project creates a custom topology through the
custom_topology.py file and creates the network graphs from the retrieved data packet files through the main.py file.

# Run Instructions
Run the code through the python command line as provided below to generate the network graphs pre and post DDoS attach.
> python main.py
Run the command as given below to create the custom topology in mininet (i.e. via Ubuntu).
> sudo mn --custom custom_topology.py --topo=ddostopology

# Requirements
Python:     3.9.12
mininet:    2.3.0
pyvis:      0.1.9

Installation Instructions
pip install pyvis

# Operating System
Ubuntu      16.04.6 LTS

# Output
The program outputs the network graphs for a denial of service attack node structure as well as a graph showing the basic network 
configuration.

# Router Range:
May be found in the routes/routes.txt file.

Hub Node: 6
Node Ranges: 6 to 67211 - 6 to 82054

Removed nodes: 67211 & 82054

# Contributors
Guillermo Rodriguez     - Section: D01 - R00821937
Yaswanth Kumar Chaganti - Section: 003 - R11801037
Pratyush Kumar          - Section: 005 - R11563270
Vijay Kumar Thanikonda  - Section: 003 - R11799896
Jaswanth Vishnumolakala - Section: 003 - R11803373
