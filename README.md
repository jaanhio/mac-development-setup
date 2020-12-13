# Mac Development Ansible Setup (WIP)

This contains ansible code for setting up a Mac with various development related packages/apps for development work.
* homebrew apps/packages setup (completed)
* dotfile setup (WIP)
* mac configuration setup (WIP)
---
## Pre-setup steps
These steps have to be executed manually in order to get ansible onto local machine.

### 1. Install Apple CLI tools. Open `terminal` and run `xcode-select --install`.
```
xcode-select --install
```
### 2. [Set up SSH key](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for github access.
### 3. Clone repo to local machine.

### 4. [Install Homebrew](https://brew.sh/).
Due to high possibility of running into permission issues when installing packages via homebrew, be sure to make sure the relevant permissions to folders have been given. This can be checked via `brew doctor`.

### 5. Install latest version of `python` (python3) and `pip` (pip3) by running `brew install python`.
```
brew install python
```
Read [this](https://opensource.com/article/19/5/python-3-default-mac) for additional info on setting up python.
### 6. Update pip to latest version.
```
pip3 install --user --upgrade pip
```
OR
```
python3 -m pip install --user --upgrade pip
```
### 7. Install Ansible using `pip`.
```
python3 -m pip install --user ansible

```
Python installer installs modules at `/Users/<user>/Library/Python/<version number>/bin`.
Add to `PATH.`
```
export PATH=/Users/<user>/Library/Python/<version number>/bin:$PATH
```
---

## Setup
### Run playbook inside this directory.
```
ansible-playbook main.yml -i inventory --ask-become-pass
```
