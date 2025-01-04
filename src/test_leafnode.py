import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "testing", [], {"href": "https://www.google.com"})
        node2 = LeafNode("p", "testing", [], {"href": "https://www.google.com"})
        self.assertEqual(node1,node2)
    
    def test_noteq(self):
        node1 = LeafNode("p", "testing", [], {"href": "https://www.google.com"})
        node2 = LeafNode("a", "testing", [], {"href": "https://www.google.com"})
        self.assertNotEqual(node1,node2)

    def test_to_html(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node1.to_html()
        self.assertEqual(result,"<a href=\"https://www.google.com\">Click me!</a>")