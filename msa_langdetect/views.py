import typing as t
from collections import OrderedDict

from langdetect import detect, detect_langs
from langdetect.language import Language

# from guess_language import guess_language

from msa_langdetect import jsonrpc


@jsonrpc.method('google.detect(String) -> Array')
def _detect(text):
    return detect(text)


@jsonrpc.method('google.detect_langs(String) -> Object')
def _detect_langs(text):
    guess: t.List[Language] = detect_langs(text)
    return OrderedDict((l.lang, l.prob) for l in guess)


# @jsonrpc.method('guess_language.detect_lang(String) -> String')
# def _detect_lang(text):
#     return guess_language(text)
