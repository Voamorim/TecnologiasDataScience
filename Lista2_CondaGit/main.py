from label_propagation import LabelPropagation

import networkx as nx

INPUT_FOLDER = 'Input'

INPUT_FILE1 = f'{INPUT_FOLDER}/rede1_duas_comunidades.csv'
INPUT_FILE2 = f'{INPUT_FOLDER}/rede2.csv'
INPUT_FILE3 = f'{INPUT_FOLDER}/zachary.csv'

def run_test(input_file:str):
    lp =LabelPropagation()
    lp.read_graph(input_file)
    
run_test(INPUT_FILE1)
