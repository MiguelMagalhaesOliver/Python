from sistema import Home
from painel import Painel

# cria o sistema
sistema = Home("estoque.db")

# mangás iniciais (opcional no momento, pois vou colocar mais)
sistema.adicionar_produto("Mangá: Jujutsu Kaisen Vol. 1", 50)
sistema.adicionar_produto("Mangá: Yu Yu Hakusho Vol. 1", 40)
sistema.adicionar_produto("Mangá: JoJo Stone Ocean Vol. 1", 25)

# abre painel
Painel(sistema)