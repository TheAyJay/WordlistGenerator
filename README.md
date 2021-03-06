# WordlistGenerator
There are lots of common password lists available online, but I wanted to code a solution that allows you to input custom keywords to create a stronger password list. The intent is to feed the custom list into Aircrack-ng on Kali Linux to find the password. 

If you have deauthenticated a user/connection already and captured the handshake using the Aircrack-ng suite, then you can run through your wordlists offline to crack the password. For example, if I wanted to discover the password for a local coffeeshop named Joe's Java, I might create a keyword list like this:

coffee, joe, java, bean

I'd then run my Python script with those keywords as input. My script takes those words and performs a variety of transformations to create an extensive password list. These transformations include substituting common numbers/symbols for characters (e.g. "e" becomes "3"), capitalizing every and all letters, and appending common number and symbols to the front and end of the word. It then peforms the various combinations of those iterations:

- capitalization with numbers
- capitalization with symbols
- capitalization with substitutions
- capitalization with numbers with symbols
- capitalization with symbols with numbers
- capitalization with substitutions with numbers
- capitalization with substitutions with symbols
- capitalization with substitutions with numbers with symbols
- capitalization with substitutions with symbols with numbers
- substitutions
- substitutions with numbers
- substitutions with symbols
- substitutions with numbers with symbols
- substitutions with symbols with numbers
- numbers
- numbers with symbols
- symbols
- symbols with numbers

At the moment, my script would take the word "coffee" and generate 12,502 possible passwords. The first 300 passwords generated from the keyword "coffee":

coffee
Coffee
cOffee
coFFee
coffEE
COFFEE
c0ffee
coff3e
coff33
coffe3
coffee123
123coffee
coffee234
234coffee
coffee345
345coffee
coffee456
456coffee
coffee567
567coffee
coffee678
678coffee
coffee789
789coffee
coffee890
890coffee
coffee321
321coffee
coffee432
432coffee
coffee534
534coffee
coffee654
654coffee
coffee765
765coffee
coffee876
876coffee
coffee987
987coffee
coffee098
098coffee
coffee1234
1234coffee
coffee2345
2345coffee
coffee3456
3456coffee
coffee4567
4567coffee
coffee5678
5678coffee
coffee6789
6789coffee
coffee7890
7890coffee
coffee4321
4321coffee
coffee5432
5432coffee
coffee6543
6543coffee
coffee7654
7654coffee
coffee8765
8765coffee
coffee9876
9876coffee
coffee0987
0987coffee
coffee12345
12345coffee
coffee54321
54321coffee
coffee123456
123456coffee
coffee654321
654321coffee
coffee69
69coffee
coffee420
420coffee
coffee00
00coffee
coffee000
000coffee
coffee11
11coffee
coffee111
111coffee
coffee22
22coffee
coffee222
222coffee
coffee!
coffee!!
coffee!!!
coffee!@
coffee!@#
Coffee123
Coffee123!
Coffee123!!
Coffee123!!!
Coffee123!@
Coffee123!@#
123Coffee
123Coffee!
123Coffee!!
123Coffee!!!
123Coffee!@
123Coffee!@#
Coffee234
Coffee234!
Coffee234!!
Coffee234!!!
Coffee234!@
Coffee234!@#
234Coffee
234Coffee!
234Coffee!!
234Coffee!!!
234Coffee!@
234Coffee!@#
Coffee345
Coffee345!
Coffee345!!
Coffee345!!!
Coffee345!@
Coffee345!@#
345Coffee
345Coffee!
345Coffee!!
345Coffee!!!
345Coffee!@
345Coffee!@#
Coffee456
Coffee456!
Coffee456!!
Coffee456!!!
Coffee456!@
Coffee456!@#
456Coffee
456Coffee!
456Coffee!!
456Coffee!!!
456Coffee!@
456Coffee!@#
Coffee567
Coffee567!
Coffee567!!
Coffee567!!!
Coffee567!@
Coffee567!@#
567Coffee
567Coffee!
567Coffee!!
567Coffee!!!
567Coffee!@
567Coffee!@#
Coffee678
Coffee678!
Coffee678!!
Coffee678!!!
Coffee678!@
Coffee678!@#
678Coffee
678Coffee!
678Coffee!!
678Coffee!!!
678Coffee!@
678Coffee!@#
Coffee789
Coffee789!
Coffee789!!
Coffee789!!!
Coffee789!@
Coffee789!@#
789Coffee
789Coffee!
789Coffee!!
789Coffee!!!
789Coffee!@
789Coffee!@#
Coffee890
Coffee890!
Coffee890!!
Coffee890!!!
Coffee890!@
Coffee890!@#
890Coffee
890Coffee!
890Coffee!!
890Coffee!!!
890Coffee!@
890Coffee!@#
Coffee321
Coffee321!
Coffee321!!
Coffee321!!!
Coffee321!@
Coffee321!@#
321Coffee
321Coffee!
321Coffee!!
321Coffee!!!
321Coffee!@
321Coffee!@#
Coffee432
Coffee432!
Coffee432!!
Coffee432!!!
Coffee432!@
Coffee432!@#
432Coffee
432Coffee!
432Coffee!!
432Coffee!!!
432Coffee!@
432Coffee!@#
Coffee534
Coffee534!
Coffee534!!
Coffee534!!!
Coffee534!@
Coffee534!@#
534Coffee
534Coffee!
534Coffee!!
534Coffee!!!
534Coffee!@
534Coffee!@#
Coffee654
Coffee654!
Coffee654!!
Coffee654!!!
Coffee654!@
Coffee654!@#
654Coffee
654Coffee!
654Coffee!!
654Coffee!!!
654Coffee!@
654Coffee!@#
Coffee765
Coffee765!
Coffee765!!
Coffee765!!!
Coffee765!@
Coffee765!@#
765Coffee
765Coffee!
765Coffee!!
765Coffee!!!
765Coffee!@
765Coffee!@#
Coffee876
Coffee876!
Coffee876!!
Coffee876!!!
Coffee876!@
Coffee876!@#
876Coffee
876Coffee!
876Coffee!!
876Coffee!!!
876Coffee!@
876Coffee!@#
Coffee987
Coffee987!
Coffee987!!
Coffee987!!!
Coffee987!@
Coffee987!@#
987Coffee
987Coffee!
987Coffee!!
987Coffee!!!
987Coffee!@
987Coffee!@#
Coffee098
Coffee098!
Coffee098!!
Coffee098!!!
Coffee098!@
Coffee098!@#
098Coffee
098Coffee!
098Coffee!!
098Coffee!!!
098Coffee!@
098Coffee!@#
Coffee1234
Coffee1234!
Coffee1234!!
Coffee1234!!!
Coffee1234!@
Coffee1234!@#
1234Coffee
1234Coffee!
1234Coffee!!

This project was done purely for fun and curiosity's sake.
