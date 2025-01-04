import unittest
from textnode import TextNode
from htmlnode import split_nodes_delimiter
class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", "normal")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes,[TextNode("This is text with a ", "normal"),TextNode("code block", "code"),TextNode(" word", "normal"),])
    
    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", "normal")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes,[TextNode("This is text with a ", "normal"),TextNode("bold block", "bold"),TextNode(" word", "normal"),])