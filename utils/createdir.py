import os

class CreateDir():

    @staticmethod
    def image_dir(local_dir):
        newpath = local_dir
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        return newpath