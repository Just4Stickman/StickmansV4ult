import unittest
from app.__main__ import build_parser

class CliTests(unittest.TestCase):
    def test_greet_argument(self):
        args = build_parser().parse_args(["greet","Test"])
        self.assertEqual(args.name, "Test")

if __name__ == "__main__":
    unittest.main()
