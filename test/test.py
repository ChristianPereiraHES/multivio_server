from multivio.poppler import _mypoppler as poppler
from PIL import Image
import io
# #
d = poppler._PDFDoc(('/code/multivio/test/examples/document.pdf').encode('utf-8'))
# # print('No of pages', d._getNumPages())
# p = d.get_page(1)
# # for p in d:
# print('Page', p.page_no, 'size =', p.size)
# for f in p:
#     print(' '*1, 'Flow')
#     for b in f:
#         print(' '*2, 'Block', 'bbox=', b.bbox.as_tuple())
#         for l in b:
#             print(' '*3, l.text.encode(), '(%0.2f, %0.2f, %0.2f, %0.2f)' % l.bbox.as_tuple())
#             #assert l.char_fonts.comp_ratio < 1.0
#             for i in range(len(l.text)):
#                 print(l.text[i].encode(), '(%0.2f, %0.2f, %0.2f, %0.2f)' %
#                       l.char_bboxes[i].as_tuple())
#             print()
# print("Bingo2")
# import base64

content = '\x8fuZ\x8fuZ\x8etY\x8etY\x8dsX\x8dsX\x8crW\x8crW\x8cqV\x8cqV\x8cqV\x8cqV\x8drW\x8drW\x8esX\x8esX\x8ftY\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8ftY\x8fuZ\x8fuZ\x8fuZ\x8fuZ\x8fuZ\x8fuZ\x8fuZ\x8fuZ\x8fuZ\x8etY\x8etY\x8dsX\x8dsX\x8crW\x8crW\x8euW\x8fvX\x8fvX\x8fvX\x8fvX\x8fvX\x8fvX\x8fvX\x8fuX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x91v[\x92w\\\x92w\\\x92w\\\x92w\\\x92w\\\x92w\\\x92w\\\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uY\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8drW\x8drW\x8drW\x8drW\x8drW\x8drW\x8drW\x8drW\x8esW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x91sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x91uX\x91vY\x91vY\x90uX\x90uX\x8ftW\x8ftW\x8ftW\x8drW\x8drW\x8drW\x8esX\x8esX\x8ftY\x8ftY\x90uZ\x8drW\x8drW\x8drW\x8drW\x8drW\x8drW\x8drW\x8drW\x8drU\x8drU\x8drU\x8esV\x8esV\x8ftW\x8ftW\x90uX\x90uY\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x90uX\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x91sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x93tX\x93tX\x94uY\x94uY\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x90tY\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x90uZ\x92tX\x93tX\x93tX\x93tX\x93tX\x93tX\x93tX\x93tX\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x93tX\x93tX\x94uY\x94uY\x92rY\x92rY\x92rY\x92rY\x92rY\x92rY\x92rY\x92rY\x92rW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x91rV\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x90qU\x90qU\x90qU\x91rV\x91rV\x92sW\x92sW\x93tX\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x91rV\x91rV\x91rV\x90qU\x90qU\x8fpT\x8fpT\x8fpT\x8fpT\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x91rV\x91rV\x92sW\x92sW\x93tX\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x90qU\x90qU\x90qU\x91rV\x91rV\x92sW\x92sW\x93tX\x93tX\x93tX\x92sW\x92sW\x91rV\x91rV\x90qU\x90qU\x90pV\x90pW\x90pW\x90pW\x90pW\x90pW\x90pW\x90pW\x90pU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x8fpT\x8fpT\x8fpT\x8fpT\x90qU\x90qU\x91rV\x91rV\x8fsV\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x92tW\x93tX\x92sW\x92sW\x91rV\x91rV\x90qU\x90qU\x8fsV\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x92tW\x93tX\x92sW\x92sW\x91rV\x91rV\x90qU\x90qU\x91rV\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x91rV\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x90qU\x90qU\x90qU\x91rV\x91rV\x92sW\x92sW\x93tX\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x92sW\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x91rV\x91rV\x90qU\x90qU\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x91rV\x91rV\x90qU\x90qU\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x90qU\x8fpT\x8fpT\x8eoS\x8eoS\x8dnR\x8dnR\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8eoS\x8fpT\x90qU\x91rV\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x91rV\x91rV\x90qU\x90qU\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x90qU\x90qU\x91rV\x91rV\x8fsV\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8ftW\x8fqU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qU\x90qR\x90qR\x90qR\x90qR\x90qR\x90qR\x90qR\x90qR\x90qT\x91rV\x91rV\x90qU\x90qU\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x90qU\x90qU\x91rV\x91rV\x8eoS\x8dnR\x8dnR\x8eoS\x8eoS\x8fpT\x8fpT\x90qU\x8fpT\x8fpT\x8fpT\x8fpT\x90qU\x90qU\x91rV\x91rV\x91rV\x91rV\x91rV\x90qU\x90qU\x8fpT\x8fpT\x8fpT\x8cpT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8eqT\x90qU\x8fpT\x8fpT\x8eoS\x8eoS\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8eoS\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8dpT\x8cqT\x8cqT\x8cqT\x8drU\x8drU\x8esV\x8esV\x8fqV\x90pW\x8foV\x8foV\x8enU\x8enU\x8dmT\x8dmT\x8eoT\x90qU\x8fpT\x8fpT\x8eoS\x8eoS\x8dnR\x8dnR\x8eoS\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8dnR\x8dnR\x8dnR\x8eoS\x8eoS\x8fpT\x8fpT\x90qU\x8eoS\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8bnS\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8bmT\x8dmT\x8dmT\x8enU\x8enU\x8foV\x8foV\x90pW\x8dpU\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8dpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8cpT\x8bpU\x8bpU\x8aoT\x8aoT\x89nS\x89nS\x89nS\x89nQ\x89nQ\x89nQ\x89nQ\x8aoR\x8aoR\x8bpS\x8bpS\x8cqT\x8drU\x8cqT\x8cqT\x8bpS\x8bpS\x8aoR\x8aoR\x8bpT\x8cqV\x8cqV\x8cqV\x8cqV\x8cqV\x8cqV\x8cqV\x8epV\x8foV\x8foV\x8enU\x8clS\x8bkR\x8bkR\x8ajQ\x88kQ\x87lQ\x87lQ\x88mR\x88mR\x89nS\x89nS\x8aoT\x8bmS\x8clS\x8clS\x8clS\x8dmT\x8dmT\x8enU\x8enU\x8cmR\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dmS\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8eoS\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8dpT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoS\x8bpU\x8bpU\x8aoT\x8aoT\x89nS\x89nS\x89nS\x8amQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8boS\x8aoT\x89nS\x89nS\x88mR\x88mR\x87lQ\x87lQ\x88kO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8blP\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x89lP\x87lO\x87lO\x88mP\x88mP\x89nQ\x89nQ\x8aoR\x8aoR\x8bpS\x8bpS\x8aoR\x8aoR\x89nQ\x89nQ\x89nQ\x8amQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8coR\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8aoR\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nR\x89nS\x89nS\x89nS\x89nS\x89nS\x89nS\x89nS\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x8bmR\x8dmT\x8clS\x8clS\x8bkR\x8bkR\x8ajQ\x8ajQ\x8ajQ\x8clS\x8clS\x8clS\x8clS\x8clS\x8clS\x8clS\x8alR\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x8amQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8bmR\x8aoT\x8aoT\x8bpU\x8bpU\x8cqV\x8cqV\x8drW\x8aoT\x87lQ\x87lQ\x88mR\x88mR\x89nS\x89nS\x8aoT\x8aoT\x8bpU\x8bpU\x8aoT\x8aoT\x89nS\x89nS\x89nS\x8anR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8bnQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nR\x8aoT\x8aoT\x8bpU\x8bpU\x8cqV\x8cqV\x8drW\x8drW\x8drW\x8cqV\x8cqV\x8bpU\x8bpU\x8aoT\x8aoT\x89nR\x89nQ\x89nQ\x89nQ\x8aoR\x8aoR\x8bpS\x8bpS\x8amQ\x8akO\x8akO\x8blP\x8blP\x8cmQ\x8cmQ\x8dnR\x8bnR\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x88mR\x87lQ\x87lQ\x87lQ\x87lQ\x87lQ\x87lQ\x87lQ\x87lQ\x89nS\x89nS\x89nS\x8aoT\x8aoT\x8bpU\x8bpU\x8aoS\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8cqT\x8coR\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8cmQ\x8cmQ\x8blP\x8blP\x8akO\x8akO\x8akO\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8dnR\x8dnR\x8cmQ\x8cmQ\x8blP\x8blP\x8akO\x8akO\x8blP\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8enT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8cnS\x8bpS\x8bpS\x8aoR\x8aoR\x89nQ\x89nQ\x89nQ\x8amQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8enS\x8enU\x8enU\x8dmT\x8dmT\x8clS\x8clS\x8clS\x8bmS\x8aoT\x89nS\x89nS\x88mR\x88mR\x87lQ\x87lQ\x88lQ\x8clS\x8clS\x8clS\x8clS\x8clS\x8clS\x8clS\x8dmT\x8foV\x8foV\x8foV\x8foV\x8foV\x8foV\x8foV\x8epV\x8drW\x8cqV\x8cqV\x8bpU\x8bpU\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoS\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x8bpS\x8bpS\x8aoR\x8aoR\x89nQ\x89nQ\x89nQ\x89nQ\x89nS\x89nS\x89nS\x89nS\x89nS\x89nS\x89nS\x8amS\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8bmS\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x8amQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8cmQ\x8cmQ\x8blP\x8blP\x8akO\x8akO\x8akP\x8clS\x8clS\x8clS\x8clS\x8clS\x8clS\x8clS\x8bmS\x8bpS\x8bpS\x8aoR\x8aoR\x89nQ\x89nQ\x89nQ\x89mP\x8akO\x8akO\x8blP\x8blP\x8cmQ\x8cmQ\x8dnR\x8bnQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89mQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8bmQ\x8aoT\x8aoT\x8bpU\x8bpU\x8cqV\x8cqV\x8drW\x8drV\x8drU\x8cqT\x8cqT\x8bpS\x8bpS\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8bpU\x8bpU\x8aoT\x8aoT\x89nS\x89nS\x89nS\x89mR\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8blP\x8blP\x8blP\x8akO\x8akO\x89jN\x89jN\x89jN\x89jN\x89jN\x89jN\x89jN\x8akO\x8akO\x8blP\x8blP\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8ajO\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8dnS\x8clS\x8clS\x8clS\x8clS\x8clS\x8clS\x8clS\x8alR\x87lQ\x87lQ\x88mR\x88mR\x89nS\x89nS\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8anS\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8cnR\x8bpU\x8bpU\x8aoT\x8aoT\x89nS\x89nS\x89nS\x89nS\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoT\x8aoS\x8aoR\x89nQ\x89nQ\x88mP\x88mP\x87lO\x87lO\x88lO\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8eoS\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8eoS\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8bmQ\x89nQ\x89nQ\x89nQ\x8aoR\x8aoR\x8bpS\x8bpS\x8boR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8cnR\x8aoR\x89nQ\x89nQ\x88mP\x88mP\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x87lO\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8bmQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89mQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8blP\x8akO\x8akO\x8blP\x8blP\x8cmQ\x8cmQ\x8dnR\x8cmR\x8clS\x8clS\x8clS\x8dmT\x8dmT\x8enU\x8enU\x8enT\x8eoS\x8eoS\x8dnR\x8dnR\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8cnR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8anR\x8dnR\x8cmQ\x8cmQ\x8blP\x8blP\x8akO\x8akO\x8akO\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8blP\x8akO\x8akO\x8blP\x8blP\x8cmQ\x8cmQ\x8dnR\x8dmR\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8dmT\x8cmS\x89nS\x89nS\x89nS\x89nS\x89nS\x89nS\x89nS\x89nS\x8bpS\x8bpS\x8aoR\x8aoR\x89nQ\x89nQ\x89nQ\x89mQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8blP\x8akO\x8akO\x8blP\x8blP\x8cmQ\x8cmQ\x8dnR\x8cnR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8anQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8bmQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89nQ\x89mP\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x89kO\x87lO\x87lO\x88mP\x88mP\x89nQ\x89nQ\x8aoR\x8anQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8ajQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8blP\x87lO\x87lO\x88mP\x88mP\x89nQ\x89nQ\x8aoR\x8anQ\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8blP\x8akO\x8akO\x8blP\x8blP\x8cmQ\x8cmQ\x8dnR\x8dnR\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8fpT\x8eoS\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8dnR\x8dnR\x8cmQ\x8cmQ\x8blP\x8blP\x8akO\x8akO\x8akO\x8akO\x8akO\x8blP\x8blP\x8cmQ\x8cmQ\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8cmQ\x8cmQ\x8blP\x8blP\x8akO\x8akO\x8akO\x8blP\x8blP\x8akO\x8akO\x89jN\x89jN\x89jN\x89jN\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8bmQ\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8anR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8dnR\x8cmQ\x8cmQ\x8cmQ\x8cmQ\x8dnR\x8dnR\x8eoS\x8eoS\x8doR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8aoR\x8anQ\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8akO\x8fpQ\x8fpQ\x8fpQ\x90qR\x90qR\x91rS\x91rS\x90rS\x86u[\x8bz`\x84sY'


# print(cont)
im = d.get_image(1)
print("Scale:")
print(im._getScale())
new_width = im._getWidth()
new_height = im._getHeight()
image_data = im._getBitmap()
print(new_width)
print(new_height)
print(image_data)
print(type(image_data))
pil = Image.frombytes('RGB', (new_width, new_height), image_data)
temp_file = io.BytesIO()
pil.save(temp_file, "JPEG", quality=90)
temp_file.seek(0)
content = temp_file.read()
