# ROMDetect
Detect Edify-installers (TWRP/Magisk-installers) that can brick your phone.

> This repository is open for pull-requests. Help world community to stay safe with custom ROMs. <3

## Installation guide
For **Termux**:
```shell script
pkg up
pkg install python
pkg install git
git clone https://github.com/k1zn/ROMDetect.git
cd ROMDetect
```

For **PC**:
1) [Download](https://github.com/k1zn/ROMDetect/archive/refs/heads/main.zip) this repository

## Usage
For **Termux**:
1) Give Termux permission for files in app settings
2) 
```bash
$ python ROMDetect.py <filename>
```

Example: 
```bash
$ python ROMDetect.py /sdcard/Download/someshit.zip
```

For **PC**:
```bash
ROMDetect.py <filename>
```

Example:
```bash
ROMDetect.py someshit.zip
```
