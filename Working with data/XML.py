import xml.dom.minidom as md
import xml.sax as sa
import xml.sax

class SongHandler(sa.ContentHandler):

    def startElement(self, name, attributes):
        self.name = name
        if self.name == "song":
            print("ID: {}".format(attributes['id']))

    def characters(self, cont):
        if self.name == "title":
            self.name = cont
            print("\ttitle: {}".format(self.name))
        elif self.name == "artist":
            self.age = cont
            print("\ttitle: {}".format(self.age))

    def endElement(self, name):
        self.name = ""

def parse_function():
    xml_sax = sa.make_parser()
    handler = SongHandler()
    xml_sax.setContentHandler(handler)
    xml_sax.parse('songs.xml')

def dataChange_function():
    plik_xml = md.parse('songs.xml')

    songs = plik_xml.documentElement
    all_songs = songs.getElementsByTagName('song')

    idx = int(input("Wpisz nr piosenki do zmiany"))
    print("Before:")
    print(all_songs[idx-1].getElementsByTagName('title')[0].childNodes[0].data)

    new_tag = input("Nowy tutuł dla piosenki")
    all_songs[idx-1].getElementsByTagName('title')[0].childNodes[0].data = new_tag
   
    print("After:")
    print(songs.toxml())
    plik_xml.writexml(open('new_songs.xml', 'w'))

parse_function()
dataChange_function()