import dataclasses

import lxml.html

import ctfd_dl.exceptions


def xpath(element: lxml.html.HtmlElement, path: str):
    nodes = element.xpath(path)
    assert isinstance(nodes, list)
    for node in nodes:
        if type(node) is lxml.html.HtmlElement:
            yield HtmlElement(node)
        elif type(node) is lxml.html.InputElement:
            yield InputElement(node)
        else:
            raise ctfd_dl.exceptions.Error


def get(element: lxml.html.HtmlElement, key: str):
    value = element.get(key)
    assert isinstance(value, str)
    return value


@dataclasses.dataclass
class HtmlElement:
    element: lxml.html.HtmlElement

    def xpath(self, path: str):
        return xpath(self.element, path)

    def get(self, key: str):
        return get(self.element, key)


@dataclasses.dataclass
class InputElement:
    element: lxml.html.InputElement

    def xpath(self, path: str):
        return xpath(self.element, path)

    def get(self, key: str):
        return get(self.element, key)


def document_from_string(html: str):
    element = lxml.html.document_fromstring(html)
    assert isinstance(element, lxml.html.HtmlElement)
    return HtmlElement(element)
