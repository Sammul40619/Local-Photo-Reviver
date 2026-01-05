import argparse
from pipeline.full_pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--restore", action="store_true")
    parser.add_argument("--colorize", action="store_true")
    parser.add_argument("--animate", choices=["parallax", "face"])
    args = parser.parse_args()
    run_pipeline(args)

if __name__ == "__main__":
    main()