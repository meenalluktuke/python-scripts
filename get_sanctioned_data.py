import urllib2
import time

date=time.strftime("%Y_%b_%d")

#UN Sanctioned List
url = 'https://scsanctions.un.org/resources/xml/en/consolidated.xml'

s=urllib2.urlopen(url)
contents=s.read()
fname="../data/sanctioned_un_"+date+"_.xml"
file=open(fname,'w')
file.write(contents)
file.close()

#US Sanctioned Consolidated List
url='https://www.treasury.gov/ofac/downloads/consolidated/consolidated.xml'

s=urllib2.urlopen(url)
contents=s.read()
fname="../data/sanctioned_consolidated_us_"+date+"_.xml"
file=open(fname,'w')
file.write(contents)
file.close()

#US SDN List
url='https://www.treasury.gov/ofac/downloads/sdn.xml'

s=urllib2.urlopen(url)
contents=s.read()
fname="../data/sanctioned_sdn_us_"+date+"_.xml"
file=open(fname,'w')
file.write(contents)
file.close()

#EU Sanctioned List
url='http://ec.europa.eu/external_relations/cfsp/sanctions/list/version4/global/global.xml'

s=urllib2.urlopen(url)
contents=s.read()
fname="../data/sanctioned_eu_"+date+"_.xml"
file=open(fname,'w')
file.write(contents)
file.close()
