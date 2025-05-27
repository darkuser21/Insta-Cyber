# 🕵️‍♂️ Insta-Cyber: Instagram OSINT Tool

![Insta-Cyber Banner](https://img.shields.io/badge/python-3.8%2B-blue.svg) ![OSINT Tool](https://img.shields.io/badge/type-OSINT-informational.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 About

**Insta-Cyber** is a hacker-vibe themed Instagram OSINT (Open-Source Intelligence) tool built in Python.  
It allows you to extract public profile information and optionally download the list of followers and following from Instagram accounts.

Built for ethical hacking, educational demos, and digital forensics.

---

## 🧰 Features

- 🎯 Fetch public Instagram profile data:
  - Username, full name, user ID
  - Bio, external URL
  - Follower/following count
  - Post count, profile picture URL
  - Private/verified status
- 📥 Download followers list to `followers.txt`
- 📥 Download following list to `following.txt`
- 🎨 Stylish hacker-themed terminal interface with colorized output
- 🔐 Optional login support for accessing private profiles you follow

---

## 📸 Demo

> Terminal Preview:
##################################################

- ██████ ██ ██ ████████ ██████
- ██ ██ ██ ██ ██ ██ ██
- ██ ██ ██ ██ ██ ██ ██
- ██ ▄▄ ██ ██ ██ ██ ██ ██
- ██████ ██████ ██ ██████
- ▀▀
[ I N S T A - C Y B E R O S I N T ]
##################################################

[?] Enter Instagram username: cyber_user

--- Instagram OSINT Info ---
- [+] Username : cyber_user
- [+] Full Name : John Cyber
- [+] Followers : 1024
- [+] Following : 220
- ...
---

## 🛠️ Setup

### Requirements

- Python 3.8+
- `instaloader`
- `colorama`

### Installation

```bash
git clone https://github.com/darkuser21/Insta-Cyber.git
cd Insta-Cyber
pip install -r requirements.txt
python insta_cyber.py
```

 # Optional #
## You’ll  be prompted to enter the Instagram username. Choose what data to fetch (followers, following, or both).
## If you want to access private profiles you follow, uncomment the login line in the script and use: ## 

```

loader.login('your_username', 'your_password')
```

