import sys

if len(sys.argv) < 2:
    print("Usage: python gigione.py <number>")
    sys.exit(1)

gigione = sys.argv[1]

print(f"Numarul introdus este: {gigione}")
