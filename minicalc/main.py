import sys
from .interpreter import run

def main():
    if len(sys.argv) < 2:
        print("Uso: python -m minicalc.main <arquivo.mc>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    run(source)

if __name__ == "__main__":
    main()