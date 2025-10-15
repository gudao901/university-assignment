def grade_for(mark: int) -> str:
    # Adjust bands if your class uses different ones
    if mark >= 85: return "HD"
    if mark >= 75: return "D"
    if mark >= 65: return "C"
    if mark >= 50: return "P"
    return "F"

def average_mark(subjects: list[dict]) -> float:
    if not subjects:
        return 0.0
    return sum(s["mark"] for s in subjects) / len(subjects)

def is_pass_final(subjects: list[dict]) -> bool:
    """Pass rule: only 'final' when 4 subjects and avg >= 50."""
    return len(subjects) == 4 and average_mark(subjects) >= 50
