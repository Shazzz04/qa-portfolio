import subprocess
import sys

tests = [
    "test_login.py",
    "test_cart.py", 
    "test_cart_navigation.py",
    "test_checkout.py"
]

print("Running SauceDemo Selenium Suite (4 tests)")
print("=" * 50)

for test in tests:
    print(f"\n Running {test}...")
    result = subprocess.run([sys.executable, test], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)
