import unittest
from textnode import TextNode
from htmlnode import split_nodes_image, split_nodes_link
class TestNodesImageAndLink(unittest.TestCase):
    def test_image(self):
        nodes = [TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)","normal",)]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(new_nodes,[TextNode("This is text with a link ", "normal"),TextNode("to boot dev", "images", "https://www.boot.dev"),TextNode(" and ", "normal"),TextNode("to youtube", "images", "https://www.youtube.com/@bootdotdev"),])
    
    def test_links(self):
        nodes = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)","normal",)]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(new_nodes,[TextNode("This is text with a link ", "normal"),TextNode("to boot dev", "links", "https://www.boot.dev"),TextNode(" and ", "normal"),TextNode("to youtube", "links", "https://www.youtube.com/@bootdotdev"),])