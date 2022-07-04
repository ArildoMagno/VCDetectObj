from io import BytesIO
from PIL import Image
from six import BytesIO
from urllib.request import urlopen
from object_detection.utils import visualization_utils as viz_utils
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from structure_code import config

# SELECT THE OPTIONS TO FLIP OR CONVERT TO GRAYSCALE
flip_image_horizontally_key = False
convert_image_to_grayscale_key = False


def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.

    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.

    Args:
      path: the file path to the image

    Returns:
      uint8 numpy array with shape (img_height, img_width, 3)
    """
    image = None
    if (path.startswith('http')):
        response = urlopen(path)
        image_data = response.read()
        image_data = BytesIO(image_data)
        image = Image.open(image_data)
    else:
        img = Image.open(path)
        buf = BytesIO()
        img.save(buf, 'jpeg')
        buf.seek(0)
        image_data = buf.read()
        image = Image.open(BytesIO(image_data))
        buf.close()

    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (1, im_height, im_width, 3)).astype(np.uint8)


def flip_image(image_np):
    if flip_image_horizontally_key:
        image_np[0] = np.fliplr(image_np[0]).copy()
    return image_np


def convert_gray_scale(image_np):
    if convert_image_to_grayscale_key:
        image_np[0] = np.tile(
            np.mean(image_np[0], 2, keepdims=True), (1, 1, 3)).astype(np.uint8)
    return image_np


def inference(image_np):
    # running inference
    results = config.hub_model(image_np)

    # different object detection models have additional results
    # all of them are explained in the documentation
    result = {key: value.numpy() for key, value in results.items()}
    return result


def visualizing_result(image_np, result):
    create_result_folder()
    label_id_offset = 0
    image_np_with_detections = image_np.copy()

    # Use keypoints if available in detections
    keypoints, keypoint_scores = None, None
    if 'detection_keypoints' in result:
        keypoints = result['detection_keypoints'][0]
        keypoint_scores = result['detection_keypoint_scores'][0]

    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections[0],
        result['detection_boxes'][0],
        (result['detection_classes'][0] + label_id_offset).astype(int),
        result['detection_scores'][0],
        config.category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=.30,
        agnostic_mode=False,
        keypoints=keypoints,
        keypoint_scores=keypoint_scores,
        keypoint_edges=config.COCO17_HUMAN_POSE_KEYPOINTS)

    plt.figure(figsize=(24, 32))
    plt.imshow(image_np_with_detections[0])
    plt.savefig("./results/result.png")


def create_result_folder():
    Path("../results").mkdir(parents=True, exist_ok=True)
