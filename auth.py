import hashlib

# High-Security Password Hashes (SHA-256) instead of plaintext
# "1234" -> 03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4
# "admin123" -> 240be518fabd2724ddb6f04eeb1da5967448d7e65447e0340d8aa506f36077fb
USERS = {
    "student": {
        "student1": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
        "student2": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    },
    "teacher": {
        "teacher1": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    },
    "admin": {
        "admin": "240be518fabd2724ddb6f04eeb1da5967448d7e65447e0340d8aa506f36077fb"
    }
}

FAILED_ATTEMPTS = {}
MAX_FAILED_ATTEMPTS = 5

def hash_password(password):
    """Securely hash plain-text passwords using SHA-256."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def login_user(role, username, password):
    """
    High security login verifier with SHA-256 password hashing 
    and brute-force rate-limiting lockouts.
    """
    if role not in USERS:
        return False
        
    # Bruteforce protection check
    user_key = f"{role}:{username}"
    if FAILED_ATTEMPTS.get(user_key, 0) >= MAX_FAILED_ATTEMPTS:
        # User is locked out
        return "LOCKED"

    hashed = hash_password(password)
    if username in USERS[role] and USERS[role][username] == hashed:
        # Reset brute-force counter on success
        FAILED_ATTEMPTS[user_key] = 0
        return True
    else:
        # Increment failure count
        FAILED_ATTEMPTS[user_key] = FAILED_ATTEMPTS.get(user_key, 0) + 1
        return False
