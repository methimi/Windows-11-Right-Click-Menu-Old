# Windows 11 Classic Context Menu

Restore the classic **Windows 10-style right-click context menu** on Windows 11 with a single click.

This is a lightweight, open-source utility written in Python that safely enables or restores the Windows 11 context menu by modifying only the current user's registry settings.

---

## ✨ Features

* ✅ Enable the classic Windows 10 context menu
* ✅ Restore the default Windows 11 context menu
* ✅ One-click operation
* ✅ No installation required
* ✅ No administrator privileges required
* ✅ Safe and reversible
* ✅ Open source
* ✅ Standalone EXE available

---

## 📸 Screenshots

> Add screenshots here.

```
screenshots/
├── before.png
└── after.png
```

---

## 📥 Download

Download the latest executable from the **Releases** section.

Run:

```
ClassicContextMenu.exe
```

No installation is required.

---

## 🛠 How It Works

The application creates or removes the following registry key:

```
HKEY_CURRENT_USER
└── Software
    └── Classes
        └── CLSID
            └── {86ca1aa0-34aa-4e8b-a509-50c905bae2a2}
                └── InprocServer32
```

After applying the change, Windows Explorer is automatically restarted so the new context menu takes effect immediately.

Only the **current user's** registry is modified.

No system files are changed.

---

## 💻 Building from Source

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/windows11-classic-context-menu.git
cd windows11-classic-context-menu
```

Run with Python:

```bash
python main.py
```

Build the executable:

```bash
pip install pyinstaller
pyinstaller --onefile --uac-admin main.py
```

The compiled executable will be located in:

```
dist/
```

---

## 🔒 Safety

This application:

* Does not collect any data
* Does not connect to the Internet
* Does not modify Windows system files
* Only edits a single registry location under **HKEY_CURRENT_USER**
* Can restore the original Windows 11 context menu at any time

---

## 📋 Compatibility

| Windows Version            | Supported |
| -------------------------- | --------- |
| Windows 11 21H2            | ✅         |
| Windows 11 22H2            | ✅         |
| Windows 11 23H2            | ✅         |
| Windows 11 24H2            | ✅         |
| Future Windows 11 versions | Expected* |

*Microsoft may change this registry behavior in future Windows updates.

---

## 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify and distribute it.

---

## 🤝 Contributing

Contributions, bug reports and feature requests are always welcome.

If you find this project useful, consider giving it a ⭐ on GitHub.

---

## ⚠ Disclaimer

This software is provided **as is**, without warranty of any kind.

Although it only modifies a single user registry key, you use this software at your own risk.

---

Made with ❤️ for the Windows community.
