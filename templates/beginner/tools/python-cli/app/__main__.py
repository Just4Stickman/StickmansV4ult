import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Python CLI starter")
    sub = parser.add_subparsers(dest="command")
    greet = sub.add_parser("greet")
    greet.add_argument("name")
    return parser

def main():
    args = build_parser().parse_args()
    if args.command == "greet":
        print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
