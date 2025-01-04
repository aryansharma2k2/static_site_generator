from textnode import TextType, TextNode
import re
class HtmlNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def __repr__(self):
        return f"({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if self.tag==other.tag and self.value==other.value and self.children==other.children and self.props==other.props:
            return True
        else:
            return False

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            self.props = {}
        props_as_string = ""
        for i in self.props:
             props_as_string += f" {i}=\"{self.props[i]}\""
        return props_as_string

class LeafNode(HtmlNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)


    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return f"{self.value}" 
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HtmlNode):
    def __init__(self, tag, children, props={}, value=None):
        super().__init__(tag, value, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError
        elif not self.children:
            raise ValueError("children argument empty")
        else:
            bruh = ""
            for child in self.children:
                bruh+=child.to_html()
            return f"<{self.tag}{self.props_to_html()}>"+bruh+f"</{self.tag}>"

def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.NORMAL.value:
                return LeafNode(tag=None, value=text_node.text,)
            case TextType.BOLD.value:
                return LeafNode(tag="b", value=text_node.text,)
            case TextType.ITALIC.value:
                return LeafNode(tag="i", value=text_node.text,)
            case TextType.CODE.value:
                return LeafNode(tag="code", value=text_node.text,)
            case TextType.LINKS.value:
                return LeafNode(tag="a", value=text_node.text,props={"href":text_node.url})
            case TextType.IMAGES.value:
                return LeafNode(tag="img", value="",props={"src":text_node.url,"url":text_node.text})
            case _:
                raise Exception("Invalid text type provided for text node")
            
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #returns list of TextNodes with the respective node type except images and links
    new_nodes = []
    for node in old_nodes:
        text = node.text
        node_type = node.text_type
        node_texts = text.split(delimiter)
        node_texts_length = len(node_texts)
        if node_texts_length>1:
            if node_texts_length%2==0:
                raise Exception("Invalid markdown syntax")
            else:
                counter = 0
                for curr_text in node_texts:
                    if counter%2==0:
                        new_nodes.append(TextNode(text=curr_text, text_type=node_type))
                    else:
                        new_nodes.append(TextNode(text=curr_text, text_type=text_type))
                    counter+=1
        else:
            new_nodes.append(TextNode(text=text, text_type=node_type))
    return new_nodes

def extract_markdown_images(text):
    #returns list of tuples - [(alt_text,url)]
    images = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)',text)
    return images

def extract_markdown_links(text):
    #returns list of tuples - [(alt_text,url)]
    links = re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)',text)
    return links

def split_nodes_image(old_nodes):
    #returns list of TextNodes with respective node type specifically for images
    result = []
    for node in old_nodes:
        text = node.text
        images_data = extract_markdown_images(text)
        node_type = node.text_type
        url = None
        if node.url:
            url = node.url
        if len(images_data)>0:
            for pair in images_data:
                alt_text = pair[0]
                link = pair[1]
                sections = text.split(f"![{alt_text}]({link})",1)
                if sections[0]:
                    result.append(TextNode(text=sections[0], text_type=node_type,))
                result.append(TextNode(text=alt_text, text_type="images",url=link))
                text = sections[1]
            if text:
                result.append(TextNode(text=text, text_type=node_type,))
        else:
            result.append(TextNode(text=text, text_type=node_type, url=url))
    return result
        
def split_nodes_link(old_nodes):
    #returns list of TextNodes with respective node type specifically for links
    result = []
    for node in old_nodes:
        text = node.text
        links_data = extract_markdown_links(text)
        node_type = node.text_type
        url = None
        if node.url:
            url = node.url
        if len(links_data)>0:
            for pair in links_data:
                alt_text = pair[0]
                link = pair[1]
                sections = text.split(f"[{alt_text}]({link})",1)
                if sections[0]:
                    result.append(TextNode(text=sections[0], text_type=node_type,))
                result.append(TextNode(text=alt_text, text_type="links",url=link))
                text = sections[1]
            if text:
                result.append(TextNode(text=text, text_type=node_type,))
        else:
            result.append(TextNode(text=text, text_type=node_type, url=url))
    return result

def text_to_textnodes(text):
    #returns list of text nodes from the string in a block
    texty = TextNode(text=text,text_type=TextType.NORMAL.value,)
    listy = []
    listy=split_nodes_delimiter([texty],"**",TextType.BOLD.value)
    listy=split_nodes_delimiter(listy,"*",TextType.ITALIC.value)
    listy=split_nodes_delimiter(listy,"`",TextType.CODE.value)
    listy=split_nodes_image(listy)
    print(listy)
    listy=split_nodes_link(listy)
    return listy

def markdown_to_blocks(markdown):
    #returns list of blocks
    result = markdown.split("\n\n")
    result = list(map(lambda x: x.strip(), result))
    return [l for l in result if l]
