template = """<div class="w3-card-2 w3-quarter w3-margin cast-card bloody">
  <header class="w3-container">
    <h3>{name}</h3>
  </header>
  <div class="w3-container">
    <p> {role}</p>
  </div>
</div>
"""

cast_positions = """Margo
Mingus
Samantha
Parker
Carla
Luna"""

cast_names = """Brenda Wooley
Aldo B.
Nikki Green
Michael Curry
Natalie Kelly
Courtney Land"""

print """<div class="w3-container" > <h3 class="w3-wide">Cast</h3>"""
cast_pairs = zip(cast_names.split("\n"), cast_positions.split("\n"))
for name, position in cast_pairs:
    print(template.format(name=name, role=position))

print "</div>"


crew_positions = """Director
Producer
Executive Producer
Writer/Screenplay
1st AD
Director of Photography
1st AC
2nd AC
Gaffer
Key Grip
Sound Op
Boom Op
Key MUA
BTS Photography
PA 1
PA 2
PA 3
Editor
Composer 1
Composer 2
Composer 3
Craft Services"""

crew_names = """Brian "Sham" Green
Aldo Billingslea
Wm. Derek Grasty
Wm. Derek Grasty
Jay Raja
Gavin Murray
Ferguson Rogan
Stephen Bartlett
Ryan Nelson
Kat.
Adam Drakewolf
Steven Lagosh
Whittany Robinson
Nathan Adams
Lee Harold
Skylar Adams
Thomas Ariniello
Brian Green
Peder B Helland
Vidal Garcia
Derek Thomas
Grasty Family"""

print """<div class="w3-container" > <h3 class="w3-wide">Crew </h3>"""

crew_pairs = zip(crew_positions.split("\n"), crew_names.split("\n"))
for name, position in crew_pairs:
    print(template.format(name=name, role=position))

print "</div>"
