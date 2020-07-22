import glob
import os
import cv2

import psycopg2
import torch
from PIL import Image
from torchvision import transforms

from mobilefacenet import MobileFaceNet
# from mtcnn.alignment import _read_image_2_cvMat, _align_faces
# from mtcnn.mtcnn import MTCNN

loader = transforms.Compose([transforms.ToTensor(), transforms.Normalize([0.55453955, 0.42548006, 0.36506366], [0.24527807, 0.2112494, 0.19777784])])


def image_loader(image):
    """load image, returns cuda tensor"""

    image = image.resize((112, 112))
    image = loader(image).float()
    image = image.unsqueeze(0)  # this is for VGG, may not be needed for ResNet
    return image

"""
def crop_images():
    path = 'images/*'
    files = [os.path.basename(f) for f in glob.glob(path, recursive=True)]

    face_scale = 1.1
    # size of output faces
    face_size = (224, 224)

    detector = MTCNN()

    face_cascade = cv2.CascadeClassifier('mtcnn/haarcascade_frontalface_default.xml')
    for i, file in enumerate(files):
        print(i, "/", len(files))
        file_path = path[:-1] + file

        image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
        if len(faces) > 0:
            image = _read_image_2_cvMat(file_path)

            # run alignment
            result, number_of_detected, main_idx = _align_faces(image, detector, face_scale, face_size)

            filename = file_path.split("/")[-1]
            new_folder = "cropped_images/"

            if not os.path.exists(new_folder):
                os.mkdir(new_folder)

            new_filename = new_folder + filename[:-3] + 'png'

            cv2.imwrite(new_filename, cv2.cvtColor(result[main_idx], cv2.COLOR_RGB2BGR))
"""

def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    model = MobileFaceNet(512)
    model = model.to(device)
    model.load_state_dict(torch.load('model_mobilefacenet_arcface_2020-07-21-03-12_accuracy=0.9263333333333333_step=413240_final_step.pth',
                                     map_location=lambda storage, loc: storage))

    model.eval()

    path = 'cropped_images/*'
    files = [os.path.basename(f) for f in glob.glob(path, recursive=True)]

    embeddings = []
    names = []
    for i, file in enumerate(files):
        print(i, "/", len(files))
        file_path = path[:-1] + file

        image = Image.open(file_path)
        image = image_loader(image)

        embedding = model(image).detach().numpy()[0]

        embeddings.append(embedding)
        names.append(file[:-4])

    try:
        connection = psycopg2.connect(user="bcjvkxzttihwua",
                                      password="5ec611f4077ad84d4a4cfc63fcf84e7dfbcc2ed644ebea903f1d963edf89f469",
                                      host="ec2-54-217-213-79.eu-west-1.compute.amazonaws.com",
                                      port="5432",
                                      database="d8pltdd2quqsdh")

        cursor = connection.cursor()
        for n, e in zip(names, embeddings):
            postgres_insert_query = " INSERT INTO \"Person\" (name, embeddings) VALUES (%s,%s)"
            record_to_insert = (n, e.tolist())
            cursor.execute(postgres_insert_query, record_to_insert)

            # time.sleep(0.3)

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    main()
