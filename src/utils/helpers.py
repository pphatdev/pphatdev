BAR_STYLES = {
    "block":   ("█", "░"),
    "shade":   ("▓", "░"),
    "ascii":   ("#", "-"),
    "dot":     ("●", "○"),
    "pipe":    ("|", "·"),
    # 3-tuple styles: (filled, transition, empty)
    "emoji":   ("🟩", "🟨", "⬜"),
}


def generate_progress_bar(percent, style="block", width=25):
    """Generate a progress bar for a percentage value.

    Args:
        percent: Value between 0 and 100.
        style:   One of 'block', 'shade', 'ascii', 'dot', 'arrow', 'pipe', 'emoji'.
            style:   One of 'block', 'shade', 'ascii', 'dot', 'pipe', 'emoji'.
        width:   Total number of characters in the bar (default 25).
    """
    if style not in BAR_STYLES:
        raise ValueError(
            f"Unknown style '{style}'. Choose from: {', '.join(BAR_STYLES)}")

    chars = BAR_STYLES[style]
    normalized = max(0, min(percent, 100))
    filled = round((normalized / 100) * width)
    empty = width - filled

    if len(chars) == 3:
        filled_char, transition_char, empty_char = chars
        if filled == 0:
            return empty_char * width
        if filled == width:
            return filled_char * width
        return filled_char * (filled - 1) + transition_char + empty_char * empty

    filled_char, empty_char = chars
    return filled_char * filled + empty_char * empty
