from PIL import Image

# Abrir a imagem
caminho = r"C:\Users\weber\Downloads\finalcompontos.png"
caminho.strip('""')
imagemCor = Image.open(caminho)
# Obter as dimensões da imagem
largura, altura = imagemCor.size
# Criar uma nova imagem em tons de cinza
imagemCinza = Image.new("L", (largura, altura))
indexpartidaxy, indexchegadaxy = [], []
caminho2 = caminho.split('\\')

diretorio = len(caminho2)-1
caminho2 = "\\".join(caminho2[0:-1])

# Iterar sobre cada pixel na imagem colorida
for x in range(largura):
    for y in range(altura):
        # Obter o valor de cada canal de cor (R, G, B)
        (r, g, b) = imagemCor.getpixel((x, y))

        # Calcular a média dos valores de R, G e B para obter o tom de cinza
        cinza = int((r + g + b) / 3)

        if not indexpartidaxy:
            # partida é amarelo hex: ffcc5e
            if cinza == 184:
                indexpartidaxy.append(y), indexpartidaxy.append(x)

        # chegada é verde hex: 96ff5e
        if not indexchegadaxy:
            if cinza == 166:
                indexchegadaxy.append(y), indexchegadaxy.append(x)

        # Definir o pixel na imagem em tons de cinza
        imagemCinza.putpixel((x, y), cinza)

# Salvar a nova imagem em tons de cinza

imagemCinza.save(caminho2 + "\\cinza.png",)
imagemCinza.show()
