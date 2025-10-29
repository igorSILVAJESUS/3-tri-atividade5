inventario  = ["elmo","chapeu","espada","botas"]
busca =  input("digite um item ")
for item in inventario:
    if item == busca:
        print (f"{busca.capitalize()} foi  encontrada!")
        break
else:
        print("item não encontrado")
