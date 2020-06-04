
from datetime import datetime
import logging
import os
from time import sleep

from picamera import PiCamera
import toml
import dropbox

with open('config.toml', 'r') as fo:
    config = toml.load(fo)

logging.basicConfig(filename=config['log_path'], level=logging.DEBUG)


def send_to_dropbox(fpath, destination):
    '''
    Send a file to Dropbox
    '''

    with open(fpath, 'rb') as fo:
        data = fo.read()

    fname = os.path.basename(fpath)

    try:
        res = dbx.files_upload(data, '{}/{}'.format(destination, fname))
    except Exception as e:
        logging.error('Exception occured: {}'.format(str(e)))


if __name__ == '__main__':

    dbx = dropbox.Dropbox(config['dropbox']['access_token'])
    counter = 0

    with PiCamera() as camera:

        camera.resolution = (1280, 720)
        camera.brightness = 50
        camera.zoom = (0.0, 0.0, 1.0, 1.0)

        while True:
            dt = datetime.now().isoformat()
            fpath = os.path.join(config['image_path'],
                                 'img_{}_{}.jpg'.format(counter, dt))
            camera.annotate_text = dt
            camera.capture(output=fpath)
            logging.info('saving {}'.format(fpath))
            if 'dropbox' in config.keys():
                logging.info('sending to dropbox ...')
                send_to_dropbox(fpath, config['dropbox']['destination_path'])
                logging.info('sending to dropbox done.')
            sleep(30)
            counter += 1
