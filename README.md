Algorithm
=========
1- extract pages from PDF file as images
2- for each image:
    21- detect all ayat separators and build a list of its position
    22- paste the empty ayat separator on the layout in positions retrived from 21
    23- detect all soura beginnings and build a list of its position
    24- paste the empty soura beginning on the layout in positions retrived from 23
    25- paste the the layout on the page
3- build a new pdf file with the editted images
