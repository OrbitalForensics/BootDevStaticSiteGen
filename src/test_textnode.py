import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_url_blank(self):
        node = TextNode("This is a text node", TextType.CODE, "")
        self.assertEqual(node.url, "")

    def test_url_not_eq(self):
        node1 = TextNode("This is a text node", TextType.LINK, "http://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "http://different.com")
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()