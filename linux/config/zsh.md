# ZSH



  ## 1) ZSH Installation

  Host filesystem must be ext4.

  1.Install zsh

    ```
      apt install zsh
    ```

  2. Install oh-my-zsh

    ```
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```

3. Install plugin : zsh-interactive-cd

   install fzf first :
   ```
     git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
     ~/.fzf/install
   ```



## 2) Theme Installation

### Linux

1. Install Powerline

    ```
      sudo apt-get install fonts-powerline
    ```

2. Change theme to `agnoster` by replacing ZSH_THEME variable in `~/.zshrc` file

### WSL 2

1. Open Powershell then type :

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy Unrestricted
   mkdir c:/fonts
   cd C:\fonts\
   git clone https://github.com/powerline/fonts.git
   cd .\fonts-master\
   .\install.ps1
   ```

​		Then pick `DejaVu Sans Mono for Powerline` as your font.



2. Add this scheme in your wsl `settings.json`:

   ````
   "schemes": [
           {
               "background" : "#002B36",
               "black" : "#002B36",
               "blue" : "#268BD2",
               "brightBlack" : "#657B83",
               "brightBlue" : "#839496",
               "brightCyan" : "#D33682",
               "brightGreen" : "#B58900",
               "brightPurple" : "#EEE8D5",
               "brightRed" : "#CB4B16",
               "brightWhite" : "#FDF6E3",
               "brightYellow" : "#586E75",
               "cyan" : "#2AA198",
               "foreground" : "#93A1A1",
               "green" : "#859900",
               "name" : "wsl",
               "purple" : "#6C71C4",
               "red" : "#DC322F",
               "white" : "#93A1A1",
               "yellow" : "#B58900"
           }
       ],
   ````

   then pick `wsl` as your color scheme

   

3. Change theme to `agnoster` by replacing ZSH_THEME variable in `~/.zshrc` file
