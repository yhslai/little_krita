# Little Krita

A collection of small convenience actions for Krita, including tracing-paper creation/removal, merging down unnamed layers, brush flipping and resizing, and toggling sibling-layer visibility.

## Install

1. Download the plugin `.zip` file.
2. In Krita, open **Tools → Scripts → Import Python Plugin From File** and select the downloaded `.zip` file.
3. Restart Krita.

The actions are available under **Tools → Little Krita → Scripts**. Assign keyboard shortcuts through **Settings → Configure Krita → Configure Shortcuts** if desired.

## Development install (Windows)

Keep this repository anywhere, then link its two plugin items into `%APPDATA%\krita\pykrita\`. Windows requires Developer Mode or an elevated terminal to create symbolic links:

```powershell
$repo = 'C:\path\to\little_krita'
$pykrita = "$env:APPDATA\krita\pykrita"

New-Item -ItemType SymbolicLink -Path "$pykrita\little_krita" -Target "$repo\little_krita"
New-Item -ItemType SymbolicLink -Path "$pykrita\little_krita.desktop" -Target "$repo\little_krita.desktop"
```

Remove any existing `little_krita` folder and `little_krita.desktop` file in the destination before creating the links.
