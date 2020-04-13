import os
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request

app = Flask(__name__)

INPUT_MODEL_CONFIG = "/conf/frozen_inference_graph.pb"
INPUT_MODEL_CLASSES = "/conf/coco_labels.txt"

def ReadLabelFile(file_path):
        with open(file_path, 'r') as f:
                lines = f.readlines()
        ret = {}
        for line in lines:
                pair = line.strip().split(maxsplit=1)
                ret[int(pair[0])] = pair[1].strip()
        return ret

@app.route('/process', methods=['POST','PUT'])
def upload_file():
        file = request.files['image_file']

        picture = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

        initial_h, initial_w, channels = picture.shape
        frame = cv2.resize(picture, (300, 300))
        frame = frame[:, :, [2, 1, 0]]  # BGR2RGB
        frame = frame.reshape(1, frame.shape[0], frame.shape[1], 3)

        out = sess.run([sess.graph.get_tensor_by_name('num_detections:0'),
                sess.graph.get_tensor_by_name('detection_scores:0'),
                sess.graph.get_tensor_by_name('detection_boxes:0'),
                sess.graph.get_tensor_by_name('detection_classes:0')],
                feed_dict={'image_tensor:0': frame})

        output = ""
        num_detections = int(out[0][0])

        for i in range(num_detections):
                classId = int(out[3][0][i])
                score = float(out[1][0][i])

                output = output + "Class: " + labels[classId] + " with confidence: " + str(score) + "\n"

        return output

labels = ReadLabelFile(INPUT_MODEL_CLASSES) 

tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True

with tf.gfile.FastGFile(INPUT_MODEL_CONFIG, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

sess = tf.Session(config=tf_config)
sess.graph.as_default()
tf.import_graph_def(graph_def, name='')

if __name__ == '__main__':
        app.run()
