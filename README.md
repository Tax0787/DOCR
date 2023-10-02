# DOCR
reality Document text OCR drive (usually use programming)

## HOW 2 USE?
use as a fork. It's a template repo 

## Setup

execute this code at repo directory

```
cd img2txt
python tesseract_installer.py
```

### Setup Help (2)

>`cd img2txt`
>
> if you use termux
>> `touch .is_termux` touch will make empthy file
> if you use replit
>> `touch .is_replit` touch will make empthy file
> if you use want init (this repo is setup in replit) (this is bash or sh, if you use batch(cmd), you should use not `rm`, `del`)
>> `rm .tesseract_path.txt`
>>> if you want delete example
>>>> `rm img.txt img.png`
>>> else if you want delete example results
>>>> `rm img.txt`
>>> else if you want delete metadata_file
>>>> `rm test_download.sh test_script.sh guide.txt`
>>> else if you want remake `img.png` (if you use windows, then you must use WSL linux)
>>>> `sh test_download.sh`

### about `test_script.sh`

test script, same working file : `main.py` (repo root dir's main.py)