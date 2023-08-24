def download(api_id, api_hash, file_id):
    from pyrogram import Client

    api_id = api_id
    api_hash = api_hash
    file_id = file_id

    with Client('my_account', api_id, api_hash) as app:
        file_path = app.download_media(file_id)
        print(f"Indirilen dosya: {file_path}")
        exit()
