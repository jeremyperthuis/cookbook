# How to recove data from RAID system with CLI tools

In this article, we'll see a not so well documented procedure based on my personnal experience : recovering data from  a RAID system with only CLI tools.

The scenario is the following : I own a Synology NAS to store all my data, i dont have any backup nor trashbin system to recover accidentally erased data.

Requirements :
- A computer with ubuntu installed on a ext4 partition
- the connection needed to connect all the discs


## Step 1 : Reconstruct RAID on your computer.

1. Get root privilege

  From this point, you must perform all your action with root privilege.
  After opening your terminal, type :

  ```
  sudo -i
  ```
2. Install mdadm

  mdadm is a powerful tool to build and manage RAID devices (md devices), you must install it with lvm2, wich allow to manage logical volume

  ```

  ``
