import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# --- Select conv layers to visualize ---
selected_layers = [
    'block4a_expand_activation',  # deep encoder
    'block6a_expand_activation',  # deeper encoder
    'top_activation',             # bottleneck
    'conv2d_13',                  # decoder middle
    'conv2d_14',                  # decoder near output
]

def compute_gradcam(img, layer_name):
    """Compute Grad-CAM heatmap for a given conv layer"""
    grad_model = tf.keras.models.Model(
        inputs=model.input,
        outputs=[model.get_layer(layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img)
        loss = tf.reduce_mean(predictions)

    grads = tape.gradient(loss, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0,1,2))

    conv_outputs = conv_outputs[0]
    heatmap = tf.reduce_sum(tf.multiply(pooled_grads, conv_outputs), axis=-1)

    heatmap = np.maximum(heatmap, 0)
    heatmap /= np.max(heatmap) + 1e-8

    heatmap = cv2.resize(heatmap, (img.shape[2], img.shape[1]))
    return heatmap

# --- Loop through all test images ---
num_images = len(x_test)   # or set to a smaller number like 10 if dataset is big

for idx in range(num_images):
    x_test_image = x_test[idx:idx+1]   # (1,H,W,3)
    y_test_mask = y_test[idx]

    plt.figure(figsize=(20, 6))

    # Original image
    img = x_test_image[0]
    img_norm = (img - img.min()) / (img.max() - img.min())

    plt.subplot(1, len(selected_layers)+2, 1)
    plt.imshow(img_norm)
    plt.axis('off')
    plt.title("Original")

    # Ground truth mask
    plt.subplot(1, len(selected_layers)+2, 2)
    if y_test_mask.ndim == 3 and y_test_mask.shape[-1] == 1:
        plt.imshow(y_test_mask[:,:,0], cmap='gray')
    else:
        plt.imshow(y_test_mask, cmap='gray')
    plt.axis('off')
    plt.title("Ground Truth")

    # Grad-CAM overlays
    for i, layer_name in enumerate(selected_layers):
        heatmap = compute_gradcam(x_test_image, layer_name)
        plt.subplot(1, len(selected_layers)+2, i+3)
        plt.imshow(img_norm)
        plt.imshow(heatmap, cmap='jet', alpha=0.5)
        plt.axis('off')
        plt.title(layer_name)

    plt.tight_layout()
    plt.show()
