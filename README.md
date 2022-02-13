# small_tracer
Study for tracer primitive

## Build
```
gcc -pg mcount.S main.c
```

## Run
```
$ ./a.out
[1644731649375724078] main[0x5648f8c64347] <= ??[0x7f7a21682565]
[1644731649402600808] bar[0x5648f8c642fc] <= main[0x5648f8c64351]
[1644731649428705236] foo[0x5648f8c642e7] <= bar[0x5648f8c64306]
[1644731649454766866] recursive[0x5648f8c6431a] <= main[0x5648f8c6435b]
[1644731649480964789] recursive[0x5648f8c6431a] <= recursive[0x5648f8c64337]
[1644731649507332189] recursive[0x5648f8c6431a] <= recursive[0x5648f8c64337]
[1644731649533815810] recursive[0x5648f8c6431a] <= recursive[0x5648f8c64337]
[1644731649560091777] recursive[0x5648f8c6431a] <= recursive[0x5648f8c64337]
```
