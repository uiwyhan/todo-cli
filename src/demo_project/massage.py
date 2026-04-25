MENU = "\n=== Score Manager ===\n1.add score\n2.show summary\n3.clear scores\n4.quit\n"
PROMPT_MENU_CHOICE = "Choose an option:"
PROMPT_MENU_SCORE = "Enter score:"
MASSAGE_GOODBYE = "it's over"
MASSAGE_INVALID_INPUT = "Invalid input. please enter a number."
MASSAGE_INVALID_INPUT_RANGE = "Invalid input. please enter a number from 0 to 100."
MASSAGE_NO_SCORE = "No scores available."
MASSAGE_SCORES_CLEARED = "Scores cleared."
MASSAGE_MENE_INVALID = "Invalid input.please input a number from 1 to 4."


def massage1(a, b) -> str:
    return f"score: {a}, grade: {b}"


def massage2(
    count: int,
    average: float,
    highest: int,
    lowest: int,
) -> str:
    return (
        f"You entered {count} scores\n"
        f"Average: {average}\n"
        f"Highest: {highest}\n"
        f"Lowest: {lowest}\n"
    )
