# Android setup without AndroidStudio

## Get Android SDK Manger CLI
Download SDKManager CLI and move it to `/lib/android-sdk/cmdline-tools/latest/`

Add following lines to .bashrc
```
export ANDROID_HOME=/usr/lib/android-sdk

export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
```
Show installed packages: `./sdkmanager --list_installed`
Show available packages: `./sdkmanager --list`

Typical setup
```
build-tools;29.0.3
build-tools;30.0.3
build-tools;34.0.0
emulator
platform-tools
platforms;android-34
system-images;android-34;google_apis;x86_64
```


## openjdk
Install openjdk-xx with `sudo apt install openjdk-xx`


## Gradle
Download current Gradle (Binary-only) `https://gradle.org/install/`
```
mkdir /opt/gradle
unzip -d /opt/gradle gradle-x.x-bin.zip
```

Add following lines to .bashrc
```
export PATH=/opt/gradle/gradle-x.x/bin:$PATH # must be prepended, else it would use windows gradle
```

## Emulator


## Flutter

Download current Flutter CLI here: https://docs.flutter.dev/release/archive?tab=linux  

Extract files and copy them into lib folder

```
tar xvf flutter_linux_x.xx.x-stable.tar.xz
mv flutter_linux_x.xx.x-stable/* /usr/lib/flutter/
```

Add following lines to .bashrc

```
export FLUTTER_HOME=/usr/lib/flutter
export PATH=$PATH:$FLUTTER_HOME/bin
```

Check with `flutter --version`
