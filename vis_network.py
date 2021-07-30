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

        # error when trying to access source/target in json
        G = nx.from_pandas_edgelist(df, source=[d.get('source') for d in df.links], target=[d.get('target') for d in df.links])

        net = Network(notebook=True)
        net.from_nx(G)
        net.show('topology.html')

if __name__ == "__main__":
    createHTML(DATA_PATH)