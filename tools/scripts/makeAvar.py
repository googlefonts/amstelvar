import os
from fontTools.designspaceLib import DesignSpaceDocument
scriptsFolder = os.path.split(__file__)[0]
baseFolder = os.path.split(scriptsFolder)[0]
path = os.path.join(baseFolder, "sources/Amstelvar-Roman.designspace")
d =  DesignSpaceDocument()
d.read(path)
for a in d.axes:
    if a.tag != 'opsz':
        print """    <segment axis="%s">
      <mapping from="0" to="0"/>
      <mapping from="1" to="1"/>
    </segment>""" % a.tag