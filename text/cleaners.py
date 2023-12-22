import re
from unidecode import unidecode
from text.korean import latin_to_hangul, divide_hangul, fix_g2pk2_error
from g2pk2 import G2p


def korean_cleaners(text):
    text = latin_to_hangul(text)
    g2p = G2p()
    text = g2p(text)
    text = divide_hangul(text)
    text = fix_g2pk2_error(text)
    text = re.sub(r'([\u3131-\u3163])$', r'\1.', text)
    return text
