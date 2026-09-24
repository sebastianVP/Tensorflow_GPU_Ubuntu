import tensorflow as tf
import time

# Función para medir tiempo de ejecución
def benchmark_matmul(device):
    with tf.device(device):
        a = tf.random.normal([10000, 10000])
        b = tf.random.normal([10000, 10000])

        start = time.time()
        c = tf.matmul(a, b)
        tf.linalg.norm(c)  # Asegurar que la operación se ejecuta
        return time.time() - start

# Prueba en CPU
cpu_time = benchmark_matmul('/CPU:0')
print(f"Tiempo en CPU: {cpu_time:.4f} segundos")

# Prueba en GPU (si está disponible)
gpu_time = benchmark_matmul('/GPU:0')
print(f"Tiempo en GPU: {gpu_time:.4f} segundos")

if gpu_time < cpu_time:
    print("✅ La GPU es más rápida que la CPU. TensorFlow está usando la GPU correctamente.")
else:
    print("⚠️ La GPU no parece estar acelerando el proceso. Revisa la configuración de CUDA/cuDNN.")
