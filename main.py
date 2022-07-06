from structure_code import utils


def __image(image_path):
    image_np = utils.load_image_into_numpy_array(image_path)

    utils.flip_image(image_np)

    utils.convert_gray_scale(image_np)
    return image_np


if __name__ == '__main__':
    image_path = "./images/img1.jpg"
    image_np = __image(image_path)

    inference = utils.inference(image_np)
    utils.visualizing_result(image_np, inference)
    print("Resultado gerado na pasta results")
