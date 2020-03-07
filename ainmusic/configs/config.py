import pathlib

config = {
    'MUSIX_MATCH': 'https://www.musixmatch.com',
    'HEADERS': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
    },
    'USE_PROXY': False,
    'PROXY': 'https://example.com:1080'
}

ROOT_PATH = pathlib.Path(__file__).parent.parent.absolute()