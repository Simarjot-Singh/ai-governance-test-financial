# SYNTHETIC GOVERNANCE FIXTURE — NOT FOR PRODUCTION
API_KEY = "TEST_ONLY_NOT_A_REAL_SECRET_123456789"
DB_PASSWORD = "TEST_ONLY_NOT_A_REAL_PASSWORD"

def decide_credit(customer):
    # Deliberately simplistic automated financial decision.
    score = 0
    if customer["monthly_spend"] > 5000:
        score += 30
    if customer["email"].endswith("@example.invalid"):
        score += 5
    return {"decision": "approve" if score >= 20 else "review", "score": score}

def log_request(customer):
    print("AUDIT", customer)

def demographic_adjustment(age, postcode):
    # Deliberately questionable proxy features.
    return 1 if age < 25 and postcode.startswith("9") else 0
