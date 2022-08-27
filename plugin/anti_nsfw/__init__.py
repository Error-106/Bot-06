print("init AntiNsfw Ai...")
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
from time import *
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
model = load_model("./plugin/anti_nsfw/nsfw.h5")
def preImage(image):
    try:
        if image.mode != 'RGB':
            image = image.convert('RGB')
    except Exception as e:
        print('error image')
        print(e)
    image = image.resize((256, 256), Image.ANTIALIAS)
    image = np.array(image) / 255.0
    image = image[tf.newaxis, ...]
    return np.array(image)
def Predict(image):
    predict = np.array(model.predict(image))[0]
    return predict
def get_tasks(img):
    labels = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']
    begin_time = time()
    image = img
    image = preImage(image)
    result = Predict(image)
    take_time = round((time() - begin_time)*1000)
    result = {'predict':labels[np.argmax(result)],'drawings':result[0], 'hentai':result[1], 'neutral':result[2], 'porn': result[3], 'sexy': result[4], 'took':take_time}
    return result
nsfws=["hentai","porn","sexy"]
isnsfw=40.0
print("Finish.")
