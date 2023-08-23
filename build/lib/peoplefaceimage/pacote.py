import cv2 as cv
import os

class DetectaFace:
    """ 
    Classe responsável por detectar rostos em imagens ou em um vídeo da webcam.

    Esta classe utiliza o classificador Haar Cascade para detectar rostos em imagens ou em tempo real a partir da webcam.

    Attributes
    ----------
    imagem : str, optional
        Caminho para o arquivo de imagem a ser processado.

    Methods
    -------
    videoCaptureFace()
        Captura um vídeo da webcam e detecta rostos em tempo real usando o Haar Cascade.

    load_face_cascade()
        Carrega um classificador Haar Cascade pré-treinado para detecção de faces.

    detect_faces(image, face_cascade)
        Detecta rostos em uma imagem utilizando o classificador Haar Cascade.

    main()
        Permite que o usuário escolha entre capturar vídeo da webcam ou processar uma imagem/pasta.
    """
    def __init__(self, imagem=None):
        """
        Parameters
        ----------
        imagem : str, optional
            Caminho para o arquivo de imagem a ser processado.
        """
        self.imagem = imagem

    def videoCaptureFace(self):
        """
        permite a captura de vídeo da webcam e detecta faces em cenario real.

        usa classificador Haar Cascade para detecção de faces.
        """
        webcamera = cv.VideoCapture(0)

        classificadorVideo = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


        while True:
            camera, frame = webcamera.read()

            img_cinza = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            detecta = classificadorVideo.detectMultiScale(img_cinza, scaleFactor=1.08, minNeighbors=5, minSize=(35,35))

            for(x,y,l,a) in detecta:
                cv.rectangle(frame,(x, y), (x + l, y + a),(255,0,0), 2)
                contador = str(detecta.shape[0])
                #cv.putText(frame, contador, (x + 10, y -10), cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv.LINE_AA)
                cv.putText(frame, 'Quantidade de Faces:' + contador, (10,450), cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv.LINE_AA)
            cv.imshow("Video WebCamera", frame)

            if cv.waitKey(1) == ord('s'):
                break

        webcamera.release() 
        cv.destroyAllWindows()

    def load_face_cascade(self):
        """
        O método load_face_cascade carrega um classificador Haar Cascade 
        
        classificador pré-treinado para detecção de faces.
        """
        face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        return face_cascade

    def detect_faces(self, image, face_cascade):
        """
        usa o classificador carregado para detectar rostos em uma imagem. 
        
        Ele desenha retângulos ao redor das faces detectadas.
        """
        image_copy = image.copy()

        # Detecta rostos na imagem
        face_rectangles = face_cascade.detectMultiScale(image_copy, scaleFactor=1.09, minNeighbors=5)

        for (x, y, w, h) in face_rectangles:
            cv.rectangle(image_copy, (x, y), (x+w, y+h), (0, 0, 255), 5)

        return image_copy, len(face_rectangles)
    
    def main(self):
        """
        permite que o usuário escolha entre capturar vídeo da webcam, processar uma imagem específica.
         
        ou, processar todas as imagens em uma pasta.
        """
        face_cascade = self.load_face_cascade()
        while True:
            print('-'*60)
            print('| Digite "sair" caso deseje encerrar o programa!           |')
            print('| Digite "video" caso deseje capturar faces pela webcam    |')
            print('-'*60)
            entrada = input("Digite o caminho para a pasta ou para o arquivo de imagem: ")
            obj = DetectaFace(entrada)
            if entrada == 'sair':
                break
            elif entrada == 'video':
                obj.videoCaptureFace()

            # Verifica se a entrada é uma pasta
            elif os.path.isdir(entrada):
                pasta_imagens = entrada
                pasta_saida = 'saida'

                # Cria a pasta de saída se ela não existir
                if not os.path.exists(pasta_saida):
                    os.makedirs(pasta_saida)

                # Obtém a lista de arquivos na pasta
                lista_arquivos = os.listdir(pasta_imagens)

                for arquivo in lista_arquivos:
                    # Verifica se o arquivo é uma imagem (extensão .jpg, .jpeg, .png, etc.)
                    if arquivo.endswith(('.jpg', '.jpeg', '.png')):
                        # Cria o caminho completo para a imagem
                        caminho_imagem = os.path.join(pasta_imagens, arquivo)
                        # Verifica se o caminho da imagem existe
                        if os.path.exists(caminho_imagem):

                            # Carrega a imagem e converte para escala de cinza
                            image = cv.imread(caminho_imagem)
                            gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

                            # Detecta os rostos na imagem
                            result_image, num_faces = obj.detect_faces(gray_image, face_cascade)

                            print('Quantidade de faces em', arquivo, ':', num_faces)

                            # Salva a imagem com os retângulos na pasta de saída
                            caminho_saida = os.path.join(pasta_saida, arquivo)
                            cv.imwrite(caminho_saida, result_image)
                        else:
                            print('O caminho da imagem não foi encontrado:', caminho_imagem)

                    else:
                        print("Entrada invalida. \nCertifique-se de fornecer um arquivo de imagem valido ou o caminho para uma pasta contendo imagens.")

                cv.destroyAllWindows()

            else:
                # A entrada é um arquivo de imagem
                # Verifica se o arquivo é uma imagem (extensão .jpg, .jpeg, .png, etc.)
                if entrada.lower().endswith(('.jpg', '.jpeg', '.png')):
                    # Carrega a imagem e converte para escala de cinza
                    image = cv.imread(entrada)
                    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

                    # Detecta os rostos na imagem
                    result_image, num_faces = obj.detect_faces(gray_image, face_cascade)

                    print('Quantidade de faces:', num_faces)

                    # Salva a imagem com os retângulos na pasta de saída
                    caminho_saida = os.path.join(os.path.dirname(entrada), 'saida', os.path.basename(entrada))
                    cv.imwrite(caminho_saida, result_image)

                    cv.imshow("Faces", result_image)
                    cv.waitKey(0)

                    cv.destroyAllWindows()
                else:
                    print("Entrada inválida. Certifique-se de fornecer um arquivo de imagem válido ou o caminho para uma pasta contendo imagens.")

            cv.destroyAllWindows()
