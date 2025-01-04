import unittest
from htmlnode import markdown_to_blocks
class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic(self):
        markdown_text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(markdown=markdown_text)
        self.assertEqual(result,["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n* This is a list item\n* This is another list item"])