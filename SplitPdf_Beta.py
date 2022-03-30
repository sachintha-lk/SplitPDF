#!/usr/bin/env python3.8
try:
    from PyPDF2 import PdfFileReader, PdfFileMerger,PdfFileWriter
    import webbrowser, time
except Exception as e1:
    print("Unable to import modules or ", e1)

print("PDF Spliter for Canon LBP6030 Duplex print".center(50, " "))
print("Beta edition".center(50, " "))
print("Print order \n 1) pdfSplit1.pdf \n 2) pdfSplit2.pdf")

try:
    pdfLocation = input('Type the location of the pdf to split')

    # opening the relevent pdf files
    pdfFileOriginal = open(pdfLocation , "rb")
    pdfDotFile = open("dot.pdf", "rb")              #   The dot to replace blank pages
    pdfSplitFile1 = open( "pdfSplit1.pdf", "wb")    #   Even pages are added in reverse order to this file
    pdfSplitFile2 = open("pdfSplit2.pdf", "wb")     #   Odd pages are added to this file

    pdfReaderOriginal = PdfFileReader(pdfFileOriginal)  # The orignal file is read
    pdfReaderDot = PdfFileReader(pdfDotFile)            # dot file is read
    pdfWriter1 = PdfFileWriter()                        # where odd pages are temp stored
    pdfWriter2 = PdfFileWriter()                        # where even pages are temp stored

    dot_pg_watermark = pdfReaderDot.getPage(0)

    num_of_pages = pdfReaderOriginal.numPages

    #spliting even pages in reverse order
    for pageRev in reversed(range(num_of_pages)):
        if (pageRev + 1) % 2 == 0:      #check pg is even
            pageObj1 = pdfReaderOriginal.getPage(pageRev)
            char_in_page = len(pageObj1.extractText().strip())   # Find the num of characters in the page after striping spaces should be zero if blank, but PyPDF2 gives zero for some pgs with text
            if char_in_page == 0:
                pageObj1.mergePage(dot_pg_watermark)          #Add the dot as a watermark for blank pages
                print("Blank Pg detected, watermark added split 1")
            pdfWriter1.addPage(pageObj1)

        # spliting odd pages
    for page in range(num_of_pages):
        if (page + 1) % 2 != 0:      #check pg is odd
            pageObj2 = pdfReaderOriginal.getPage(page)
            char_in_page = len(pageObj2.extractText().strip())  # Find the num of characters in the page after striping spaces should be zero if blank, but PyPDF2 gives zero for some pgs with text
            if char_in_page == 0:
                pageObj2.mergePage(dot_pg_watermark)          #Add the dot as a watermark for blank pages
                print("Blank Pg detected, watermark added split 2")
            pdfWriter2.addPage(pageObj2)

        # writing to the files
    pdfWriter1.write(pdfSplitFile1)
    pdfWriter2.write(pdfSplitFile2)

    # closing opened files
    for f in [pdfSplitFile1,pdfSplitFile2,pdfDotFile,pdfFileOriginal]:
        f.close()

    print("Done!!".center(30))
    print("REMEMBER:  Print order \n 1) pdfSplit 1.pdf \n 2) pdfSplit 2.pdf")


except Exception as e2:
    print(e2)
    user_exit = input("Press any key to exit")

try:
    webbrowser.open_new(r"file://E:\Users\Sachintha\Downloads\pdfSplit2.pdf")
    time.sleep(1.25)
    webbrowser.open_new(r"file://E:\Users\Sachintha\Downloads\pdfSplit1.pdf")

except Exception as e3:
    print(e3)
    print('Error opening splitpdf1 and 2 OR Error e3' , e3)
    user_exit = input("Press any key to exit")
