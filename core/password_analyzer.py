import math
import string
from core.vulnerability_checker import check_vulnerabilities


def calculate_entropy(password):

    pool = 0

    if any(c in string.ascii_lowercase for c in password):
        pool += 26

    if any(c in string.ascii_uppercase for c in password):
        pool += 26

    if any(c in string.digits for c in password):
        pool += 10

    if any(c in string.punctuation for c in password):
        pool += 32

    if pool == 0:
        return 0

    return round(len(password) * math.log2(pool), 2)


def analyze_password(password):

    score = 0

    if len(password) >= 8:
        score += 20

    if len(password) >= 12:
        score += 15

    if len(password) >= 16:
        score += 10

    if any(c.islower() for c in password):
        score += 10

    if any(c.isupper() for c in password):
        score += 10

    if any(c.isdigit() for c in password):
        score += 10

    if any(c in string.punctuation for c in password):
        score += 15

    if len(set(password)) < len(password) * 0.6:
        score -= 10

    vulnerabilities = check_vulnerabilities(password)

    score -= len(vulnerabilities) * 5

    score = max(0, min(score, 100))

    if score < 25:
        strength = "Very Weak"
    elif score < 45:
        strength = "Weak"
    elif score < 65:
        strength = "Moderate"
    elif score < 85:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "score": score,
        "strength": strength,
        "entropy": calculate_entropy(password),
        "length": len(password),
        "vulnerabilities": vulnerabilities
    }