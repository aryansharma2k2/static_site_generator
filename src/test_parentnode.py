import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)

        result = node.to_html()
        self.assertEqual(result, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_parent_nodes(self):
        node1 = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        node2 = ParentNode("p",[node1,],)
        
        result = node2.to_html()
        self.assertEqual(result, "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")

    def test_eq(self):
        node1 = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        node2 = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        self.assertEqual(node1,node2)

    def test_noteq(self):
        node1 = ParentNode("p",[LeafNode("i", "Bold text"),LeafNode(None, "Normal text"),LeafNode("b", "italic text"),LeafNode(None, "Normal text"),],)
        node2 = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        self.assertNotEqual(node1,node2)

