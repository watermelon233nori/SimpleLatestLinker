# LatestLinker

I will develop this app through C# one day. Now I just use this python file to set my soft link. (noted on 2023-04-30)

A useless shit.

This can generate a soft link to the folder for the latest version of a program. It doesn't require any third-party library. I have tested it on Windows.

In such a file structure like this: 

```textile
D:\Portable Programs\FFmpeg\
├─ffmpeg-4.4-full_build
│  ├─bin
│  │  └─fonts
│  ├─doc
│  └─presets
├─ffmpeg-5.0-full_build
│  ├─bin
│  │  └─fonts
│  ├─doc
│  └─presets
└─ffmpeg-5.1.1-full_build
   ├─bin
   │  └─fonts
   ├─doc
   └─presets
```

Save this script on primary directory, and run the script.

The script will traverse the primary directory and list them like this:

```textile
Select a directory to link:
--------------
1: ffmpeg-4.4-full_build
2: ffmpeg-5.0-full_build
3: ffmpeg-5.1.1-full_build
--------------
Input the number:
```

Just input the number! The script will generate a soft link which can direct to the directory corresponding to the number you input.

I often use it on command-line tools, so I can change the GUI program's configuration (e.g. *path to ffmpeg and ffprobe binaries (executable)* is <code>D:\Portable Programs\FFmpeg\latest\<code>). If these command-line tools update, I just need decompress the package to the FFmpeg version directory and run the script so that I don't need to change the configuration.

I will add decompress function in half a year if I remember.
