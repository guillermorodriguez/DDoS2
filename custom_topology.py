from mininet.topo import Topo
import os

class DDoSTopology(Topo):
    
    def build(self):
        # Create custom topology for desired configuration
        IN_FOLDER = 'routes'
        IN_FILE = 'routes.txt'

        _network_matrix = {}
        with open(os.path.join(os.getcwd(), IN_FOLDER, IN_FILE), 'r') as _network_paths:
            # Build node connections
            for _entry in _network_paths:
                _source, _sink = int(_entry[0]), int(_entry[1])
                
                if _source in _network_matrix.keys():
                    _network_matrix[_source].append(_sink)
                else:
                    _network_matrix[_source] = [_sink]

        for _key, _value in _network_matrix.items():
            # Add hosts and switches
            _switch = self.addSwitch(str(_key))

            for _host in _value:
                self.addLink(self.addHost(str(_host)), _switch)

topos = { 'ddostopology': ( lambda: DDoSTopology() ) }