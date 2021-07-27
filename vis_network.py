import networkx as nx
import pandas as pd
from pyvis.network import Network

DATA_FOLDER = './data'
EXAMPLE_PATH = './data/book1.csv'
DATA_PATH = './data/topology.json'

def createHTML(path):
    if path.endswith('.csv'):
        df = pd.read_csv(path)
        G = nx.from_pandas_edgelist(df, source='Source', target='Target') # source and target depend on file
        net = Network(notebook=True)
        net.from_nx(G)
        net.show('example.html')

    elif path.endswith('.json'):
        df = pd.read_json(path)
        G = nx.from_pandas_edgelist(df, source='source', target='target') # error when trying to access source/target in json
        net = Network(notebook=True)
        net.from_nx(G)
        net.show('topology.html')

if __name__ == "__main__":
    createHTML(EXAMPLE_PATH)