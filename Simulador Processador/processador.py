#Tarefa 2 - Fazer um simulador de um processador com Conjunto de Instruções Baseado em Pilha.
#Requisitos:
# - Linguagem de programação: Python;
# - Pilha de 8 níveis (8 bits de largura);
# - Aritmética básica + inst. pop e pusch;
# - Comando extra: mostrar pilha;
# - Mostrar sempre o valor do Stack-Pointer.

# PC (ou CI)- Contador de instruções
# RI  - Registrador de Instruções
# UC  - Unidade de Controle
# AC  - Acumulador de Instruções
# MP  - Unidade de armazenamento ou transferencia
# UAL - Unidade Aritmética e Lógica
# REM - Registrador de Endereços de Memória
# RDM - Registrador de controle de Dados de Memória


#       Registradores Internos da CPU
# -> Contador de programa (PC) = Endereço da instrução
# -> Registrador de instrução (IR) = Instrução sendo executada
# -> Acumulador (AC) = Armazenamento temporário

#       Lista parcial de opcodes
# -> 0001 = Carrega AC da memória
# -> 0010 = Armazena AC na memória
# -> 0101 = Adiciona da memória ao AC


#Passos para execução instruções
# S1 - Busca de instruções (instruction fetch)
#      - Ciclo de Busca
#      - A CPU busca o código de operação na memória principal (MP) e armazena no
#        Registrador de Instruções (RI) da Unidade de Controle (UC)
# S2 - Decodificação da instrução (instruction decode)
#       - Ciclo de decodificação
#       - A Unidade de Controle (UC) decodifica o código de operação
# S3 - Busca de operandos (operand  fetch)
#       - Ciclo de exucução
#       - A UC busca (se houver) o(s) operando(s)
# S4 - Execução da Instrução (instruction execution)
#       - Ciclo de execução
#       - A UC comanda a execução da instrução (a operação é executada sobre o dado).
# S5 - Escrever o resultado (write Back)
#       - Ciclo de armazenamento
#       - O resultado da instrução executada é salvo na memória. Esta memória
#       pode ser temporária, para acesso rápido, ou permanente, no caso de armazenamento
#       de longo tempo.

#  Resuimindo
#  S1: A CPU busca o código de operação na MP e armazena no RI da UC
#  S2: A UC decodifica o código de operação
#  S3: A UC busca, se houver, os operandos
#  S4: A UC comanda a execução da instrução
#  S5: O resultado da instrução é salvo na memória
