from setuptools import setup

VERSION = '0.0.8'
DESCRIPTION = 'Detecção de faces em imagens'
LONG_DESCRIPTION = 'Este pacote é capaz de detectar faces em imagens.'

# Carregando o conteúdo do arquivo README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="peoplefaceimage",
    version=VERSION,
    author="Victor Macedo, Luis Eduardo",  # Adicione os dois autores separados por vírgula
    author_email="victmacc@ufpi.edu.br, duardos26@gmail.com",  # Emails dos autores separados por vírgula
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['peoplefaceimage'],
    install_requires=[
        'opencv-python',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
