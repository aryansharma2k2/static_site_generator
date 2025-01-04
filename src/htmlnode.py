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
            return f"<{self.tag} {self.props_to_html}>{self.value}</{self.tag}>"
        