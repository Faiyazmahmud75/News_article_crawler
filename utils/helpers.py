# Helper fucntion for cleaning whitespaces
import re

def clean_whitespace(text: str) -> str:
    """Collapse multiple spaces/newlines into single spaces."""
    return re.sub(r"\s+", " ", text).strip()
