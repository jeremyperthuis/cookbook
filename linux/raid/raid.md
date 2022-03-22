# Raid
------
## Liste des commandes
* fdisk : outil de base pour réaliser des opérations sur les tables de partitions des disques durs.
* mdadm : gestion des Raid
* mount : monter un volume a un emplacement
* lvm (Logical Volume Manager) : permet la création et la gestion de volumes logiques
*


## Workflow

#### I) Création d'un Raid 1

1. on liste des les volumes  disponible avec `fdisk -l` en root :

  ```
    Disque /dev/sda : 1,37 TiB, 1500301910016 octets, 2930277168 secteurs
    Disk model: ST31500341AS    
    Unités : secteur de 1 × 512 = 512 octets
    Taille de secteur (logique / physique) : 512 octets / 512 octets
    taille d'E/S (minimale / optimale) : 512 octets / 512 octets

    Disque /dev/sdb : 298,9 GiB, 320072933376 octets, 625142448 secteurs
    Disk model: HITACHI HTS72503
    Unités : secteur de 1 × 512 = 512 octets
    Taille de secteur (logique / physique) : 512 octets / 512 octets
    taille d'E/S (minimale / optimale) : 512 octets / 512 octets
    Type d'étiquette de disque : dos
    Identifiant de disque : 0x0002af6c

    Périphérique Amorçage  Début       Fin  Secteurs Taille Id Type
    /dev/sdb1    *        206848 625139711 624932864   298G 83 Linux

  ```
2. On crée le raid avec la commande suivante :

  ```
    mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sda
  ```

  On obtient le nouveau volume :
  ```
    Disque /dev/md0 : 297,89 GiB, 319830360064 octets, 624668672 secteurs
    Unités : secteur de 1 × 512 = 512 octets
    Taille de secteur (logique / physique) : 512 octets / 512 octets
    taille d'E/S (minimale / optimale) : 512 octets / 512 octets
  ```

  Plus de détails  concernant le raid avec la commande `mdadm --detail /dev/md0` :
  ```
    /dev/md0:
           Version : 1.2
     Creation Time : Sun Jan 30 15:33:46 2022
        Raid Level : raid1
        Array Size : 312334336 (297.87 GiB 319.83 GB)
     Used Dev Size : 312334336 (297.87 GiB 319.83 GB)
      Raid Devices : 2
     Total Devices : 2
       Persistence : Superblock is persistent

     Intent Bitmap : Internal

       Update Time : Sun Jan 30 16:43:42 2022
             State : clean
    Active Devices : 2
   Working Devices : 2
    Failed Devices : 0
     Spare Devices : 0

  Consistency Policy : bitmap

              Name : desktop:0  (local to host desktop)
              UUID : 1e2431f0:0cd067bb:2e9401fd:9de8b623
            Events : 851

    Number   Major   Minor   RaidDevice State
       0       8       17        0      active sync   /dev/sdb1
       1       8        0        1      active sync   /dev/sda
  ```
3. Formatage et montage du nouveau volume raid :
  ```
    mkfs.ext4 /dev/md0
  ```

  ```
    mount /dev/md0 /home/user/dir
  ```

4. Ajouter cette ligne dans `/etc/fstab` pour un montage auto au démarage :

  ```
    /dev/md0 	/media/raid	ext4	defaults 	0	1
  ```
