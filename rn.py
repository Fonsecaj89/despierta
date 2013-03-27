from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection

def crearRN():
    #Se crea la red neuronal
    n = FeedForwardNetwork()

    #Se declaran los layes de la red neuronal
    inLayer = LinearLayer(2)
    hiddenLayer = SigmoidLayer(3)
    outLayer = LinearLayer(1)

    #Se agregan los layers a la red neuronal
    n.addInputModule(inLayer)
    n.addModule(hiddenLayer)
    n.addOutputModule(outLayer)

    #Se declaran las conexiones de los nodos
    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)

    #Se establecen las conexiones en los layers de la red neuronal
    n.addConnection(in_to_hidden)
    n.addConnection(hidden_to_out)

    #Red neuronal lista para usar
    n.sortModules()

    return n


def estimularRN(rn,matriz):
    #Se estimula la red neuronal
    rn.activate(matriz)


"""FALTA REESTRUCTURAR Y PROBAR"""