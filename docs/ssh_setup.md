# Git SSH Setup

This guide configures SSH authentication for pushing code to GitHub using Git.

---

## Initally

* Git installed (`git --version`)

---

## Check Existing SSH Keys

```bash
ls ~/.ssh
```

Look for:

* `id_ed25519`
* `id_ed25519.pub`

If they exist, you may reuse them. Otherwise, create a new key.

---

## Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

* Press **Enter** to accept default path
* Optionally set a passphrase (recommended for security)

---

## Start SSH Agent and Add Key

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

## Copy Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output.

---

## Add SSH Key to GitHub

1. Go to: https://github.com/settings/keys
2. Click **New SSH Key**
3. Paste your key
4. Save

---

## Test SSH Connection

```bash
ssh -T git@github.com
```

Expected output:

```bash
Hi <your-username>! You've successfully authenticated...
```

---