# irsl_universal_robot

## Build Docker

```
(cd docker; ./build.sh)
```

## Run Docker

```
./run.sh jupyter
```

```
./run.sh choreonoid-console
```

```
./run.sh
```

## Compiling real-time kernel on Ubuntu

### https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/real_time.md
- Setting GRUB
- Disable CPU speed scaling

### https://frankaemika.github.io/docs/installation_linux.html

- Using .config on ubuntu
- Download kernel/config on ubuntu from http://kernel.ubuntu.com/~kernel-ppa/config/
- ref: https://gihyo.jp/admin/serial/01/ubuntu-recipe/0526

### https://hiiragi-works.sakura.ne.jp/linux-004/

- Required .deb (merged from 3 sites)
```
sudo apt install bc bison build-essential ca-certificates curl dwarves flex gawk gnupg2 kernel-package libelf-dev liblz4-tool libncurses-dev libssl-dev lsb-release wget zstd
```

- Error related to pem file
```
[.config]
#修正前
CONFIG_SYSTEM_TRUSTED_KEYS="debian/canonical-certs.pem"
CONFIG_SYSTEM_REVOCATION_KEYS="debian/canonical-revoked-certs.pem"
↓
#修正後
CONFIG_SYSTEM_TRUSTED_KEYS=""
CONFIG_SYSTEM_REVOCATION_KEYS=""
```

- Error related to BTF
```
[.config]
#修正前
CONFIG_DEBUG_INFO_BTF=y
CONFIG_DEBUG_INFO_BTF_MODULES=y
↓
#修正後
CONFIG_DEBUG_INFO_BTF=n
CONFIG_DEBUG_INFO_BTF_MODULES=n
```
