import numpy as np
class Perceptron:
    def __init__(self, num_inputs, learning_rate=0.01, num_epochs=100):
        self.num_inputs = num_inputs
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.weights = np.random.rand(num_inputs+1)
        self.bias = np.random.rand(1)

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0] * self.bias
        return self.activation_function(summation)

    def train(self,training_inputs, labels):
        for _ in range(self.num_epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights[1:]+= self.learning_rate * error * inputs
                self.weights[0] += self.learning_rate * error

if __name__ == "__main__":
    #Dados de treinamento (porta AND)
    training_inputs = np.array([0, 0], [1, 0], [0, 1], [1, 1])
    labels = np.array(([0, 0, 0, 1]))

    #Criando e treinando o Perceptron
    perceptron = Perceptron(num_inputs=2)
    perceptron.train(training_inputs, labels)

    #Testando o Perceptron treinado
    test_inputs = np.array([0, 0], [0, 1], [1, 0], [1, 1])
    for inputs in test_inputs:
        print(f"Input {inputs}, Prediction: {perceptron.predict(inputs)}")