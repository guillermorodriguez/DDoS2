import os
import argparse
from pyvis.network import Network

print('Started')

def createNetworkGraph(_matrix, out_file):
    OUTPUT_FOLDER = 'out'

    _network = Network()

    # Create nodes
    for key, value in _matrix.items():
        # New node
        _node_weight = len(value)
        _color = "#{0:02x}{1:02x}FF".format(int(200/(_node_weight+1)), int(75.0/(_node_weight+1)))
        _network.add_node(key, label=key, title="Node: {0} - Weight: {1}".format(key, _node_weight), value=10+_node_weight, color=_color)
    
    # Create relationships
    for source, sinks in _matrix.items():
        for sink in sinks:
            if sink not in _matrix.keys():
                # New node
                _node_weight = 1
                _color = "#{0:02x}{1:02x}FF".format(int(200/(_node_weight+1)), int(75.0/(_node_weight+1)))
                _network.add_node(sink, label=sink, title="Node: {0} - Weight: {1}".format(sink, _node_weight), value=10+_node_weight, color=_color)

            # New relationship
            _network.add_edge(source, sink)

    _network.show(os.path.join(os.getcwd(), OUTPUT_FOLDER, out_file))


if __name__ == "__main__":
    IN_FOLDER = 'in';
    INPUT_FILE = 'simulations.txt'
    REGULAR_TRAFFIC = 'network_traffic.html'
    DDoS_TRAFFIC = 'ddos.html'

    _source_file = os.path.join( os.getcwd(), IN_FOLDER, INPUT_FILE);      

    try:
        # Create data array for all nodes in landscape
        with open(_source_file, 'r') as _incidents:
            for entry in _incidents:
                print(entry)

    except Exception as err:
            print(err)

print('Completed')