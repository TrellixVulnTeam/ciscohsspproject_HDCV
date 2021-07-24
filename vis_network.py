import networkx as nx
import pandas as pd
from pyvis.network import Network

DATA_PATH = './data/book1.csv'

df = pd.read_csv(DATA_PATH)
G = nx.from_pandas_edgelist(df, source='Source', target='Target', edge_attr='weight')
net = Network(notebook=True)
net.from_nx(G)
net.show('example.html')