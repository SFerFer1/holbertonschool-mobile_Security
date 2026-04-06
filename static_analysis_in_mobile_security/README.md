Task0
MainActivityKt.Java
grep -r "xorDeobfuscate" out_task0/
strings out_task0/resources/classes4.dex | grep -E "[0-9a-fA-F]{10,}"