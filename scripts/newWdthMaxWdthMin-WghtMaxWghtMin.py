from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
from mutatorMath.ufo.document import DesignSpaceDocumentWriter, DesignSpaceDocumentReader

path = u"/Users/SO/Desktop/Typemade/TypeDesign/FB/Amstelvar/Amstelvar-SO/sources/Amstelvar-Roman-so.designspace"
doc = DesignSpaceDocumentReader(path, ufoVersion=3)
doc.process(makeGlyphs=True, makeKerning=True, makeInfo=True)
print 'done'