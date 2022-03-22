# Debian Installation Guide
  ------

  ## I) Procedure

  1. Get latest Debian Image
	Latest Debian image with Gnome desktop env can be download [here](https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/)
	-> debian-live-11.2.0-amd64-gnome.iso
  2. Create a bootable usb drive with Rufus tool (Windows only)

  3. Performs installation
	- At drive partition step, create 3 partition ( /, home and swap)
	- Debian doesnt include non-free firmware like intel wifi driver (install it later)

  4. Post installation things to do
	- Add user in sudoers file
    ```
    	su root
    	sudo nano /etc/sudoers
    ```
    then add `<user>	ALL=(ALL:ALL) ALL` in file

	- Install non free wifi firmware (example for Bullseye 11.2 with intel for x1 carbon)
		- Go to `https://cdimage.debian.org/cdimage/unofficial/non-free/firmware/bullseye/11.2.0/`, then download `firmware.tar.gz`.
		- Dezip archive then find appropriate firmware (`firmware-iwlwifi_20210818-1_all.deb` in our case), then :
  		```
  		  sudo dpkg -i firmware-iwlwifi_20210818-1_all.deb
  		```
	- Add non-free repo in `/etc/apt/sources.list` ->  should looks like this :

    ```
      deb http://deb.debian.org/debian bullseye main contrib non-free
      deb-src http://deb.debian.org/debian bullseye main contrib non-free

      deb http://deb.debian.org/debian-security/ bullseye-security main contrib non-free
      deb-src http://deb.debian.org/debian-security/ bullseye-security main contrib non-free

      deb http://deb.debian.org/debian bullseye-updates main contrib non-free
      deb-src http://deb.debian.org/debian bullseye-updates main contrib non-free
		```
