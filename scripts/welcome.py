import os
import sys

# ANSI Escape Sequences for Colors
PEACH = "\033[38;2;212;140;107m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def display_splash():
    # Welcome Box
    width = 70
    print(f"\n{PEACH}┌" + "─" * (width-2) + "┐")
    print(f"│  {WHITE}* Welcome to the {BOLD}Smart AI Skills Library{RESET}{WHITE} research preview!{PEACH}   │")
    print("└" + "─" * (width-2) + "┘" + RESET)

    # PREMIUM SOLID BLOCK LOGO
    # Font: 'Blocks' style
    logo = f"""
{PEACH}   ██████╗ ███╗   ███╗ █████╗ ██████╗ ████████╗ {WHITE}  █████╗ ██╗
{PEACH}  ██╔════╝ ████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝ {WHITE} ██╔══██╗██║
{PEACH}  ╚█████╗  ██╔████╔██║███████║██████╔╝   ██║    {WHITE} ███████║██║
{PEACH}   ╚═══██╗ ██║╚██╔╝██║██╔══██║██╔══██╗   ██║    {WHITE} ██╔══██║██║
{PEACH}  ██████╔╝ ██║ ╚═╝ ██║██║  ██║██║  ██║   ██║    {WHITE} ██║  ██║██║
{PEACH}  ╚═════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    {WHITE} ╚═╝  ╚═╝╚═╝

{CYAN}        ███████╗██╗  ██╗██╗██╗     ██╗     ███████╗
{CYAN}        ██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝
{CYAN}        ███████╗█████╔╝ ██║██║     ██║     ███████╗
{CYAN}        ╚════██║██╔═██╗ ██║██║     ██║     ╚════██║
{CYAN}        ███████║██║  ██╗██║███████╗███████╗███████║
{CYAN}        ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝
    """
    print(logo)

    # Status Line
    print(f"{WHITE}  {BOLD}SYSTEM:{RESET} {CYAN}Smart AI Skills Library{RESET} | {WHITE}v2.2.9{RESET}")
    print(f"{WHITE}  {BOLD}PKG:{RESET}    {PEACH}@harshitj183/ai-skills{RESET}")
    print(f"{WHITE}  {BOLD}REPO:{RESET}   {CYAN}harshitj183/ai-skills{RESET}")
    print(f"{WHITE}  {BOLD}STATUS:{RESET} {BOLD}READY{RESET}")
    print(f"{WHITE}  {BOLD}MODE:{RESET}   Direct Orchestration Active{RESET}\n")

if __name__ == "__main__":
    display_splash()
