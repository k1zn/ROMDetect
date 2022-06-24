# with <3 by k1zn

import sys, zipfile 

check_files = ['META-INF/com/google/android/update-binary', 'META-INF/com/google/android/updater-script']
is_brick = False

if len(sys.argv) > 1:
  with zipfile.ZipFile(sys.argv[1:][0]) as zf:
      for file in zf.infolist():
        if file.filename in check_files:
          byte_text = zf.read(file)
          if 'blockdev' in byte_text.decode('utf-8') and not is_brick:
            is_brick = True
  if is_brick:
    print("[BRICK] DON'T INSTALL THIS! This installer contains \"blockdev\" function, which brick the phone.")
  else:
    print("[CLEAN] ROMDetect.py didn't found \"blockdev\" function in update scripts.")
else:
  print('Usage: ROMDetect.py <filename>')