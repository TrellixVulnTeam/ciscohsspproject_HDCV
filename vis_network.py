import networkx as nx
import pandas as pd
from pyvis.network import Network
import random



# define data paths
DATA_FOLDER = './data'
EXAMPLE_PATH = './data/book1.csv'
DATA_PATH = './data/topology.json'



# create the html to be displayed based on the url/path
def createHTML(path):
    # example data
    if path.endswith('.csv'):
        # read the file, access source/target pairs
        df = pd.read_csv(path)
        G = nx.from_pandas_edgelist(df, source='Source', target='Target')
        filename = 'example.html'

    # router topology data
    elif path.endswith('.json'):
        df = pd.read_json(path) # creates a dataframe but source/target stored in dictionaries
        source=[d.get('source') for d in df.links]
        target=[d.get('target') for d in df.links]
        # replace router IDs with router names
        for d in df.nodes:
            replace_id_with_name(source, d)
            replace_id_with_name(target, d)

        # randomly assign green or red to routers to represent their status
        # green = router running, red = router down
        colors = {}
        for router in source:
            random_number = random.randint(1, 4)
            if random_number == 3:
                colors[router] = "red"
            else:
                colors[router] = "green"

        # create a new dataframe and access the source/target data
        dataf = pd.DataFrame({'Source': source, 'Target':target})
        # create the graph and add the colors attribute
        G = nx.from_pandas_edgelist(dataf, source='Source', target='Target')
        nx.set_node_attributes(G, colors, 'color')
        filename = 'topology.html'

    # create the network topology and store in an html file (added to current directory)
    net = Network(width='1440px', height='700px', notebook=True)
    net.from_nx(G)
    net.show(filename)



# function to replace router IDs with router names
def replace_id_with_name(id_list, name_dict):
    for index, router_id in enumerate(id_list):
        if router_id == name_dict.get('id'):
            id_list[index] = name_dict.get('name')



# test by running this file directly
if __name__ == "__main__":
    createHTML(DATA_PATH)