# DetectaFace - Detecção de Rostos em Imagens e Vídeos usando OpenCV

Este é um pacote Python que permite a detecção de rostos em imagens individuais, em um conjunto de imagens dentro de uma pasta e a captura de rostos em tempo real usando a webcam, utilizando a biblioteca OpenCV.

## Funcionalidades

O pacote `peoplefaceimage` oferece as seguintes funcionalidades:

1. **Detectar Rostos em Imagens Individuais:** Carregue uma imagem e identifique rostos presentes nela.

2. **Detectar Rostos em um Conjunto de Imagens:** Processa várias imagens em uma pasta e detecta os rostos em cada uma delas.

3. **Capturar Rostos em Tempo Real pela Webcam:** Capture rostos em tempo real utilizando a webcam do seu dispositivo.

## Requisitos

Antes de começar, certifique-se de ter o OpenCV instalado em seu ambiente Python. Se ainda não tiver, instale-o com o seguinte comando:

```bash
pip install opencv-python
```

## Principais Características

- **Algoritmo de Detecção Avançado:** O pacote utiliza um algoritmo avançado de detecção de rostos implementado com a biblioteca OpenCV. Isso garante uma alta taxa de precisão na detecção, permitindo que você identifique com confiança rostos em suas imagens e vídeos.

- **Flexibilidade de Uso:** A classe `DetectaFace` oferece métodos específicos para diferentes tipos de detecção de rostos, desde a detecção em imagens individuais até a captura em tempo real pela webcam. Isso permite que você escolha a abordagem que melhor se adapta às suas necessidades.

- **Processamento Eficiente:** O pacote foi projetado visando a eficiência de processamento. Isso é especialmente importante ao lidar com conjuntos de imagens grandes ou streaming de vídeo em tempo real, onde o desempenho é fundamental.

## Cenários de Uso

O pacote `peoplefaceimage` pode ser aplicado em uma variedade de cenários, incluindo, mas não se limitando a:

- **Análise de Imagens e Vídeos:** Use o pacote para automatizar a detecção de rostos em grandes conjuntos de imagens ou vídeos, agilizando o processo de análise e classificação.

- **Desenvolvimento de Aplicações de Segurança:** Integre a detecção de rostos em sistemas de segurança para identificação de pessoas em tempo real.

- **Pesquisa e Mineração de Dados:** Utilize a detecção de rostos para coletar estatísticas sobre a presença de indivíduos em imagens ou vídeos, contribuindo para análises de dados mais precisas.

## Instalação

Você pode instalar o pacote `peoplefaceimage` usando o gerenciador de pacotes pip. Certifique-se de ter o OpenCV instalado em seu ambiente Python antes de prosseguir.

```bash
pip install opencv-python
```

```bash
pip install peoplefaceimage
```

## Uso

Depois de instalar o pacote, você pode realizar um teste simples para verificar suas funcionalidades. Abaixo está um exemplo de como realizar um teste básico:

```python
from peoplefaceimage import DetectaFace

# Crie uma instância da classe DetectaFace
teste = DetectaFace()

# Chame o método main para acessar as opções do pacote
teste.main()
```

Após executar este código, você verá as opções disponíveis do pacote peoplefaceimage. Siga as instruções no terminal para explorar e utilizar as funcionalidades oferecidas pelo pacote.

##

A classe `DetectaFace` oferece um conjunto de métodos para diferentes tipos de detecção de rostos. Abaixo estão exemplos de cada um deles:

### 1. Detectar Rostos em Imagens Individuais

```python
from detecta_face import DetectaFace
import cv2 as cv

# Carregue uma imagem
imagem = cv.imread('caminho_para_imagem.jpg')

# Crie uma instância da classe DetectaFace
detector = DetectaFace(imagem)

# Carregue o classificador de rostos
face_cascade = detector.load_face_cascade()

# Detecte rostos na imagem
imagem_resultado, num_faces = detector.detect_faces(imagem, face_cascade)

# Exiba a quantidade de rostos detectados
print('Quantidade de rostos:', num_faces)

# Exiba a imagem com retângulos ao redor dos rostos
cv.imshow('Rostos Detectados', imagem_resultado)
cv.waitKey(0)
cv.destroyAllWindows()

```

### 2. Detectar Rostos em um Conjunto de Imagens

```python
# Importar as bibliotecas necessárias
from detecta_face import DetectaFace
import os

# Crie uma instância da classe DetectaFace
detector = DetectaFace()

# Carregue o classificador de rostos
face_cascade = detector.load_face_cascade()

# Especifique o caminho para a pasta de imagens
caminho_pasta = 'caminho_para_pasta_de_imagens'

# Chame o método para processar imagens na pasta
detector.processar_pasta_imagens(caminho_pasta, face_cascade)
```

### 3. Capturar Rostos em Tempo Real pela Webcam

```python
# Importar as bibliotecas necessárias
from detecta_face import DetectaFace

# Crie uma instância da classe DetectaFace
detector = DetectaFace()

# Capture rostos em tempo real
detector.video_capture_face()
```
## Conclusão
O pacote DetectaFace é uma ferramenta poderosa para detecção de rostos em imagens e vídeos. Sua simplicidade de uso, alta precisão e eficiência de processamento o tornam uma escolha excelente para uma variedade de aplicações. Experimente hoje mesmo e descubra como ele pode aprimorar suas análises e projetos de visão computacional.