def grade_exam(answers, questions):
    score = 0
    for i, q in enumerate(questions):
        if i in answers and answers[i] == q["answer"]:
            score += 1
    return score, len(questions)
