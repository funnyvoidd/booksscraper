import argparse
from src.core.engine import run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="src/config/config.yaml")
    args = parser.parse_args()

    run(args.config)


if __name__ == "__main__":
    main()