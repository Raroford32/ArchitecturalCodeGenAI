import tensorflow as tf
from .networks import build_simple_model, build_mlp_model

def train_model(model_type='cnn', epochs=10, batch_size=32, dataset='mnist'):
    """
    Train the specified model type (e.g., CNN or MLP) on a specified dataset (e.g., MNIST).
    """
    if dataset == 'mnist':
        # Load MNIST dataset
        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
        train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
        test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255
    else:
        raise ValueError(f"Dataset '{dataset}' not supported.")
    
    # Select the model type
    if model_type == 'cnn':
        model = build_simple_model(input_shape=(28, 28, 1), num_classes=10)
    elif model_type == 'mlp':
        model = build_mlp_model(input_dim=784, num_classes=10)
    else:
        raise ValueError(f"Model type '{model_type}' not supported.")
    
    # Train the model
    model.fit(train_images, train_labels, epochs=epochs, batch_size=batch_size)
    
    # Evaluate the model
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print(f"Test accuracy: {test_acc}")
    
    return model

