import csv
import sys
import io

sys.stdout=open("braindance.html","w")

# begin the table
print("<table>")


infile = open("brainrave.csv","r")



for line in infile:
    row = line.split(",")
    pst = row[0]
    gmt = row [1]
    country = row[2]
    name = row[3]
    bandcamp = row[4]
    sc = row[5]
    ig = row[6]
    fb = row[7]
    twit = row[8]
    www = row[9]
    vis = row[10]
    vislink = row[11]

    print("<tr>")
    print("<td>%s</td>" % pst)
    print("<td>%s</td>" % gmt)
    print("<td><i %s.gif></td>" % country)
    print("<td>%s</td>" % name)
    print('<td><a href="%s" target="_blank"><i class="fa fa-bandcamp w3-hover-opacity"></i></a></td></td>' % bandcamp)
    print('<td><a href="%s" target="_blank"><i class="fa fa-soundcloud w3-hover-opacity"></i></a></td>' % sc)
    print('<td><a href="%s" target="_blank"><i class="fa fa-instagram w3-hover-opacity"></i></a></td>' % ig)
    print('<td><a href="%s" target="_blank"><i class="fa fa-facebook-official w3-hover-opacity"></i></a></td>' % fb)
    print('<td><a href="%s" target="_blank"><i class="fa fa-twitter w3-hover-opacity"></i></a></td>' % twit)
    print('<td><a href="%s" target="_blank">www</a></td>' % www)
    print('<td><a href="%s" target="_blank">' % vislink)
    print('%s</a></td>' % vis)

   #<a href="%s" target="_blank"><i class="fa fa-bandcamp w3-hover-opacity"></i></a></td>

    print("</tr>")

# end the table
print("</table>")
sys.stdout.close()
