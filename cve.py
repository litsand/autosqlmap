try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='cve.xml')
root = tree.getroot()
# print root.tag 
# print root.attrib
# for cvenode in root.findall("cvrfdoc/Vulnerability"):
# 	print cvenode.text
print root.tag

vulnode_all = root.findall('{http://www.icasi.org/CVRF/schema/vuln/1.1}Vulnerability')

for vulnode in vulnode_all:
	osvdb =''
	cve = vulnode.find('{http://www.icasi.org/CVRF/schema/vuln/1.1}CVE').text
	try:
		refernode_all = vulnode.find('{http://www.icasi.org/CVRF/schema/vuln/1.1}References').findall('{http://www.icasi.org/CVRF/schema/vuln/1.1}Reference')
		for refernode in refernode_all:
			desc = refernode.find('{http://www.icasi.org/CVRF/schema/vuln/1.1}Description').text

			if desc.startswith('OSVDB'):
				print cve+","+desc
				# osvdb = desc+','+osvdb
		# print osvdb
		# if len(osvdb) > 2:

		# 	print cve+","+osvdb		
			# 	pass
			# print refernode.find('{http://www.icasi.org/CVRF/schema/vuln/1.1}Description').text
	except Exception, e:
		pass
	# refernode_all = vulnode.find('{http://www.icasi.org/CVRF/schema/vuln/1.1}References').findall('{http://www.icasi.org/CVRF/schema/vuln/1.1}Reference')
	# for refernode in refernode_all:
	# 	print refernode.find('{http://www.icasi.org/CVRF/schema/vuln/1.1}Description').text
		
# print type(vulnode)

# for elem in tree.iter():
# 	print elem.tag
# for vul in vulnode:
# 	print vul.find('Title').text
# 	print vul.findall('Reference').findall('Description').text

# print cvenode
# for child in root:
# 	print child.tag,




