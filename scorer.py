def judge(question, expects, answer, results) -> bool:
    if not expects:
        return True
    
    if not answer:
        return False
    
    return expects.lower() in answer.lower()


