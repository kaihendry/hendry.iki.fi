#!/usr/bin/python
# Gauge - For recording of hit/miss or 1/0 scoring!
# Visit URL: http://www.cs.helsinki.fi/u/hendry/content/gauge/

from snack import *
from time import *
from pickle import *
import getopt, sys, string

rev = '$Revision: 1.2 $'
rev = string.join(filter(lambda s: '$' not in s, string.split(rev)))

def player_menu(shooters):
	"""
	The Main Menu GUI
	"""
	screen = SnackScreen()
	
	li = Listbox(height = 4, width = 20)
	#print "Shooters: " + `shooters`
	#print "Length Shooters: " + `len(shooters)`
	count = 0	
	for shooter in shooters:
		#print "Shooter: " + `shooter`
		#print "Length Shooter: " + `len(shooter)`
		if shooter != '':
			li.append(`count+1` + ": " + shooter[0], count)
			count = count + 1

	bb = ButtonBar(screen, (("Info", "info"), ("Shoot!", "shoot"),("Add", "add"), ("Quit", "quit")))

	g = GridForm(screen, "GAUGE! " + rev, 1, 9)
	g.add(li, 0, 0)
	g.add(bb, 0, 3)

	result = g.runOnce()

	screen.finish()

	if shooters != '':
		selection = li.current() 
	else: 	selection = -1
	print "listbox:", selection
	status = bb.buttonPressed(result)
	print "bb:", status
	return (selection, status)


def player_add():
	""" 
	Returns a name if there was one entered 
	"""

	screen = SnackScreen()
	addprompt = EntryWindow(screen, 'Add shooter', 'Please enter the full name of the shooter',
	            ['Name'])
	screen.finish()
	print addprompt 
	prompt = addprompt[0]
	name = addprompt[1]
	name = name[0]
	print "Prompt: " + `prompt`
	print "Name: " + `name`
	if name != '' and prompt != 'cancel':
		return name


def menu(shooters):
	"""
	The main menu control
	"""
	while 1:
		result = player_menu(shooters)
		print result
		selection = result[0]
		status = result[1]
		print "Selection: " + `selection`
		print "Status: " + `status`
		if status == 'shoot' and selection != -1:
			shooter = shooters[selection]
			newscore = letshoot(shooter)
			print "Current record: " + `shooter`
			print "After a day shooting: " + `newscore`
			if newscore != 0:
				shooter.insert(1, newscore)
			print "Appended: " + `shooter`
		if status == 'quit':
			prompt = areyousure()
			if prompt == 'ok':
				return shooters
		if status == 'info' and selection != -1 and len(shooters[selection]) > 1:
			# print shooters[selection]
			# print len(shooters[selection])
			# sleep(2)
			info_view(shooters[selection])
		if status == 'add':
			name = player_add()
			print 'Shooters: ' + `shooters`
			if name != None:
				if shooters == '':
					shooters = ([[name]])
				else: shooters[:0] = ([[name]])
				print 'Shooters: ' + `shooters`
			


def info_view(shooter):
	"""
	Displays detailed statistics 
	"""

	text = '-'*50 + "\n"

	i = len(shooter)-1
	while i > 0:
		text += `shooter[i][0]` + ":(" + ctime(shooter[i][1]) + "):"
		text += '%2d %2d %2d' % (hitno(shooter[i][2]), missno(shooter[i][2]), totalno(shooter[i][2]))
		text += ' %3d' % (int(average(shooter[i][2])*100)) + "%" + "\n"
		i = i - 1	

	text += '-'*50 + "\n"


	totalstats = crazyhorse(shooter)

	text += '%31d %2d %2d %3d' % (totalstats[0], totalstats[1], totalstats[2], totalstats[3]*100 ) + "%"

	screen = SnackScreen()
	tb = Textbox(50, 20, text)
	bb = ButtonBar(screen, (["Ok"]))
	
	
	g = GridForm(screen, "Statistics for " + shooter[0], 1, 4)
	g.add (tb, 0, 0)
	g.add (bb, 0, 1)
	result = g.runOnce()
	
	screen.finish()

def crazyhorse(shooter):
	""" 
	A badly named function that returns overall/total hits, misses and average
	"""

	i = len(shooter)-1
	hit = 0
	miss = 0
	total = 0
	while i > 0:
		print "Shooter: " + `shooter[i]` + " i: " + `i`
		for score in shooter[i][2]:
			if score == 1:
				hit = hit + 1
			else: miss = miss + 1
			total = total + 1
		i = i - 1
	
	return (hit, miss, total, (float(hit)/(float(total))))
			

def totalno(scores):
	""" 
	Calculate total number of shots from a score
	"""
        total = 0 
	if len(scores) == 0: # if no scores avoid div by zero !
		return 0
        for score in scores:
		total = total + 1
        return total

def missno(scores):
	""" 
	Calculate number of misses
	"""
        total = 0 
	if len(scores) == 0: # if no scores avoid div by zero !
		return 0
        for score in scores:
		if score == 0:
	                total = total + 1
			print total
        return total


def hitno(scores):
	""" 
	Calculate number of hits
	"""
        total = 0 
	if len(scores) == 0: # if no scores avoid div by zero !
		return 0
        for score in scores:
		if score == 1:
	                total = total + 1
        return total

def average(scores):
	""" 
	Calculate average in scores data structure
	"""
        total = 0 
	if len(scores) == 0: # if no scores avoid div by zero !
		return 0
        for score in scores:
                total = total + score
        return (float(total)/float(len(scores)))


def areyousure():
	"""
	Little function to return an ok or cancel
	"""
	screen = SnackScreen()
	answer = ButtonChoiceWindow(screen, "Confirmation", "Are you sure?")
	screen.finish()
	print answer
	return answer

def letshoot(shooter):
	"""
	Function which handles data entry
	"""
	if len(shooter) > 1:
		sessionid = shooter[1][0] # Load previous sessionid
	else: sessionid = 0
	print "Session ID: " + `sessionid`	
	hits = []
	while 1:
		print shooter
		screen = SnackScreen()
	
		li = Listbox(height = 10, width = 25)
	
		count = 0
		if hits != []:
			for i in hits:
				if i == 1:
					text = 'Hit!'
				else:	text = 'Miss'
				li.append(`count+1` + ":" + "\t" + text, count)
				count = count + 1

		ab = ButtonBar(screen, (("Hit", "hit"), ("Miss", "miss"), ("Delete", "del"), ("Quit", "quit")))

		g = GridForm(screen, "Session " + `sessionid+1` + " Enter the score for " + shooter[0], 1, 9 )
		g.add(ab, 0, 0)
		g.add(li, 0, 2)
		# g.setCurrent(screen)
		result = g.runOnce()

		screen.finish()
		if hits != []:
			selection = li.current() 
		else: 	selection = -1

		print "listbox:", selection
		status = ab.buttonPressed(result)
		print "ab:", status

		if status == 'quit':
			if hits != []:
				return ([sessionid+1, time(), hits])
			else: return 0
		if status == 'hit':
			hits[:0] = [1]
		if status == 'miss':
			hits[:0] = [0]
		if status == 'del' and selection != -1:
			prompt = areyousure()
			if prompt == 'ok':
				hits.pop(selection)



def generate_html(shooters, filename):
	"""
	Generates XHTML for publishing on a website or printing
	"""
	try:
	    f = open(filename, 'w')
	except IOError, (errno, strerror):
	    print "I/O error(%s): %s" % (errno, strerror)
	except:
	    print "Unexpected error:", sys.exc_info()[0]
	    raise

	header = """
	<?xml version="1.0" encoding="iso-8859-1"?>
			 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

	<html xml:lang="en">

	<head>
	  <meta name="author" content="Kai Hendry" />
	  <meta name="copyright" content="&copy; copyright 2002 by Kai Hendry" />
	  <meta http-equiv="Content-Type" name="Content-Type" content="text/html; charset=ISO-8859-1" />
	  <link rev="made" href="mailto:gauge@n0spam.dabase.com" />
	  <style type="text/css">
            body { font-family: verdana, arial, sans-serif; background: white; color: black; }    
	    table { border: solid;}
	    td.total { font-weight: bold; }
	    td { text-align: center; }
	    td.name { text-align: left; font-weight: bold; }
            th { text-align: left; font-weight: bold;}
	    h1 {
	        text-align: center;
                text-decoration: none;
                border: solid;
                }

     	    :link, :visited { text-decoration: none; }
            :link:hover, :visited:hover { text-decoration: underline; }  
            :link:active, :visited:active,
            :link:focus, :visited:focus,
            :link:hover, :visited:hover { outline: none; }   
            .footer { 	border-top: thin solid;
			font-size: 1em;
                        text-align: right; 
			margin-top: 10px;
	                }	
	  </style>

	"""

	title = "<title>Gauge - " + ctime(time()) + "</title>\n\n"

	h1 = """
	</head>
    <body>
        <h1>Shooting statistics</h1>
        <div class="main">
        <table>
                <tr>
                <th>Name</th>
"""
	
	sessionno = maxsessions(shooters)
	print sessionno	
	for i in range(1,sessionno+1):
		h1 += "\t\t<th>Stand " + `i` + "</th>\n"
	h1 += "\t\t<th class=\"total\">Total</th>\n"
	h1 += "\n\t</tr>\n"

	for shooter in shooters:
		total = 0
		h1 += "\n\t\t<tr>\n\n\t\t<td class=\"name\">" + shooter[0] + "</td>\n"
		sessions = len(shooter)
		shesh = range(1,sessions)
		shesh.reverse()	
		for i in shesh:
			#print '-'*50
			#print shooter
			#print '*'*50
			#print shooter[i]
			#print '_'*50
			#print shooter[i][2]
			entry = (hitno(shooter[i][2]))
			total += entry
			h1 += "\t\t<td>" + `entry` + "</td>\n"
		#print "This shooter's sessions: " + `sessions-1` + "\tMax sessions: " + `sessionno`
		if sessions-1 < sessionno:
			# print "HIT!!! : " + `(sessionno-(sessions-1))`
			h1+= "\t\t<td>-</td>\n"*(sessionno-(sessions-1))
		h1 += "\n\t\t<td class=\"total\">" + `total` + "</td>\n"
		h1 += "\n\t\t</tr>\n"


	end = """
        </table>
        </div>

        <div class="footer">
        Produced by Gauge """
	
	end += rev # hmmm, is there a better way of doing this?
	
	end += """. Visit Gauge's homepage at:<br />
        <a href="http://www.cs.helsinki.fi/u/hendry/content/gauge/">
        http://www.cs.helsinki.fi/u/hendry/content/gauge/</a>

    </body>
</html>
"""

	f.write(header)
	f.write(title)
	f.write(h1)
	f.write(end)
	print f
	f.close


def maxsessions(shooters):
	"""
	Discovers the highest number of sessions/stands between all shooters
	"""
	max = 0
	#print '-'*65
	for shooter in shooters:
		length = len(shooter)
		#print `shooter` + "\n"
		#print "Length: \t" + `length` + "\n"
		if max < length:
			max = length
		#print "Max: \t" + `max` + "\n"
	return max-1

def usage():
	"""
	Prints usage help
	"""
	print
	print '*'*15 + ' Gauge Help ' + '*'*15
	print
	print "-h or --help \t This help message"
	print "-o or --output \t Specify report output file, Default: gauge.html"
	print "-s or --scores \t Specify scores file, where scores are read and saved, Default: gauge_scores"
	print
	print "Example usage: ./gauge.py -s ~/oldscores --output ~/public_html/gauge_day2.html"
	print
	print "Author: gauge@dabase.com, License: GPL, Version: " + rev
	print

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "ho:s:", ["help", "output=", "scores="])
	except getopt.GetoptError:
		# print help information and exit:
		usage()
		sys.exit(2)

	output = None
	scores = None
	    
	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
		if o in ("-s", "--scores"):
			scores = a
		if o in ("-o", "--output"):
			output = a
	
	openfile = 0

	# If no options given, set defaults
	if scores == None:
		scores = 'gauge_score'
	if output == None:
		output = 'gauge.html'

	# try to read in previous scores
	try:
	    f = open(scores, 'r+')
	    shooters = load(f)
	    openfile = 1
	except IOError, (errno, strerror):
	    print "I/O error(%s): %s" % (errno, strerror)
	except:
	    print "Unexpected error:", sys.exc_info()[0]
	    raise

	# else create a new file

	if openfile == 0:
		# create a new file
		print "Creating a new file named: " + scores
		sleep(1)
		f = open(scores, 'w')
		shooters = ''
	else: f = open(scores, 'w')

	print "Openfile: " + `openfile`
	print "Shooters: " + `shooters`

	record = menu(shooters)
	print "Final Record: " + `record`
	dump(record,f)
	print f
	f.close
	generate_html(record, output)

	print "Output: " + `output`
	print "Scores: " + `scores`

main()	
