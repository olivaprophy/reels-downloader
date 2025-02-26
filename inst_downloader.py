# -*- coding: utf-8 -*-

pip install instaloader

import json
import instaloader
from itertools import islice

with open("/content/cookies.json", "r") as f:
    cookies = json.load(f)

L = instaloader.Instaloader(download_video_thumbnails=False)
L.download_json = False

for cookie in cookies:
    name = cookie.get("name")
    value = cookie.get("value")
    domain = cookie.get("domain", ".instagram.com")
    path = cookie.get("path", "/")
    if name and value:
        L.context._session.cookies.set(name, value, domain=domain, path=path)


profile_name = "tiaunariley"  # замените на нужное имя профиля
profile = instaloader.Profile.from_username(L.context, profile_name)

reels_generator = profile.get_reels()
reels = list(islice(reels_generator, 41))
if reels:
    for reel in reels:
        print(f"Скачиваем reel: {reel.shortcode}")
        L.download_post(reel, target=f"{profile.username}_reels")
else:
    print("Нет доступных Reels у данного профиля.")
