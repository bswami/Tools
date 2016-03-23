
import sys
import xml.dom.minidom

wpXMLFile = sys.argv[1]

blogDoc = xml.dom.minidom.parse(wpXMLFile)

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def handlePre():
    print "<html>"

def handleEnd():
    print "</body></html>"
    
def handleTitle(dom):
    chanElem = dom.getElementsByTagName("channel")[0]
    tElem = chanElem.getElementsByTagName("title")[0]
    title = getText(tElem.childNodes)
    print "<head><title> %s </title> </head>" % title
    print "<body> <h2> %s </h2>" %  title

def handlePost(item):
    tElem = item.getElementsByTagName("title")[0]
    print "<h3> %s </h3>" % getText(tElem.childNodes)
    contentElem = item.getElementsByTagName("content:encoded")[0]
    cbody = contentElem.toxml()
    cbody = cbody.replace("<content:encoded><![CDATA[",'')
    ctext = cbody.replace("]]></content:encoded>",'')
    print "<p> %s </p>" % ctext

    
def handlePosts(dom):
    chanElem = dom.getElementsByTagName("channel")[0]
    itemList = chanElem.getElementsByTagName("item")
    for item in itemList:
        handlePost(item)
        
handlePre()
handleTitle(blogDoc)
handlePosts(blogDoc)
handleEnd()
