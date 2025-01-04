import unittest
from htmlnode import text_to_textnodes, TextNode, TextType
class TestTextToNodes(unittest.TestCase):
    def test_basic(self):
        text="This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertEqual(result,[
    TextNode("This is ", TextType.NORMAL.value),
    TextNode("text", TextType.BOLD.value),
    TextNode(" with an ", TextType.NORMAL.value),
    TextNode("italic", TextType.ITALIC.value),
    TextNode(" word and a ", TextType.NORMAL.value),
    TextNode("code block", TextType.CODE.value),
    TextNode(" and an ", TextType.NORMAL.value),
    TextNode("obi wan image", TextType.IMAGES.value, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.NORMAL.value),
    TextNode("link", TextType.LINKS.value, "https://boot.dev"),
])