import tensorflow as tf
import time

# Crear una matriz grande en la GPU
with tf.device('/GPU:0'):
    a = tf.random.normal([10000, 10000])
    b = tf.random.normal([10000, 10000])

    # Medir tiempo de multiplicación de matrices en GPU
    start = time.time()
    c = tf.matmul(a, b)
    print("Tiempo de ejecución en GPU:", time.time() - start, "segundos")
