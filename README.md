# tg-fetcher
This tool uses the telegram API to automatically fetch and translate messages from groups and channels. API is not required for translation. It can be useful for tracking foreign APT groups.


# Installation
## Requirements
You will need a telegram user API. Define this API in **config.py**. https://core.telegram.org/api
then:

    pip3 install -r requirements.txt


# Usage

## What you need to know:

The DEST_LANGUAGE argument is set to "tr" by default. So translations will be in Turkish by default. 

You can give channel or group username to the -c parameter. 

If you use the -d option, you must give it the file ID as an argument. 


    usage: tg-fetcher.py [-h] -c CHANNEL [-m MESSAGES_LIMIT] [-l DEST_LANGUAGE] [-p] [-n] [-d DOWNLOAD_MEDIA]

    This tool uses the telegram API to automatically fetch and translate messages from groups and channels. API is not required for translation. It can be useful for tracking foreign APT groups.
    
    options:
      -h, --help            show this help message and exit
      -c CHANNEL, --channel CHANNEL
                            Telegram Channel Username
      -m MESSAGES_LIMIT, --messages-limit MESSAGES_LIMIT
                            Messages Limit
      -l DEST_LANGUAGE, --dest-language DEST_LANGUAGE
                            Messages Language
      -p, --print           Printable output (for copy)
      -n, --no-translate    No Translate
      -d DOWNLOAD_MEDIA, --download-media DOWNLOAD_MEDIA
                            Download Media with ID

if you want to automatically scan several channels/groups, take a look at the fetch-all.sh script.

