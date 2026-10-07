from pathlib import Path


folder = Path("Download")

folder_doc = folder / "Documents"
folder_images = folder / "Images"
folder_videos = folder / "Videos"
folder_audio = folder / "Audio"

folder_doc.mkdir(exist_ok=True)
folder_images.mkdir(exist_ok=True)
folder_videos.mkdir(exist_ok=True)
folder_audio.mkdir(exist_ok=True)


for item in folder.iterdir():

    if not item.is_file():
        continue

    if item.suffix in [".txt", ".pdf"]:
        item.rename(folder_doc / item.name)

    elif item.suffix in [".png", ".jpg"]:
        item.rename(folder_images / item.name)

    elif item.suffix == ".mp3":
        item.rename(folder_audio / item.name)

    elif item.suffix == ".mp4":
        item.rename(folder_videos / item.name)
            

