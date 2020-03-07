import re
import subprocess as sp
import csv

import progressbar
import eyed3
from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup


class Songs:
    # This class contains methods for operations on songs of an artist

    def __init__(self, config, list_file):
        self.config = config
        self.list_file = list_file
        self.driver = None

    def run_driver(self):
        if self.driver is None:
            options = ChromeOptions()
            #options.headless = True
            self.driver = Chrome(chrome_options=options)

    def get_list(self, artist):
        # Get list of songs of an artist and save to file
        songs = []
        bar = progressbar.ProgressBar(maxval=100, widgets=[progressbar.Bar('=', '[', ']'), progressbar.Percentage()])
        bar.start()

        for i in range(1, 5):
            req = self.config['MUSIX_MATCH'] + '/artist/{}/{}'.format(artist.replace(' ', '-'), i)
            self.run_driver()
            self.driver.get(req)
            s = BeautifulSoup(self.driver.page_source, 'html.parser')
            links = s.find_all('a', {'class': 'title'})
            for j, a in enumerate(links):
                songs.append([artist.strip(), a.string.strip(), a['href']])
                try:
                    bar.update(i * 25 + (j * 25 / len(links)))
                except:
                    pass
        bar.finish()
        self.driver.quit()

        with open(self.list_file, 'w', encoding='utf-8') as f:
            if songs:
                w = csv.writer(f)
                w.writerows(songs)
            else:
                print('No songs!')

    def print_list(self):
        # Print the list of songs of an artist
        with open(self.list_file, 'r', encoding='utf-8') as f:
            songs = list(csv.reader(f))
            for i in range(0, len(songs)):
                print('[{:3d}] {} - {}'.format(i, songs[i][0], songs[i][1]))

    def download_item(self, index):
        # Download a song from list of songs of an artist
        with open(self.list_file, 'r', encoding='utf-8') as f:
            row = list(csv.reader(f))[index]
            song = row[0] + ' - ' + row[1] + '.mp3'

        print('Downloading {}'.format(song))
        bar = progressbar.ProgressBar(maxval=100, widgets=[progressbar.Bar('=', '[', ']'), progressbar.Percentage()])
        bar.start()
        ydlcmd = ['youtube-dl', '--extract-audio', '--newline', '--audio-format', 'mp3', '--output', song]
        if self.config['USE_PROXY']:
            ydlcmd += ['--proxy', self.config['PROXY']]
        ydlcmd.append('ytsearch1:"{}"'.format(song))
        p = sp.Popen(ydlcmd, stdout=sp.PIPE)
        while True:
            out = str(p.stdout.readline())
            if '[download]' in out:
                reg = re.search(r'(\d+\.?\d+?)%', out)
                if reg is not None:
                    bar.update(int(float(reg.group(1))))
            if p.poll() is not None:
                bar.finish()
                break

    def fix_tags(self, index):
        # Fix meta data of a downloaded song
        with open(self.list_file, 'r', encoding='utf-8') as f:
            artist, track, lyrics_page = list(csv.reader(f))[index]
            print('Fixing tags for {} - {}'.format(artist, track))
            '''
            req = self.config['MUSIX_MATCH'] + lyrics_page
            print(req)
            self.run_driver()
            self.driver.get(req)
            s = BeautifulSoup(self.driver.page_source, 'html.parser')
            img = s.find('div', {'class': 'banner-album-image"'})
            urllib.request.urlretrieve(img, '{} - {}.jpg'.format(artist, track))
            '''
            af = eyed3.load('{} - {}.mp3'.format(artist, track))
            af.tag.artist = artist
            af.tag.title = track
            #af.tag.images.set(3, open('cover.jpg', 'rb').read(), 'image/jpeg')
            af.tag.save()
