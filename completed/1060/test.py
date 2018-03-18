from unittest import TestCase, main
from are_they_equal import format_
class TestFormat(TestCase):
    def test_format(self):
        self.assertEqual(format_("123.0", 3), "0.123*10^3")
        self.assertEqual(format_("0.0000", 3), "0.000*10^0")
        self.assertEqual(format_("0.3234", 3), "0.323*10^0")
        self.assertEqual(format_("1.0000", 3), "0.100*10^1")
        self.assertEqual(format_("123456.7", 4), "0.1234*10^6")
        self.assertEqual(format_("03214.3", 3), "0.321*10^4")
        self.assertEqual(format_("00001234", 3), "0.123*10^4")
        self.assertEqual(format_("12.34", 3), "0.123*10^2")
        self.assertEqual(format_("0.0000132", 2), "0.13*10^-4")
        self.assertEqual(format_("0.0000134", 2), "0.13*10^-4")
        self.assertEqual(format_("0", 2), "0.00*10^0")
        self.assertEqual(format_("345.123", 5), "0.34512*10^3")
        self.assertEqual(format_("0.00000000003", 3), "0.300*10^-10")
        self.assertEqual(format_("12300", 3), "0.123*10^5")
        self.assertEqual(format_("12358.9", 3), "0.123*10^5")
        self.assertEqual(format_("120", 3), "0.120*10^3")



if __name__ == "__main__":
    main()
