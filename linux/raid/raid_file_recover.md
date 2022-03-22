# Raid file recover
------

## Issue description
All files erased caused by bad manipulation - impossible to recover files

This tutorial is based on thes 2 documentation from Synology : [Install shr on linux](https://kb.synology.com/fr-fr/DSM/tutorial/How_can_I_recover_data_from_my_DiskStation_using_a_PC) and [recover data](https://kb.synology.com/fr-fr/DSM/tutorial/How_can_I_use_PhotoRec_to_recover_files_accidentally_deleted_from_my_Synology_NAS)


## Workflow

#### I) Set-up Raid on Linux

Host filesystem must be ext4.

1. Install mdadm and lvm2
  ```
    apt-get install -y mdadm lvm2
  ```

2. Assemble all disks from RaidDevice
  ```
    mdadm -Asf && vgchange -ay
  ```

3. Get info with `lvs` :

  ```
    WARNING: PV /dev/md2 in VG vg1 is using an old PV header, modify the VG to update.
    WARNING: PV /dev/md3 in VG vg1 is using an old PV header, modify the VG to update.
    WARNING: PV /dev/md4 in VG vg1 is using an old PV header, modify the VG to update.
    LV                    VG  Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
    syno_vg_reserved_area vg1 -wi-a----- 12,00m                                                    
    volume_1              vg1 -wi-a-----  7,26t
  ```
  So device path is : /dev/vg1/volume1

4. To get rid of the Warnings above, we update volume metadata with following command :
  ```
    vgck --updatemetadata vg1
  ```
5. Then we can mount the volume :

  ```
    mount /dev/vg1/volume_1 /home/user/raid -o ro
  ```

#### II) Recover files with photorec

1. Install photorec (part of testdisk package):

  ```
    apt-get install testdisk
  ```

2. Launch photorec with command `photorec`:
