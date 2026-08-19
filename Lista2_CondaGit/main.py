from label_propagation import LabelPropagation

import networkx as nx
import matplotlib.pyplot as plt

INPUT_FOLDER = 'Input'

INPUT_FILE1 = f'{INPUT_FOLDER}/rede1_duas_comunidades.csv'
INPUT_FILE2 = f'{INPUT_FOLDER}/rede2.csv'
INPUT_FILE3 = f'{INPUT_FOLDER}/zachary.csv'

def run_test(input_file:str):
    lp =LabelPropagation()
    labels = lp.run(100, input_file)

    print('=-' * 30)
    print(' ' * 8, end='')
    print(f'Rede: {input_file}')
    print('=-' * 30)
    print(f'\nLabels: {labels}\n')

    fig, ax = plt.subplots(figsize=(6, 6))
    nx.draw(lp.graph, nx.spring_layout(lp.graph), node_color=list(lp.labels.values()), cmap=plt.cm.Set1, with_labels=True, ax=ax) 
    ax.set_title(f'Rede: {input_file}', fontsize=16)
    plt.show()


run_test(INPUT_FILE1)
run_test(INPUT_FILE2)
run_test(INPUT_FILE3)
