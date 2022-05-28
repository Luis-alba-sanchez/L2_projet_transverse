from outils import *
from réseaux_neurones_profond import *

# parametres = initialisation([2, 32, 32, 1])
# toPrint_dictionnary(parametres)
#
# X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=0)
#
# activations = forward_propagation(X, parametres)
# toPrint_dictionnary(activations)
#
# grad = back_propagation(y, activations, parametres)

X, y = make_circles(n_samples=100, noise=0.1, factor=0.3, random_state=0)
X = X.T
y = y.reshape((1, y.shape[0]))

print('dimensions de X:', X.shape)
print('dimensions de y:', y.shape)

plt.scatter(X[0, :], X[1, :], c=y, cmap='summer')
plt.show()
deep_neural_network(X, y, hidden_layers=(16, 16, 16), learning_rate=0.1, n_iter=3000)
