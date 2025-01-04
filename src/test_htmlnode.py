import unittest

from htmlnode import HtmlNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HtmlNode("p", "testing", [], {"href": "https://www.google.com", "target": "_blank",})
        node2 = HtmlNode("p", "testing", [], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node1, node2)

    def test_noteq(self):
        node1 = HtmlNode("p", "testing yoooooo", [], {"href": "https://www.google.com", "target": "_blank",})
        node2 = HtmlNode("p", "testing", [], {"href": "https://www.google.com", "target": "_blank",})
        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        node = HtmlNode("p", "testing", [], {"href": "https://www.google.com", "target": "_blank",})
        result = node.props_to_html()
        self.assertEqual(result, " href=\"https://www.google.com\" target=\"_blank\"")