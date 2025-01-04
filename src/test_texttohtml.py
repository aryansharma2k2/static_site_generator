import unittest

from htmlnode import text_node_to_html_node, LeafNode
from textnode import TextNode

class TestTextToHTML(unittest.TestCase):
    def test_links(self):
        node1 = TextNode("I hope this works on the first try!", text_type="links",url="abcd.com")
        leafy = LeafNode(tag="a",value="I hope this works on the first try!",props={"href":"abcd.com"},)
        result = text_node_to_html_node(node1)
        self.assertEqual(result,leafy)

    def test_normal(self):
        node1 = TextNode("I hope this works on the first try!", text_type="normal",)
        leafy = LeafNode(tag=None,value="I hope this works on the first try!",)
        result = text_node_to_html_node(node1)
        self.assertEqual(result,leafy)
    
    def test_bold(self):
        node1 = TextNode("I hope this works on the first try!", text_type="bold",)
        leafy = LeafNode(tag="b",value="I hope this works on the first try!",)
        result = text_node_to_html_node(node1)
        self.assertEqual(result,leafy)

    def test_italic(self):
        node1 = TextNode("I hope this works on the first try!", text_type="italic",)
        leafy = LeafNode(tag="i",value="I hope this works on the first try!",)
        result = text_node_to_html_node(node1)
        self.assertEqual(result,leafy)