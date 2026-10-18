[app]
title = Akash AI
package.name = akashai
package.domain = org.subrato
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 1.0

requirements = python3,kivy,flask,requests

orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO,CAMERA,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
