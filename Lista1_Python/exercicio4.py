# parte 1

file_name = "arquivo_teste.txt"

linhas = []

with open(file_name, mode="r") as input_file:
    linhas = input_file.readlines()

print(f"numero de linhas no arquivo {file_name}: {len(linhas)}") 

# parte 2

output_file = "arquivo_saida.txt"

with open(output_file, mode="w") as outf:
    outf.writelines(linhas)
