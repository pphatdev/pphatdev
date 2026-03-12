def generate_progress_bar(percent):
    """Generate a 25-block progress bar for a percentage value."""
    total_blocks = 25
    normalized_percent = max(0, min(percent, 100))
    filled_blocks = round((normalized_percent / 100) * total_blocks)
    empty_blocks = total_blocks - filled_blocks

    progress = "█" * filled_blocks + "░" * empty_blocks
    return progress