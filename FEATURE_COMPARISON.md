# Linux Desktop Automation MCP Servers — Deep Feature Comparison

> Last updated: 2026-03-28 (all branches)

| Feature | **gnome-ui-mcp** (ours) | **kwin-mcp** | **hyprland-mcp** | **wayland-mcp** | **hyprmcp** |
|---|---|---|---|---|---|
| **Repository** | asattelmaier + mlugo-apx | isac322/kwin-mcp | alderban107/hyprland-mcp | someaka/wayland-mcp | stefanoamorelli/hyprmcp |
| **Target** | GNOME Wayland (Mutter) | KDE Plasma 6 (KWin) | Hyprland | Any Wayland | Hyprland |
| **Total tools** | **79** | 29 | 27 | 9 | 13 |
| **Input method** | Mutter RemoteDesktop D-Bus | KWin EIS/libei | hyprctl + ydotool + wtype | evemu (raw kernel) | hyprctl only |
| | | | | | |
| **MOUSE INPUT** | | | | | |
| Click (single) | ✅ | ✅ | ✅ | ✅ | ❌ |
| Click (double/triple) | ✅ | ✅ | ⚡ double only | ❌ | ❌ |
| Move/hover | ✅ mouse_move + hover_element | ✅ | ✅ | ✅ | ❌ |
| Drag | ✅ | ✅ (waypoints) | ✅ | ✅ | ❌ |
| Scroll | ✅ | ✅ (horiz + smooth) | ✅ | ✅ | ❌ |
| Button hold (down/up) | ✅ | ✅ | ❌ | ❌ | ❌ |
| | | | | | |
| **KEYBOARD INPUT** | | | | | |
| Type text | ✅ | ✅ | ✅ | ✅ | ❌ |
| Press key | ✅ | ✅ | ✅ | ✅ | ❌ |
| Key combos | ✅ key_combo | ✅ | ✅ send_shortcut | ✅ | ❌ |
| Key hold (down/up) | ✅ | ✅ | ❌ | ❌ | ❌ |
| Unicode/CJK/emoji | ✅ type_unicode | ✅ keyboard_type_unicode | ⚡ wtype partial | ❌ | ❌ |
| | | | | | |
| **TOUCH INPUT** | | | | | |
| Tap | ✅ | ✅ | ❌ | ❌ | ❌ |
| Swipe | ✅ | ✅ | ❌ | ❌ | ❌ |
| Pinch | ✅ | ✅ | ❌ | ❌ | ❌ |
| Multi-finger | ✅ | ✅ | ❌ | ❌ | ❌ |
| | | | | | |
| **ACCESSIBILITY (AT-SPI)** | | | | | |
| AT-SPI tree | ✅ | ✅ | ❌ | ❌ | ❌ |
| Find elements (name/role) | ✅ | ✅ (+ state filter) | ❌ | ❌ | ❌ |
| Element at point | ✅ | ❌ | ❌ | ❌ | ❌ |
| Wait for element | ✅ | ✅ | ❌ | ❌ | ❌ |
| Wait for element gone | ✅ | ❌ | ❌ | ❌ | ❌ |
| Popup detection | ✅ | ❌ | ❌ | ❌ | ❌ |
| Shell settle verification | ✅ | ❌ | ❌ | ❌ | ❌ |
| Effect verification | ✅ | ❌ | ❌ | ❌ | ❌ |
| Element recovery/relocate | ✅ | ❌ | ❌ | ❌ | ❌ |
| Activate element (multi-strategy) | ✅ | ❌ | ❌ | ❌ | ❌ |
| Focus element | ✅ | ❌ | ❌ | ❌ | ❌ |
| Set element text | ✅ | ❌ | ❌ | ❌ | ❌ |
| Select element text | ✅ | ❌ | ❌ | ❌ | ❌ |
| | | | | | |
| **SCREENSHOTS & RECORDING** | | | | | |
| Full screen | ✅ D-Bus + JPEG/resize/HiDPI | ✅ KWin ScreenShot2 | ✅ grim | ✅ multi-backend | ❌ |
| Region/area | ✅ | ❌ | ✅ | ⚡ | ❌ |
| Window | ✅ | ❌ | ✅ | ❌ | ❌ |
| Burst after action | ✅ | ✅ screenshot_after_ms | ❌ | ❌ | ❌ |
| Screen recording / GIF | ✅ Shell.Screencast + ffmpeg | ❌ | ❌ | ❌ | ❌ |
| | | | | | |
| **OCR & VISION** | | | | | |
| OCR text extraction | ✅ Tesseract + dark-theme | ❌ | ✅ Tesseract + dark-theme | ❌ | ❌ |
| OCR click-by-text | ✅ click_text_ocr | ❌ | ✅ click_text | ❌ | ❌ |
| OCR type-into by label | ✅ type_into (AT-SPI + OCR hybrid) | ❌ | ✅ type_into (OCR only) | ❌ | ❌ |
| VLM/AI vision analysis | ✅ OpenRouter + Anthropic + Ollama | ❌ | ❌ | ✅ OpenRouter VLM | ❌ |
| | | | | | |
| **CLIPBOARD** | | | | | |
| Read | ✅ wl-paste | ✅ wl-paste | ✅ wl-paste | ❌ | ❌ |
| Write | ✅ wl-copy | ✅ wl-copy | ✅ wl-copy | ❌ | ❌ |
| | | | | | |
| **WINDOW MANAGEMENT** | | | | | |
| List windows | ✅ AT-SPI | ✅ AT-SPI | ✅ hyprctl | ❌ | ✅ hyprctl |
| Focus window | ✅ | ✅ | ✅ | ❌ | ⚡ dispatch |
| Close window | ✅ Alt+F4 | ❌ | ✅ | ❌ | ❌ |
| Move/resize window | ✅ keyboard move/resize mode | ❌ | ✅ pixel-precise | ❌ | ⚡ dispatch |
| Toggle fullscreen/float | ✅ F11 / Alt+F10 / Super+h | ❌ | ✅ | ❌ | ⚡ dispatch |
| | | | | | |
| **WORKSPACE & MONITOR** | | | | | |
| List workspaces | ✅ Shell.Introspect | ❌ | ✅ | ❌ | ✅ |
| Switch workspace | ✅ key combos | ❌ | ✅ | ❌ | ⚡ dispatch |
| Move window to workspace | ✅ key combos | ❌ | ✅ | ❌ | ⚡ dispatch |
| Toggle overview | ✅ | ❌ | ❌ | ❌ | ❌ |
| Monitor/display info | ✅ Mutter.DisplayConfig | ❌ | ✅ hyprctl | ❌ | ✅ hyprctl |
| | | | | | |
| **APP MANAGEMENT** | | | | | |
| Launch app | ✅ + list_desktop_apps | ✅ | ✅ | ❌ | ❌ |
| App log capture | ✅ | ✅ | ❌ | ❌ | ❌ |
| List running apps | ✅ AT-SPI | ❌ | ❌ | ❌ | ❌ |
| List .desktop entries | ✅ | ❌ | ❌ | ❌ | ❌ |
| | | | | | |
| **SYSTEM INTEGRATION** | | | | | |
| Desktop notifications | ✅ monitor start/read/stop | ❌ | ❌ | ❌ | ❌ |
| D-Bus generic call | ✅ | ✅ | ❌ | ❌ | ❌ |
| GSettings read/write | ✅ get/set/list/reset | ❌ | ❌ | ❌ | ⚡ set_keyword |
| Pixel color sampling | ✅ pixel + region | ❌ | ❌ | ❌ | ❌ |
| Visual diff | ✅ scipy regions | ❌ | ❌ | ❌ | ❌ |
| Wayland protocol info | ✅ | ✅ | ❌ | ❌ | ❌ |
| | | | | | |
| **ARCHITECTURE** | | | | | |
| Session isolation | ✅ gnome-shell --headless | ✅ kwin_wayland --virtual | ❌ | ❌ | ❌ |
| Coordinate / HiDPI handling | ✅ scale metadata + pixel↔logical | ❌ | ✅ formula per screenshot | ❌ | ❌ |
| Screenshot format / resize | ✅ JPEG + max_width + scale_to_logical | ❌ | ✅ JPEG + scale | ❌ | ❌ |
| Action chaining | N/A (by design) | ❌ | ❌ | ✅ chain: syntax | ❌ |
| Per-window shortcuts | N/A (Wayland limitation) | ❌ | ✅ send_shortcut(target=) | ❌ | ❌ |

---

## Feature Count Summary

| Category | gnome-ui-mcp | kwin-mcp | hyprland-mcp | wayland-mcp | hyprmcp |
|----------|:---:|:---:|:---:|:---:|:---:|
| Mouse input | 6/6 | 6/6 | 4/6 | 4/6 | 0/6 |
| Keyboard input | 5/5 | 5/5 | 3/5 | 3/5 | 0/5 |
| Touch input | 4/4 | 4/4 | 0/4 | 0/4 | 0/4 |
| Accessibility | 12/12 | 3/12 | 0/12 | 0/12 | 0/12 |
| Screenshots | 5/5 | 2/5 | 3/5 | 2/5 | 0/5 |
| OCR/Vision | **4/4** | 0/4 | 3/4 | 1/4 | 0/4 |
| Clipboard | 2/2 | 2/2 | 2/2 | 0/2 | 0/2 |
| Window mgmt | **5/5** | 2/5 | 5/5 | 0/5 | 2/5 |
| Workspace/Monitor | 5/5 | 0/5 | 4/5 | 0/5 | 3/5 |
| App mgmt | 4/4 | 2/4 | 1/4 | 0/4 | 0/4 |
| System integration | 6/6 | 2/6 | 0/6 | 0/6 | 1/6 |
| **TOTAL** | **58/58 (100%)** | **28/58 (48%)** | **25/58 (43%)** | **10/58 (17%)** | **6/58 (10%)** |

---

## Unique Strengths

| Project | What only it has |
|---------|-----------------|
| **gnome-ui-mcp** | Deepest AT-SPI (12 tools), effect verification, element recovery, popup detection, AT-SPI+OCR hybrid type-into, notification monitoring, screen recording, GSettings, pixel color, visual diff, GNOME overview toggle, session isolation via gnome-shell --headless, HiDPI coordinate handling, multi-provider VLM (OpenRouter + Anthropic + Ollama). Most tools (79). Only project at 100% feature coverage. |
| **kwin-mcp** | Mature session isolation with home directory sandboxing. EIS/libei input. Waypoint drag. screenshot_after_ms built into every action. |
| **hyprland-mcp** | OCR auto-scope to active window. Pixel-precise window move/resize. Per-window shortcuts. Coordinate mapping formula. |
| **wayland-mcp** | Compositor-agnostic. Action chaining syntax. |
| **hyprmcp** | Lightest weight (single file). Direct hyprctl dispatch. Hyprland config modification. |

---

## Architecture Notes

**Action chaining** is marked N/A (not ❌) because MCP's design makes the LLM the orchestrator — blind chaining bypasses effect verification, which is our biggest differentiator. Expert review confirmed this is an anti-pattern for MCP.

**Per-window shortcuts** is marked N/A because Wayland's security model fundamentally prevents input injection into non-focused surfaces. This is a compositor-level constraint, not a missing feature. Our focus→verify→send pattern is more reliable.
