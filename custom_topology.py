from mininet.topo import Topo
import os

class DDoSTopology(Topo):
    
    def __init__(self):
        # Create custom topology for desired configuration

        Topo.__init__(self)

        IN_FOLDER = 'routes'
        IN_FILE = 'routes.txt'

        _network_matrix = {}
        with open(os.path.join(os.getcwd(), IN_FOLDER, IN_FILE), 'r') as _network_paths:
            # Build node connections
            for _entry in _network_paths:
                _source, _sink = _entry.split(',')[0], _entry.split(',')[1]
                
                _host = self.addHost(_sink)
                _switch = self.AddHost(_source)

                self.addLink(_host, _switch)

topos = { 'ddostopology': ( lambda: DDoSTopology() ) }