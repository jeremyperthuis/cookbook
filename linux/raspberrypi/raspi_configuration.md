# Raspberry Pi Configuration
  ------

  ## Description
  All files erased caused by bad manipulation - impossible to recover files

  This tutorial is based on [Google](https://google.fr)
  ## Part

  #### I) Installation

  1. Download Raspberry pi OS lite image and unzip it
    ```
      wget https://raspberry-pi.fr/download/raspbian_lite_latest.zip

      unzip path/to/image.zip
    ```

  2. Find apropiate device with `lsblk` command:
    ```
    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0         7:0    0  61,9M  1 loop /snap/core20/1328
loop2         7:2    0  61,9M  1 loop /snap/core20/1270
loop3         7:3    0   199M  1 loop /snap/rpi-imager/221
loop4         7:4    0  55,5M  1 loop /snap/core18/2284
loop5         7:5    0   219M  1 loop /snap/gnome-3-34-1804/77
loop6         7:6    0   219M  1 loop /snap/gnome-3-34-1804/72
loop8         7:8    0  55,5M  1 loop /snap/core18/2253
loop9         7:9    0 196,5M  1 loop /snap/rpi-imager/184
loop10        7:10   0 110,8M  1 loop /snap/core/12725
sda           8:0    0 223,6G  0 disk
├─sda1        8:1    0    28G  0 part /
├─sda2        8:2    0     1K  0 part
├─sda5        8:5    0   7,7G  0 part [SWAP]
└─sda6        8:6    0   188G  0 part /home
mmcblk0     179:0    0  14,9G  0 disk
├─mmcblk0p1 179:1    0   256M  0 part /media/perthuis/boot
└─mmcblk0p2 179:2    0  14,6G  0 part /media/perthuis/rootfs

    ```
    SD card device is `mmcblk0`.

  3. Copy image to sd card with dd command:
    ```
    sudo dd bs=1M if=chemin_vers_le_img_de_raspbian of=/dev/votre_carte status=progress conv=fsync
    ```

  4. Enable ssh by creating new empty `ssh` file in `boot` folder:
  ```
    touch ssh
  ```

  5. Configure wifi by creating new `wpa_supplicant.conf` file in `boot` folder, and fill it with configuration below (works with Rasbian Jessie):
  ```
  country=FR # or 2 letters country alpha code
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1

  network={
    ssid="ssid"
    psk="*******"
    key_mgmt=WPA-PSK    
  }
  ```

  6. Now you can plug your sd in the raspberry. turn it on, wait until login prompt appear, then shut if down. Then, turn it on again. (This must be done 2 times for wifi configuration purposes).

  7. Install Omxplayer
  ```
  sudo apt update
  sudo apt upgrade
  sudo apt install omxplayer
  ```
