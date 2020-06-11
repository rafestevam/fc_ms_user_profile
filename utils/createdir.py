import os
import stat

class CreateDir():

    @staticmethod
    def image_dir(local_dir):
        newpath = local_dir
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            os.chmod(local_dir, stat.S_IWRITE)
        return newpath