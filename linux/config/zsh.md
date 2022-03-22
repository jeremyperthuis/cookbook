# ZSH
  ------
  ## I) Installation

  Host filesystem must be ext4.

  1. Install zsh
    ```
      apt install zsh
    ```

  2. Install oh-my-zsh
    ```
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```

  3. Install Powerline
    ```
      sudo apt-get install fonts-powerline
    ```

  4. Install plugin : zsh-interactive-cd

    install fzf first :
    ```
      git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
      ~/.fzf/install
    ```
  5. Change theme to `agnoster` by replacing ZSH_THEME variable in `~/.zshrc` file
