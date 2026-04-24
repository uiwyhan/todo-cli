PROMPT_SCORE = "please input your score:"
MASSAGE_GOODBYE = "it's over"
MASSAGE_INVALID_INPUT = "Invalid input. please enter a number."
MASSAGE_INVALID_INPUT_RANGE = "Invalid input. please enter a number from 0 to 100."


def massage1(a, b):
    return f"score: {a}, grade: {b}"


def massage2(
    count: int,
    average: float,
    highest: int,
    lowest: int,
) -> str:
    return (
        f"you entered {count} scores\n",
        f"average score: {average:.2f}\n",
        f"highest score: {highest}\n",
        f"lowest score: {lowest}",
    )
