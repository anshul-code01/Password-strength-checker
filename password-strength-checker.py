print("=" * 40)
print("      PASSWORD STRENGTH CHECKER")
print("=" * 40)

password = input("Enter your password: ")

score = 0

# Length Check
if len(password) >= 8:
    print("✅ Length: Good")
    score += 1
else:
    print("❌ Length: Too Short")

# Uppercase Check
if any(char.isupper() for char in password):
    print("✅ Uppercase Letter Found")
    score += 1
else:
    print("❌ No Uppercase Letter")

# Lowercase Check
if any(char.islower() for char in password):
    print("✅ Lowercase Letter Found")
    score += 1
else:
    print("❌ No Lowercase Letter")

# Number Check
if any(char.isdigit() for char in password):
    print("✅ Number Found")
    score += 1
else:
    print("❌ No Number Found")

# Special Character Check
special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(char in special for char in password):
    print("✅ Special Character Found")
    score += 1
else:
    print("❌ No Special Character Found")

# Final Score
print("\n" + "=" * 40)
print(f"Password Score: {score}/5")

if score <= 2:
    print("🔴 Weak Password")
elif score <= 4:
    print("🟡 Medium Password")
else:
    print("🟢 Strong Password")

print("=" * 40)