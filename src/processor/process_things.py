import time
from app.colours import GREEN, RESET
def ack_preoccupation(preoccupation: str) -> None:
    """
    Ackowledge the preoccupation, thank it for showing up. 
    This is needed to avoid dismissing the preoccupation too early.
    """
    time.sleep(1.5)
    print(f"{GREEN}Ackowledged.{RESET}")
    pass

def process_preoccupation(preoccupation: str) -> None:
    """
    The preoccupation shall pass now.
    """
    ack_preoccupation(preoccupation)
    print(f"{GREEN}This will pass soon.{RESET}")
    pass

def process_all_purpose() -> None:
    print(f"{GREEN}All things must pass.{RESET}")
    pass