def print_texto_grande(texto):
    # Código ANSI para aumentar o tamanho do texto
    codigo_ansi = '\033[0;31m'  # 1;36m representa a cor ciano
    reset_ansi = '\033[0m'      # 0m para resetar o estilo
    
    # Imprime o texto com o código ANSI
    print(f'{codigo_ansi}{texto}{reset_ansi}')

# Exemplo de uso
print_texto_grande('Texto Grande!')
