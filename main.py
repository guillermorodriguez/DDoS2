import os
import argparse
from pyvis.network import Network

print('Started')

def createNetworkGraph(_matrix, out_file):
    OUTPUT_FOLDER = 'out'

    _network = Network()

    # Create hub node
    _node_weight = 1
    _color = "#{0:02x}{1:02x}FF".format(int(200/(_node_weight+1)), int(75.0/(_node_weight+1)))
    _network.add_node('10.0.0.0', label='10.0.0.0', title="Node: {0} - Weight: {1}".format('10.0.0.0', _node_weight), value=10+_node_weight, color=_color)

    # Create nodes
    for key, value in _matrix.items():
        # New node
        _node_weight = value['metric']
        _color = "#{0:02x}{1:02x}FF".format(int(200/(_node_weight+1)), int(75.0/(_node_weight+1)))
        _network.add_node(key, label=key, title="Node: {0} - Weight: {1}".format(key, _node_weight), value=10+_node_weight, color=_color)
    
        # New relationship
        _network.add_edge('10.0.0.0', key)

    _network.show(os.path.join(os.getcwd(), OUTPUT_FOLDER, out_file))

def packetMetrics(folder):
    try:
        # Pre attack data
        data = {}
        for file in os.listdir(os.path.join( os.getcwd(), folder)):
            node = file.replace('eth', '').replace('.csv', '')
            with open(os.path.join(os.getcwd(), folder, file)) as node_file:
                packet_size = 0
                routing_time = 0
                for line in node_file.readlines():
                    entry = line.split(',')
                    entry[3] = entry[3].replace('"', '')
                    if entry[3] == '10.0.0.' + str(node):
                        packet_size += int(entry[5].replace('"', ''))
                        routing_time += float(entry[1].replace('"', ''))

                if routing_time == 0:
                    data['10.0.0.' + str(node)] = {'size': packet_size, 'time': 0, 'metric': 0 }
                else:
                    data['10.0.0.' + str(node)] = {'size': packet_size, 'time': routing_time, 'metric': float(packet_size)/routing_time }
        
        return data

    except Exception as err:
        print(err)

if __name__ == "__main__":
    PRE_FOLDER = 'wireshark/pre'
    POST_FOLDER = 'wireshark/post'

    pre_ddos = packetMetrics(PRE_FOLDER)
    post_ddos = packetMetrics(POST_FOLDER)
    
    createNetworkGraph(pre_ddos, 'pre_ddos.html')
    createNetworkGraph(post_ddos, 'post_ddos.html')

print('Completed')