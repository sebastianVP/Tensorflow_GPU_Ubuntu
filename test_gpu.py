import tensorflow as tf

# Verificar la versión de TensorFlow
print(f"Versión de TensorFlow: {tf.__version__}")

# Verificar la disponibilidad de la GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "GPUs físicas,", len(logical_gpus), "GPUs lógicas")
    except RuntimeError as e:
        print(e)
else:
    print("No se detectaron GPUs.")

# Ejecutar una operación simple de TensorFlow
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(f"Datos de MNIST cargados. Tamaño del conjunto de entrenamiento: {len(x_train)}, Tamaño del conjunto de prueba: {len(x_test)}")
