import tensorflow as tf
import argparse
import os
import glob
import ntpath

FLAGS = None


def run(model):
    # Unpersists graph from file
    with tf.gfile.FastGFile(model, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    for image in images:
        # Read in the image_data
        image_data = tf.gfile.FastGFile(image, 'rb').read()

        # Get model label name
        model_name = ntpath.basename(model)
        label = model_name.split('_')[0]

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

            predictions = sess.run(softmax_tensor,
                                   {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            # for node_id in top_k:
            human_string = label
            score = predictions[0][0]
            print('%s (score = %.5f)' % (human_string, score))

            filename = 'results.txt'
            with open(filename, 'a+') as f:
                f.write('\n**{0}**\n'.format(image))
                # for node_id in top_k:
                human_string = label
                score = predictions[0][0]
                f.write('%s (score = %.5f)\n' % (human_string, score))


def get_models():
    files = []
    for file in glob.glob(os.path.join(FLAGS.model_dir, '*.pb')):
        files.append(file)
    return files


def get_images():
    files = []
    extensions = ['jpg', 'jpeg']
    for extension in extensions:
        for file in glob.glob(os.path.join(FLAGS.image_dir, '*.' + extension)):
            files.append(file)
    return files


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_dir", help="directory of images to be processed")
    parser.add_argument("--model_dir", help="directory of graphs/models to be executed")
    FLAGS = parser.parse_args()

    if FLAGS.model_dir:
        model_file = FLAGS.model_dir
    if FLAGS.image_dir:
        file_name = FLAGS.image_dir

    models = get_models()
    images = get_images()

    for model in models:
        run(model)
