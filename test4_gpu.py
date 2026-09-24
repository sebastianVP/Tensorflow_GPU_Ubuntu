
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import time

# Verificar si TensorFlow detecta la GPU
gpus = tf.config.list_physical_devices('GPU')
if not gpus:
    print("❌ No se detectaron GPUs en TensorFlow.")
else:
    print(f"✅ Se detectaron {len(gpus)} GPU(s):")
    for gpu in gpus:
        print(f"- {gpu}")

# Función para entrenar un modelo simple en un dispositivo específico
def train_mnist(device):
    with tf.device(device):
        # Cargar datos de MNIST
        (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
        x_train = x_train / 255.0  # Normalizar los datos

        # Definir un modelo simple
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        # Medir tiempo de entrenamiento
        start = time.time()
        model.fit(x_train, y_train, epochs=100, batch_size=64, verbose=0)
        return time.time() - start

# Entrenar en CPU
cpu_time = train_mnist('/CPU:0')
print(f"Tiempo de entrenamiento en CPU: {cpu_time:.2f} segundos")

# Entrenar en GPU (si está disponible)
if gpus:
    gpu_time = train_mnist('/GPU:0')
    print(f"Tiempo de entrenamiento en GPU: {gpu_time:.2f} segundos")

    if gpu_time < cpu_time:
        print("✅ La GPU está funcionando correctamente y acelerando el entrenamiento.")
    else:
        print("⚠️ La GPU no parece estar acelerando el entrenamiento. Revisa tu configuración.")
