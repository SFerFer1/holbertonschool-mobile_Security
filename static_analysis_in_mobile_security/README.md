Task0
MainActivityKt.Java
jadx --show-bad-code out_task0/resources/classes4.dex -d out_redebug
grep -r "xorDeobfuscate" out_task0/
strings out_task0/resources/classes4.dex | grep -E "[0-9a-fA-F]{10,}"
grep -A 20 "xorDeobfuscate" out_redebug/sources/com/holberton/task1/MainActivityKt.java