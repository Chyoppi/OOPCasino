# This custom color library is created using AI

import re
import builtins

# Saving original print
original_print = builtins.print

class CPrint:
    COLORS = {
        "r": "\033[91m",  # Red
        "g": "\033[92m",  # Green
        "y": "\033[93m",  # Yellow
        "b": "\033[94m",  # Blue
        "m": "\033[95m",  # Magenta
        "c": "\033[96m",  # Cyan
        "reset": "\033[0m"  # Reset
    }

    @staticmethod
    def parse_colors(text):
        def replace_color(match):
            color_code = match.group(1)
            if color_code == "reset":
                return CPrint.COLORS["reset"]
            return CPrint.COLORS.get(color_code, "")

        colored_text = re.sub(r"~(reset|[a-z])~", replace_color, text)
        return f"{colored_text}{CPrint.COLORS['reset']}"

    @staticmethod
    def custom_print(*args, **kwargs):
        text = " ".join(str(arg) for arg in args)
        colored_text = CPrint.parse_colors(text)
        original_print(colored_text, **kwargs)


builtins.print = CPrint.custom_print