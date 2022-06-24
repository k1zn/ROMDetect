# with <3 by k1zn

import sys, zipfile 

if len(sys.argv) > 1:
  with zipfile.ZipFile(sys.argv[1:][0]) as zf:
      for file in zf.infolist():
        if file.filename == 'META-INF/com/google/android/update-binary':
          byte_text = zf.read(file)
          if 'blockdev' in byte_text.decode('utf-8'):
            print("[BRICK] DON'T INSTALL THIS! This installer contains \"blockdev\" function, which brick the phone.")
          else:
            print("[CLEAN] ROMDetect.py didn't found \"blockdev\" function in update-binary.")
else:
  print('Usage: ROMDetect.py <filename>')