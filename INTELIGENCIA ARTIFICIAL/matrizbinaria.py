import cv2
import numpy as np


def transforma_matriz(caminho):
    # Carrega a imagem
    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    # Define um limiar para distinguir as ruas do resto
    _, imagem_binaria = cv2.threshold(imagem, 44, 100, cv2.THRESH_BINARY_INV)
    matriz = np.where(imagem_binaria == 100, 0, 1)

    # Salva a matriz em um arquivo de texto

    return matriz


def recria_imagem(arquivo_txt, caminho_imagem):
    # Carrega a matriz do arquivo de texto
    matriz = np.loadtxt(arquivo_txt, dtype=int)

    # Converte a matriz de volta para uma imagem binária
    imagem_binaria = np.where(matriz == 1, 255, 0).astype(np.uint8)

    # Inverte a imagem binária (pois a conversão anterior inverteu)
    imagem_binaria = cv2.bitwise_not(imagem_binaria)

    # Salva a imagem
    cv2.imwrite(caminho_imagem, imagem_binaria)

    return imagem_binaria
