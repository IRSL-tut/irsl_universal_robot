# Build RT linux

## build

- Read memo.txt
- Download linux-x.y.z.tar.xz
- Download patch-x.y.z-rt???.patch.xz

- tar xz linux-x.y.z.tar.xz
- cd linux-x.y.z
- xzcat ../patch-x.y.z-rt???.patch.xz | patch -p1
- cp ../success.config .config
- make oldconfig
- make -j$(nproc) modules
- make -j$(nproc) deb-pkg
