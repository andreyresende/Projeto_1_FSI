#Importa e verifica as versões das bibliotecas que serão utilizadas no projeto, código retirado do exemplo fornecido pelo professor
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
def Verifica_versoes():
    import sys
    print('Python: {}'.format(sys.version))
    # scipy
    import scipy
    print('scipy: {}'.format(scipy.__version__))
    # numpy
    import numpy
    print('numpy: {}'.format(numpy.__version__))
    # matplotlib
    import matplotlib
    print('matplotlib: {}'.format(matplotlib.__version__))
    # pandas
    import pandas
    print('pandas: {}'.format(pandas.__version__))
    # scikit-learn
    import sklearn
    print('sklearn: {}'.format(sklearn.__version__))

if __name__ == '__main__':
    Verifica_versoes()