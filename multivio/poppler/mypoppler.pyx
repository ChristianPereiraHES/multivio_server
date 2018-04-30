from libcpp cimport *
from libcpp.string cimport string
from cpython cimport bool as PyBool
from cpython.object cimport Py_EQ, Py_NE
from cpython.ref cimport PyObject
import multivio


ctypedef bool GBool
ctypedef unsigned char Guchar
ctypedef unsigned short Gushort
ctypedef unsigned int Guint
ctypedef unsigned long Gulong
ctypedef long long Goffset
ctypedef Guchar SplashColor[4]
ctypedef Guchar *SplashColorPtr

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

cdef extern from "cpp/poppler-version.h" namespace "poppler":
    cdef string version_string()

def poppler_version():
    return version_string()

cdef extern from "GlobalParams.h":
    GlobalParams *globalParams
    cdef cppclass GlobalParams:
        GBool getOverprintPreview()


cdef extern from "goo/GooString.h":
    cdef cppclass GooString:
        GooString(const char *sA)
        int getLength()
        char *getCString()
        char getChar(int i)

cdef extern from "OutputDev.h":
    cdef cppclass OutputDev:
        pass

cdef extern from "Catalog.h":
    cdef cppclass NameTree:
        pass
    cdef cppclass Catalog:
        pass

cdef extern from "Outline.h":
    cdef cppclass Outline:
        pass
    cdef cppclass OutlineItem:
        pass

cdef extern from 'Annot.h':
    cdef cppclass Annot:
        pass

cdef extern from 'XRef.h':
    cdef cppclass XRef:
        pass

cdef extern from 'Page.h':
    cdef cppclass Page:
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
        pass

cdef extern from 'splash/Splash.h':
    cdef cppclass Splash:
        pass

cdef extern from 'splash/SplashFontEngine.h':
    cdef cppclass SplashFontEngine:
        pass

cdef extern from 'Object.h':
    cdef cppclass Object:
        pass

cdef extern from "PDFDoc.h":
    cdef cppclass PDFDoc:
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


cdef extern from "TextOutputDev.h":
    cdef cppclass TextOutputDev:
        TextOutputDev(char *fileName, GBool physLayoutA,
          double fixedPitchA, GBool rawOrderA, GBool append)
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
        TextFontInfo *getFontInfo(int idx)
        GooString *getFontName(int idx)
        double getFontSize()
        void getColor(double *r, double *g, double *b)

    cdef cppclass TextFontInfo:
        GooString *getFontName()
        double getAscent()
        double getDescent()
        GBool isFixedWidth()
        GBool isSerif()
        GBool isSymbolic()
        GBool isItalic()
        GBool isBold()


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

def init():
  globalParams = new GlobalParams()
