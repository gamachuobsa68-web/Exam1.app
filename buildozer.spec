[app]
title = Oro Exam System
package.name = oroexam
package.domain = org.oro

source.dir = .
source.include_exts = py,kv,png,jpg,ttf

version = 1.0

requirements = python3,kivy==2.2.1,cython,requests,pillow,reportlab

orientation = portrait

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET
