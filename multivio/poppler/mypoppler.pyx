from libcpp cimport *
from libcpp.string cimport string
from cpython cimport bool as PyBool
from cpython.object cimport Py_EQ, Py_NE
from cpython.ref cimport PyObject
import multivio

################## Cython Intreface with poppler (C++) #######################
ctypedef bool GBool
ctypedef unsigned char Guchar
ctypedef unsigned short Gushort
ctypedef unsigned int Guint
ctypedef unsigned long Gulong
ctypedef long long Goffset
ctypedef Guchar SplashColor[4]
ctypedef Guchar *SplashColorPtr
ctypedef unsigned int Unicode;

cdef extern from "GlobalParams.h":
    GlobalParams *globalParams
    cdef cppclass GlobalParams:
        GBool getOverprintPreview()
        GBool setEnableFreeType(char *s)
        void setErrQuiet(GBool errQuietA)
globalParams = new GlobalParams()

cdef extern from "goo/GooString.h":
    cdef cppclass GooString:
        GooString(const char *sA)
        int getLength()
        char *getCString()
        char getChar(int i)

cdef extern from "goo/GooList.h":
    cdef cppclass GooList:
        GooList()
        GooList(int sizeA)
        int getLength()
        OutlineItem *get(int i)

cdef extern from "OutputDev.h":
    cdef cppclass OutputDev:
        pass

cdef extern from "Catalog.h":
    cdef cppclass NameTree:
        pass
    cdef cppclass Catalog:
        Object *getOutline()

cdef extern from "Outline.h":
    cdef cppclass Outline:
        GooList *getItems()
    cdef cppclass OutlineItem:
      Unicode *getTitle()
      int getTitleLength()

cdef extern from 'Annot.h':
    cdef cppclass Annot:
        pass

cdef extern from 'XRef.h':
    cdef cppclass XRef:
        pass

cdef extern from 'Link.h':
    cdef cppclass LinkAction:
        pass
    cdef cppclass LinkDest:
        pass
    cdef cppclass LinkGoTo:
        pass

cdef extern from 'splash/SplashBitmap.h':
    cdef cppclass SplashBitmap:
      int getWidth()
      int getHeight()
      int getRowSize()
      SplashColorPtr getDataPtr()
      Guchar *getAlphaPtr()

cdef extern from 'splash/Splash.h':
    cdef cppclass Splash:
        pass

cdef extern from 'splash/SplashTypes.h':
    cdef enum SplashColorMode:
      splashModeMono1,
      splashModeMono8,
      splashModeRGB8,
      splashModeBGR8,
      splashModeXBGR8,
      splashModeCMYK8
    cdef enum SplashThinLineMode:
      splashThinLineDefault,
      splashThinLineSolid,
      splashThinLineShape

cdef extern from 'splash/SplashFontEngine.h':
    cdef cppclass SplashFontEngine:
        pass

cdef extern from 'Object.h':
    cdef cppclass Object:
        char *getTypeName()
        ObjType getType()
        GBool isReal()
        GBool isDict()
        GBool isString()
        GBool isName()
        GBool isBool()
        GBool isNull()
        GBool isNum()
        GBool isInt()
        Dict *getDict()
        GBool getBool()
        int getInt()
        double getNum()
        double getReal()
        GooString *getString()
        char *getName()
        GooString *takeString()
    cdef enum ObjType :
      objBool,			# boolean
      objInt,			# integer
      objReal,			# real
      objString,			# string
      objName,			# name
      objNull,			# null
      # complex objects
      objArray,			# array
      objDict,			# dictionary
      objStream,			# stream
      objRef,			# indirect reference
      # special objects
      objCmd,			# command name
      objError,			# error return from Lexer
      objEOF,			# end of file return from Lexer
      objNone,			# uninitialized object
      # poppler-only objects
      objInt64,			# integer with at least 64-bits
      objDead			# and object after shallowCopy

cdef extern from "PDFDoc.h":
    cdef cppclass PDFDoc:
        PDFDoc(GooString *fileNameA, GooString *ownerPassword = NULL, GooString *userPassword = NULL, void *guiDataA = NULL)
        int getNumPages()
        void displayPage(OutputDev *out, int page,
           double hDPI, double vDPI, int rotate,
           GBool useMediaBox, GBool crop, GBool printing,
           GBool (*abortCheckCbk)(void *data) = NULL,
           void *abortCheckCbkData = NULL,
            GBool (*annotDisplayDecideCbk)(Annot *annot, void *user_data) = NULL,
            void *annotDisplayDecideCbkData = NULL, GBool copyXRef = False)
        double getPageMediaWidth(int page)
        double getPageMediaHeight(int page)
        XRef *getXRef()
        int getPageRotate(int page)
        Catalog *getCatalog()
        Outline *getOutline()
        Object getDocInfo()

cdef extern from "PDFDocFactory.h":
    cdef cppclass PDFDocFactory:
        PDFDocFactory()
        PDFDoc *createPDFDoc(const GooString &uri, GooString *ownerPassword = NULL,
                             GooString *userPassword = NULL, void *guiDataA = NULL)

cdef extern from "TextOutputDev.h":
    cdef cppclass TextOutputDev:
        TextOutputDev(char *fileName, GBool physLayoutA, double fixedPitchA, GBool rawOrderA, GBool append)
        TextPage *takeText()

    cdef cppclass TextPage:
        void incRefCnt()
        void decRefCnt()
        TextFlow *getFlows()

    cdef cppclass TextFlow:
        TextFlow *getNext()
        TextBlock *getBlocks()

    cdef cppclass TextBlock:
        TextBlock *getNext()
        TextLine *getLines()
        void getBBox(double *xMinA, double *yMinA, double *xMaxA, double *yMaxA)

    cdef cppclass TextLine:
        TextWord *getWords()
        TextLine *getNext()

    cdef cppclass TextWord:
        TextWord *getNext()
        int getLength()
        GooString *getText()
        void getBBox(double *xMinA, double *yMinA, double *xMaxA, double *yMaxA)
        void getCharBBox(int charIdx, double *xMinA, double *yMinA,
           double *xMaxA, double *yMaxA)
        GBool hasSpaceAfter  ()
        GooString *getFontName(int idx)
        double getFontSize()
        void getColor(double *r, double *g, double *b)

cdef extern from "SplashOutputDev.h":
    cdef cppclass SplashOutputDev:
        SplashOutputDev(SplashColorMode colorModeA, int bitmapRowPadA,
      		  GBool reverseVideoA, SplashColorPtr paperColorA,
      		  GBool bitmapTopDownA = gTrue,
      		  SplashThinLineMode thinLineMode = splashThinLineDefault,
      		  GBool overprintPreviewA = globalParams.getOverprintPreview())
        SplashBitmap *getBitmap()
        void startDoc(PDFDoc *docA)


cdef extern from "goo/gmem.h":
    pass

cdef extern from "PDFDocEncoding.h":
    char* pdfDocEncodingToUTF16 (GooString* orig, int* length)

cdef extern from "Dict.h":
    cdef cppclass Dict:
      int getLength()
      char *getKey(int i)
      Object lookup(const char *key, int recursion)


##################### Extern acces by Python  ################################
DEF PRECISION=1e-6

def init():
  globalParams = new GlobalParams()
  globalParams.setEnableFreeType("yes")
  globalParams.setErrQuiet(True)

cdef class _PDFDoc:
  cdef:
      PDFDoc *_doc
      int _pg
      PyBool phys_layout
      double fixed_pitch

  def __cinit__(self, char *fileNameA,  PyBool phys_layout=False, double fixed_pitch=0):
      self._doc =  PDFDocFactory().createPDFDoc(GooString(fileNameA))
      self._pg=0
      self.phys_layout=phys_layout
      self.fixed_pitch=fixed_pitch

  def __dealloc__(self):
      if self._doc != NULL:
          del self._doc

  def _getNumPages(self):
      return self._doc.getNumPages()

  def _getToc(self):
      cdef Outline *outline
      cdef GooList *list
      child = []
      # outline = self._doc.getOutline()
      # list = outline.getItems()
      # data = list.get(1)
      # child.append(data.getTitleLength())
      return child

  def _getInfo(self):
      cdef :
        Object info
        Object obj
        Unicode *title = NULL
        int titleLen = 0
        int len = 1
        GooString* s = NULL
        Dict *info_dict
        char* key

      dic = {}
      info = self._doc.getDocInfo()
      if not info.isDict():
        return dic

      info_dict = info.getDict()
      for i in range(0,info_dict.getLength()):
        key = info_dict.getKey(i)
        key1 = <unicode>key.decode('UTF-8')
        obj = info_dict.lookup(key, 1)
        if obj.isString():
          s = obj.takeString()
          dic[key1] = <unicode>s.getCString().decode('UTF-8')
        elif obj.isName() :
          dic[key1] = (<char *>obj.getName()).decode('UTF-8')
        elif obj.isNum() :
          dic[key1] = obj.getNum()
        elif obj.isBool() :
          dic[key1] = obj.getBool()
        elif obj.isNull() :
          dic[key1] = "Null"
      return dic

  def _getPageMediaWidth(self, int pg):
      return self._doc.getPageMediaWidth(pg)

  def _getPageMediaHeight(self, int pg):
      return self._doc.getPageMediaHeight(pg)

  def _getPagePageRotate(self, int pg):
      return self._doc.getPageRotate(pg)

  cdef void render_page(self, OutputDev *dev, int page_no, double hDPI, double vDPI, int rotate, PyBool useMediaBox, PyBool crop, PyBool printing ):
      self._doc.displayPage(dev, page_no, hDPI, vDPI, rotate, useMediaBox, crop, printing)

  cdef object get_page_size(self, page_no):
       cdef double w,h
       w=self._doc.getPageMediaWidth(page_no)
       h= self._doc.getPageMediaHeight(page_no)
       return (w,h)

  def __iter__(self):
      return self

  def get_page(self, int pg):
      return Page(pg, self)

  def get_image(self, int pg): #TODO
      return Image(pg, self)


  def __next__(self):
      if self._pg >= self._getNumPages():
        raise StopIteration()
      self._pg+=1
      return self.get_page(self._pg)


cdef class Image:
  cdef:
      SplashOutputDev *splash
      SplashBitmap *bitmap
      double scale
      _PDFDoc pdf

  def __cinit__(self, int page, _PDFDoc pdf):
      self.pdf = pdf
      self.splash = new SplashOutputDev(splashModeRGB8, 3, False, [255,255,255])
      self.splash.startDoc(self.pdf._doc)
      self.scale = self._getOptimalScale(595.0, 842.0, page) #TODO
      self.scale = 1.0
      self.pdf._doc.displayPage(<OutputDev*>self.splash, page, 72*self.scale, 72*self.scale, 0, True, False, False)
      self.bitmap = self.splash.getBitmap()

  def _getScale(self):
      return self.scale

  def printBitmap(self):
      print(self.bitmap.getDataPtr())

  def _getBitmap(self):
      return <char *>self.bitmap.getDataPtr()

  def _getHeight(self):
      return self.bitmap.getHeight()

  def _getWidth(self):
      return self.bitmap.getWidth()

  def _getOptimalScale(self, max_width, max_height, page_nr):
        """Compute the optimal scale factor."""
        if max_width is None and max_height is None:
            return 1.0
        page_width = self.pdf._doc.getPageMediaWidth(page_nr)
        page_height = self.pdf._doc.getPageMediaHeight(page_nr)
        if(int(self.pdf._doc.getPageRotate(page_nr)) % 180 == 90):
            page_width, page_height = page_height, page_width

        page_ratio = page_height/float(page_width)
        if max_width is None:
            max_width = max_height/page_ratio
        if max_height is None:
            max_height = max_width*page_ratio
        scale = max_width/page_width
        if max_height < (page_height*scale):
            scale = max_height/page_height
        return scale

cdef class Page:
  cdef:
      int page_no
      TextPage *page
      _PDFDoc doc
      TextFlow *curr_flow

  def __cinit__(self, int page_no, _PDFDoc doc):
      cdef TextOutputDev *dev
      self.page_no=page_no
      dev = new TextOutputDev(NULL, doc.phys_layout, doc.fixed_pitch, False, False)
      doc.render_page(<OutputDev*> dev, page_no, 72, 72, 0, True, False, False)
      self.page= dev.takeText()
      del dev
      self.curr_flow = self.page.getFlows()
      self.doc=doc

  def __dealloc__(self):
      if self.page != NULL:
          self.page.decRefCnt()

  def __iter__(self):
      return self

  def __next__(self):
      cdef Flow f
      if not self.curr_flow:
          raise StopIteration()
      f=Flow(self)
      self.curr_flow=self.curr_flow.getNext()
      return f

  property page_no:
      def __get__(self):
          return self.page_no

  property size:
      def __get__(self):
          return self.doc.get_page_size(self.page_no)

cdef class Flow:
    cdef:
        TextFlow *flow
        TextBlock *curr_block

    def __cinit__(self, Page pg):
        self.flow=pg.curr_flow
        self.curr_block=self.flow.getBlocks()

    def __iter__(self):
        return self

    def __next__(self):
        cdef Block b
        if not self.curr_block:
            raise StopIteration()
        b=Block(self)
        self.curr_block=self.curr_block.getNext()
        return b

cdef class Block:
    cdef:
        TextBlock *block
        TextLine *curr_line

    def __cinit__(self, Flow flow):
        self.block= flow.curr_block
        self.curr_line=self.block.getLines()


    def __iter__(self):
        return self

    def __next__(self):
        cdef Line l
        if not self.curr_line:
            raise StopIteration()
        l=Line(self)
        self.curr_line=self.curr_line.getNext()
        return l

    property bbox:
        def __get__(self):
            cdef double x1,y1,x2,y2
            self.block.getBBox(&x1, &y1, &x2, &y2)
            return  BBox(x1,y1,x2,y2)

cdef class BBox:
    cdef double x1, y1, x2, y2

    def __cinit__(self, double x1, double y1, double x2, double y2 ):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def as_tuple(self):
        return self.x1,self.y1, self.x2, self.y2

    def __getitem__(self, i):
        if i==0:
            return self.x1
        elif i==1:
            return self.y1
        elif i==2:
            return self.x2
        elif i==3:
            return self.y2
        raise IndexError()

    property x1:
        def __get__(self):
            return self.x1
        def __set__(self, double val):
            self.x1=val

    property x2:
        def __get__(self):
            return self.x2
        def __set__(self, double val):
            self.x2=val

    property y1:
        def __get__(self):
            return self.y1
        def __set__(self, double val):
            self.y1=val

    property y2:
        def __get__(self):
            return self.y2
        def __set__(self, double val):
            self.y2=val


cdef class Line:
    cdef:
        TextLine *line
        double x1, y1, x2, y2
        unicode _text
        list _bboxes


    def __cinit__(self, Block block):
        self.line = block.curr_line

    def __init__(self, Block block):
        self._text=u'' # text bytes
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self._bboxes=[]
        self._get_text()
        assert len(self._text) == len(self._bboxes)

    def _get_text(self):
        cdef:
            TextWord *w
            GooString *s
            double bx1,bx2, by1, by2
            list words = []
            int offset = 0, i, wlen
            BBox last_bbox

        w=self.line.getWords()
        while w:
            wlen=w.getLength()
            assert wlen>0
            # gets bounding boxes for all characters
            # and font info
            for i in range(wlen):
                w.getCharBBox(i, &bx1, &by1, &bx2, &by2 )
                last_bbox=BBox(bx1,by1,bx2,by2)
                # if previous word is space update it's right end
                if i == 0 and words and words[-1] == u' ':
                    self._bboxes[-1].x2=last_bbox.x1

                self._bboxes.append(last_bbox)
            #and then text as UTF-8 bytes
            s=w.getText()
            #print s.getCString(), w.getLength(), len(s.getCString())
            words.append(<unicode>((s.getCString()).decode('UTF-8'))) # decoded to python unicode string
            del s
            # must have same ammount of bboxes and characters in word
            assert len(words[-1]) == wlen
            #calculate line bbox
            w.getBBox(&bx1, &by1, &bx2, &by2)
            if bx1 < self.x1 or self.x1 == 0:
                self.x1=bx1
            if by1 < self.y1 or self.y1 == 0:
                self.y1= by1
            if bx2 > self.x2:
                self.x2=bx2
            if by2 > self.y2:
                self.y2=by2
            # add space after word if necessary
            if w.hasSpaceAfter():
                words.append(u' ')
                self._bboxes.append(BBox(last_bbox.x2, last_bbox.y1, last_bbox.x2, last_bbox.y2))
            w=w.getNext()
        self._text= u''.join(words)

    property bbox:
        def __get__(self):
            return BBox(self.x1,self.y1,self.x2,self.y2)

    property text:
        def __get__(self):
            return self._text

    property char_bboxes:
        def __get__(self):
            return self._bboxes
