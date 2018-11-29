import json
import os
from os import listdir
from os.path import isfile, join

import cv2

from images.cropping import crop_to_centered_square


class Sample:
    def __init__(self, name, diagnosis, image_dim, filename):
        self.filename = filename
        self.image_dim = image_dim
        self.name = name
        self.diagnosis = diagnosis

    def get_image(self):
        '''
        Returns a square NumPy matrix of the RGB triplets in the central square of this Sample's image.
        For example, if this image is 1000x760, then it returns a 760x760x3 matrix.
        :return: a square NumPy matrix of the RGB triplets in the central square of this Sample's image.
        '''
        return crop_to_centered_square(self.get_image_raw())

    def get_image_raw(self):
        return cv2.imread(self.filename)

    def get_grayscale_image(self):
        '''
        Returns a NumPy matrix of grayscale valeus for each pixel
        :return:
        '''
        return cv2.cvtColor(self.get_image(), cv2.COLOR_BGR2GRAY)

    @staticmethod
    def _get_metadata_file_names(dirname):
        return [join(dirname, f) for f in listdir(dirname) if isfile(join(dirname, f)) and f.endswith("json")]

    @staticmethod
    def get_samples(dirname):
        return [Sample.load_sample(open(filename)) for filename in Sample._get_metadata_file_names(dirname)]

    @staticmethod
    def load_sample(file):
        sample_json = json.load(file)
        acquisition_data = sample_json[u'meta'][u'acquisition']
        return Sample(
            sample_json[u'name'],
            sample_json[u'meta'][u'clinical'][u'diagnosis'],
            (acquisition_data[u'pixelsX'], acquisition_data[u'pixelsY']),
            os.path.dirname(file.name) + "/" + sample_json[u'name'] + ".jpg"
        )
