# ComparadorDeCSV
Objetivo é ter uma GUI onde é possível selecionar dois arquivos CSV 
e obter o resultado da comparação na tela


![](docs/comparador.png)

# Executável
Para criar o executável é preciso passar os templates:
> pyinstaller --onefile --add-data 'templates/*;datacompy/templates/' main.py --noconsole
