from typing import Tuple

from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten


def mlp(input_shape: Tuple[int, ...],
        output_shape: Tuple[int, ...],
        layer_size: int=128,
        dropout_amount: float=0.2,
        num_layers: int=3) -> Model:
    """
    Simple multi-layer perceptron: just fully-connected layers with dropout between them, with softmax predictions.
    Creates num_layers layers.
    """
    num_classes = output_shape[0]

    model = Sequential()
    
    # Don't forget to pass input_shape to the first layer of the model
    ##### Your code below (Lab 1)
    #Input layer that takes input data shape
    for i in range(num_layers):
        model.add(Dense(64, activation='relu', input_dim=20))
        model.add(Dropout(0.5))
        
    model.add(Dense(10, activation='softmax'))
    ##### Your code above (Lab 1)

    return model

