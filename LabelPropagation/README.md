# Atividade Prática 2: Label Propagation 

**Aluno**: Vítor Oliveira Amorim
**Professora**: Carolina Ribeiro Xavier
**Disiciplina**: Tecnologias para Data Science

--- 

## Descrição

A presente atividade desenvolvida para a disciplina de Tecnologias para Data Science contém a implementação do algoritmo de **Propagação de Rótulos (Label Propagation)** para detecção de comunidades em redes.

---

## Criar e Ativar o Ambiente Conda

```bash
conda env create -f environment.yml
conda activate label_propagation
```
## Execução

```bash
python3 main.py
```

---

## Resultados 
### Rede 1: rede1_duas_comunidades.csv

**Saída:**
```
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Rede: ../input/rede1_duas_comunidades.csv
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Labels: [5, 5, 5, 5, 5, 5]
```

### Rede 2: rede2.csv

**Saída:**
```
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Rede: ../input/rede2.csv
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Labels: [3, 3, 3, 3, 4, 4, 4]
```

### Rede 3: zachary.csv

**Saída:** 
```
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        Rede: ../input/zachary.csv
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Labels: [33, 1, 1, 1, 1, 1, 1, 33, 1, 1, 1, 1, 1, 1, 1, 33, 1, 33, 33, 33, 33, 33, 1, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33]
```

## Dificuldades Encontradas

- **Uso da biblioteca `numpy`:** Identificar onde utilizar as estruturas fornecidas pela biblioteca agregaria valor à implementação, além de ser pouco familizarizado com seus métodos e estruturas.
- **Uso da biblioteca `networkx`:** Necessidade de consultas recorrentes à documentação da biblioteca para traduzir a lógica de manipulação de grafos para os métodos da biblioteca.
- **Inconsistênsias nos arquivos de entrada:** O terceiro arquivo de testes (`zachary.csv`) utilizava identificadores com convenção diferente dos demais (não indexados em 0), o que exigiu substituir a estrutura de listas implementada anteriormente para dicionários, garantindo que o algoritmo funcione corretamente independentemente dos identificadores utilizados no arquivo de entrada.
