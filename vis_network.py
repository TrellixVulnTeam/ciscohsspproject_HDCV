import networkx as nx
import pandas as pd
from pyvis.network import Network



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
        # create a new dataframe and access the source/target data
        dataf = pd.DataFrame({"Source": source, "Target":target})
        G = nx.from_pandas_edgelist(dataf, source='Source', target='Target')
        filename = 'topology.html'

    # create the network topology and store in an html file (added to current directory)
    net = Network(notebook=True)
    net.from_nx(G)
    net.show(filename)



# test by running this file directly
if __name__ == "__main__":
    createHTML(DATA_PATH)