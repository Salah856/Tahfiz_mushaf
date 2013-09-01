Tahfiz_mushaf
=============
a quick script to convert [Mushaf AlMadinah](http://www.islamhouse.com/d/files/ar/ih_books/chain/Mushaf_AlMadinah/ar_Mushaf_AlMadinah_N_B.pdf "Mushaf AlMadinah") to a notebook for Hifz.

the script is not written to be generic with any mushaf, but to accomplish a one-off task. so there is no warranties for using that script.

sample:
![input output demonstration](https://raw.github.com/myaser/Tahfiz_mushaf/master/data/sample.jpg "sample page")

How it works
============
- loop on the pdf file extracting the image representing every page
- paste a 15-line page template on each mushaf page
- detect locations of `ayat separator`(s)
- paste a no-text version of `ayat separator` on the page
- detect locations of `soura separator`(s)
- paste a no-text version of `soura separator` on the page
- output each page as an image to output directory
- use imagemagic to collect processed images in one pdf file

Todo
====
- the script outputs collected pdf file instead of writing images to desk

usage
=====
- python converter.py path/to/the/pdf/file
- cd data/output
- convert *.jpg hefz.pdf

download
========
- [output_hefz_v1.0.pdf](https://dl.dropboxusercontent.com/s/a2q12qmz3k8nxht/output_hefz_v1.0.pdf?token_hash=AAH3p8UCwmO1hsguPI080eCPteoDQkuTbAySg9EmGuaWeQ&dl=1 "v1.0 pdf file")
