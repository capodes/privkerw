import urllib, re

class Alexa:
    def getSitesByCategoryAndPageNumber(self, category, page_number):
        url = "http://www.alexa.com/topsites/category;%s/Top/%s" % (page_number, category)
        result = urllib.urlopen(url).read()
        matches = re.findall(r"<h2><a href=\"\/siteinfo\/(.*)\">.*<\/a><\/h2>", result)

        return matches