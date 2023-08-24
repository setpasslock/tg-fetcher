from pyrogram import Client
from googletrans import Translator
import argparse
from pprint import pprint
from download import download
from config import api_id,api_hash

arg_parser = argparse.ArgumentParser(description="This tool uses the telegram API to automatically fetch and translate messages from groups and channels. API is not required for translation. It can be useful for tracking foreign APT groups.")
arg_parser.add_argument("-c", "--channel", required=True, help="Telegram Channel Username")
arg_parser.add_argument("-m", "--messages-limit", required=False, help="Messages Limit")
arg_parser.add_argument("-l", "--dest-language", required=False, help="Messages Language")
arg_parser.add_argument("-p", "--print", action='store_true', required=False, help="Printable output (for copy)")
arg_parser.add_argument("-n", "--no-translate", action='store_true', required=False, help="No Translate")
arg_parser.add_argument("-d", "--download-media", required=False, help="Download Media with ID")

args = vars(arg_parser.parse_args())
channel = args["channel"]
limitnum = args["messages_limit"]
lang = args["dest_language"]
ifprint = args["print"]
notrans = args["no_translate"]
download_id = args["download_media"]

if download_id != None:
    media_id = download_id
    download(api_id=api_id,api_hash=api_hash, file_id=media_id)
else:
    if limitnum == None:
        print("Messages Limit is required")
        exit()
    else:
        limitnum = int(args["messages_limit"])
        pass



if lang:
    lang_dec = lang
else:
    lang_dec = "tr"

if notrans == True:
    #no translate
    with Client("my_account", api_id, api_hash) as app:
        messages = app.get_chat_history(channel, limit=limitnum)

        for message in messages:
            if ifprint == True:
                print("\033[91m------------------------------------------------------------------------------------------------------\033[0m")
                print(f"Date: \033[95m{message.date}\033[0m")
                print(f"From: \033[95m{message.from_user.username if message.from_user else 'N/A'}\033[0m")
            else:
                print("\033[91m------------------------------------------------------------------------------------------------------\033[0m")
                print(f"Date: \033[95m{message.date}\033[0m")
                print(f"From: \033[95m{message.from_user.username if message.from_user else 'N/A'}\033[0m")

                data = {}

            if message.text:
                if ifprint == True:
                    print(f"Message:                 {message.text}")
                else:
                    data["Message"] = message.text
                    pprint(data, indent=4, width=95, depth=None)
            elif message.photo:
                if ifprint == True:
                    photo_caption = message.caption if message.caption else "No caption"

                    print(f"Photo Caption:          {photo_caption}")
                    print(f"Photo File ID:          {message.photo.file_id}")
                else:
                    photo_caption = message.caption if message.caption else "No caption"

                    data["Photo Caption"] = photo_caption
                    data["Photo File ID"] = message.photo.file_id
                    pprint(data, indent=4, width=95, depth=None)
            elif message.video:
                if ifprint == True:
                    video_caption = message.caption if message.caption else "No caption"
                    print(f"Video Caption:          {video_caption}")
                    print(f"Video File ID:          {message.video.file_id}")
                else:
                    video_caption = message.caption if message.caption else "No caption"

                    data["Video Caption"] = video_caption
                    data["Video File ID"] = message.video.file_id
                    pprint(data, indent=4, width=95, depth=None)
            elif message.document:
                if ifprint == True:
                    document_caption = message.caption if message.caption else "No caption"

                    print(f"Document Caption:       {document_caption}\n\n")
                    print(f"Document File ID:       {message.document.file_id}")
                else:
                    document_caption = message.caption if message.caption else "No caption"

                    data["Document Caption"] = document_caption
                    data["Document File ID"] = message.document.file_id
                    data["Document Filename"] = message.document.file_name
                    pprint(data, indent=4, width=95, depth=None)
else:
    translator = Translator()
    with Client("my_account", api_id, api_hash) as app:
        messages = app.get_chat_history(channel, limit=limitnum)

        for message in messages:
            if ifprint == True:
                print("\033[91m------------------------------------------------------------------------------------------------------\033[0m")
                print(f"Date: \033[95m{message.date}\033[0m")
                print(f"From: \033[95m{message.from_user.username if message.from_user else 'N/A'}\033[0m")
            else:
                print("\033[91m------------------------------------------------------------------------------------------------------\033[0m")
                print(f"Date: \033[95m{message.date}\033[0m")
                print(f"From: \033[95m{message.from_user.username if message.from_user else 'N/A'}\033[0m")

                data = {}
            if message.text:
               if ifprint == True:
                   translation = translator.translate(message.text, dest=lang_dec)
                   print(f"Message:                 {translation.text}")
               else:
                   translation = translator.translate(message.text, dest=lang_dec)
                   data["Message"] = translation.text
                   pprint(data, indent=4, width=95, depth=None)
            elif message.photo:
                if ifprint == True:
                    photo_caption = message.caption if message.caption else "No caption"
                    translation_photo_caption = translator.translate(photo_caption, dest=lang_dec)
                    print(f"Photo Caption:          {translation_photo_caption.text}")
                    print(f"Photo File ID:          {message.photo.file_id}")
                else:
                    photo_caption = message.caption if message.caption else "No caption"
                    translation_photo_caption = translator.translate(photo_caption, dest=lang_dec)

                    data["Photo Caption"] = translation_photo_caption.text
                    data["Photo File ID"] = message.photo.file_id
                    pprint(data, indent=4, width=95, depth=None)
            elif message.video:
                if ifprint == True:
                    video_caption = message.caption if message.caption else "No caption"
                    translation_video_caption = translator.translate(video_caption, dest=lang_dec)
                    print(f"Video Caption:          {translation_video_caption.text}")
                    print(f"Video File ID:          {message.video.file_id}")
                else:
                    video_caption = message.caption if message.caption else "No caption"
                    translation_video_caption = translator.translate(video_caption, dest=lang_dec)

                    data["Video Caption"] = translation_video_caption.text
                    data["Video File ID"] = message.video.file_id
                    pprint(data, indent=4, width=95, depth=None)
            elif message.document:
                if ifprint == True:
                    document_caption = message.caption if message.caption else "No caption"
                    translation_document_caption = translator.translate(document_caption, dest=lang_dec)
                    print(f"Document Caption:       {translation_document_caption.text}\n\n")
                    print(f"Document File ID:       {message.document.file_id}")
                else:
                    document_caption = message.caption if message.caption else "No caption"
                    translation_document_caption = translator.translate(document_caption, dest=lang_dec)

                    data["Document Caption"] = translation_document_caption.text
                    data["Document File ID"] = message.document.file_id
                    data["Document Filename"] = message.document.file_name
                    pprint(data, indent=4, width=95, depth=None)
