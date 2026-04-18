[app]
title = StreamBox
package.name = streambox
package.domain = org.delal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,urllib3,idna,charset-normalizer,certifi
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/ios-control/ios-deploy
ios.ios_deploy_branch = 1.10.0
