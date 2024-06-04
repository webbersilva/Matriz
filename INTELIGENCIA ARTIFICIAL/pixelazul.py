from PIL import Image


def pixel_azul(resultado_busca, caminho_imgcolorida):
    # Abrir a imagem
    imagemCor = Image.open(caminho_imgcolorida)
    caminho_imgcolorida_split = caminho_imgcolorida.split('\\')
    diretorio2 = "\\".join(caminho_imgcolorida_split[:])
    # Obter as dimensões da imagem
    largura, altura = imagemCor.size

    # Crie uma nova imagem com as mesmas dimensões que a imagem original
    matriz_azul = imagemCor.copy()

    # Preencha os pixels selecionados com a cor azul
    for (y, x) in resultado_busca:
        # Verifique se as coordenadas estão dentro dos limites da imagem
        if 0 <= x < largura and 0 <= y < altura:
            # Defina o pixel na imagem com a cor azul
              matriz_azul.putpixel((x, y), 255)

    matriz_azul.save("rota.png")
    matriz_azul.show()
