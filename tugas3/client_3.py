import logging
import requests
import threading
import os

def download_gambar(url=None,namagambar=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = namagambar
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':
    threads = []
    t = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/AHb9T1UsnFyf6uXd5FSRRiq3314=/0x41:1000x708/740x500/data/photo/2020/03/01/5e5b66c42d2f1.jpg','foto1'))
    threads.append(t)
    t = threading.Thread(target=download_gambar, args=(
    'https://asset.kompas.com/crops/5dZXt_K0DJ2kOe4cTdEYcYkdROQ=/41x0:881x560/740x500/data/photo/2020/03/09/5e660def40ba9.jpeg',
    'foto2'))
    threads.append(t)

    for thr in threads:
        thr.start()