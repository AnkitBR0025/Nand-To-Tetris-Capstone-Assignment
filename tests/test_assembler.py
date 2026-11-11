import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "capstone"))
from assembler import assemble

class AssemblerTests(unittest.TestCase):
    def test_labels_variables_and_machine_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "Tiny.asm"
            out = Path(tmp) / "Tiny.hack"
            symbols = Path(tmp) / "symbols.txt"
            src.write_text(
                "// tiny program\n"
                "@2\nD=A\n@i\nM=D\n(LOOP)\n@i\nD=M\n@LOOP\n0;JMP\n",
                encoding="utf-8"
            )
            count, labels, variables = assemble(src, out, symbols)
            self.assertEqual(count, 8)
            self.assertEqual(labels["LOOP"], 4)
            self.assertEqual(variables["i"], 16)
            code = out.read_text(encoding="utf-8").splitlines()
            self.assertEqual(code[0], "0000000000000010")
            self.assertEqual(code[1], "1110110000010000")
            self.assertEqual(code[2], "0000000000010000")
            self.assertIn("LOOP\t4\tLABEL", symbols.read_text(encoding="utf-8"))
            self.assertIn("i\t16\tVARIABLE", symbols.read_text(encoding="utf-8"))

    def test_invalid_instruction_has_line_number(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "Bad.asm"
            src.write_text("@1\nD=Q\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Line 2"):
                assemble(src)

if __name__ == "__main__":
    unittest.main()
