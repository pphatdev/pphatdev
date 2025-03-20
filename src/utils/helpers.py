def generate_progress_bar(percent):
    """Generate a progress bar using emojis based on percentage
    █: 10%, █: 5%, ░: remaining
    """
    total_blocks = 25
    green_blocks = int((percent / 100) * total_blocks)
    yellow_blocks = 1 if percent > 0 and green_blocks < total_blocks else 0
    white_blocks = total_blocks - green_blocks - yellow_blocks

    progress = "█" * green_blocks + "█" * yellow_blocks + "░" * white_blocks
    return progress