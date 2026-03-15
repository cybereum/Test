"""Shared UI styles, stylesheets, and font factories for ProBloC."""
from PyQt5 import QtGui

# --- Button Stylesheets ---

_BTN_BG = "background-repeat: no-repeat; background-position: center center;"

# Full three-state button (normal / pressed / disabled)
BUTTON_PRIMARY = (
    "QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch;"
    " color: rgb(205, 250, 255) }"
    "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch;"
    " color: rgb(200, 0, 5) }"
    "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch;"
    " color: rgb(50, 145, 205) }"
    + _BTN_BG
)

# Two-state button (normal / pressed) — no disabled style
BUTTON_SECONDARY = (
    "QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch;"
    " color: rgb(205, 250, 255) }"
    "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch;"
    " color: rgb(50, 145, 205) }"
    + _BTN_BG
)


def apply_primary_style(*buttons):
    """Apply BUTTON_PRIMARY stylesheet to one or more QPushButtons."""
    for btn in buttons:
        btn.setStyleSheet(BUTTON_PRIMARY)


def apply_secondary_style(*buttons):
    """Apply BUTTON_SECONDARY stylesheet to one or more QPushButtons."""
    for btn in buttons:
        btn.setStyleSheet(BUTTON_SECONDARY)


# --- Font Factories ---

def make_orbitron_font(size: int, spacing: float = 1.0) -> QtGui.QFont:
    """Return the standard ProBloC orbitron UI font."""
    f = QtGui.QFont()
    f.setFamily("orbitron")
    f.setPointSize(size)
    f.setBold(False)
    f.setItalic(False)
    f.setWeight(25)
    f.setLetterSpacing(f.AbsoluteSpacing, spacing)
    f.setCapitalization(f.SmallCaps)
    return f


def make_baskerville_font(size: int, spacing: float = 5.0) -> QtGui.QFont:
    """Return the ProBloC title / branding font."""
    f = QtGui.QFont()
    f.setFamily("Baskerville")
    f.setPointSize(size)
    f.setBold(False)
    f.setItalic(False)
    f.setWeight(35)
    f.setLetterSpacing(f.AbsoluteSpacing, spacing)
    f.setCapitalization(f.SmallCaps)
    return f
