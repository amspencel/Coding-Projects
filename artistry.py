
''' Purpose: demonstrate simple drawing commands '''

from PIL import Image, ImageDraw

def picture() :

    # replace dimensions and background as you see fit
    W  = 600
    H = 600

    DIMENSIONS = [ W, H]

    BACKGROUND_COLOR = "white"

    # create image of appropriate size
    im = Image.new( 'RGB', DIMENSIONS, BACKGROUND_COLOR )

    # get a drawable canvas of image im
    canvas = ImageDraw.Draw( im )

    # put your drawing commands here
    # ------------------------------
    r = 255
    g = 255
    b = 255
    #background color
    for y in range(0, H):
        for x in range( 0, W):
            coord = ( x, y)

            nr = max( 0, r + y // 6 )
            ng = max( 0, g + y // 6 )
            nb = max( 0, b + y // 2 )

            pixel = (nr, ng, nb)

            im.putpixel( coord, pixel )

    #Editted Polys
    p0 = (85, H - 431)
    p1 = (162, H - 483)
    p2 = (209, H - 486)
    p3 = (222, H - 479)
    p4 = (236, H - 434)
    p5 = (170, H - 365)
    poly = [p0, p1, p2, p3, p4, p5]
    p0 = (188, H - 496)
    p1 = (188, H - 484.5)
    p2 = (162, H - 483)
    poly2 = [p0, p1, p2]

    canvas.polygon(poly, fill='white')
    canvas.polygon(poly2, fill='white')


    #First Spike
    p0 = ( 54, H - 353);
    p1 = ( 110, H - 598);
    p2 = ( 135, H - 493);
    p3 = ( 216, H - 572);
    p4 = ( 188, H - 498);
    p5 = ( 133, H - 353);
    p6 = ( 76, H - 353);
    seq = [p0, p1, p2, p3, p4, p5]
    line = [ p1, p6 ]

    canvas.polygon(seq, outline='black', fill='orange')
    canvas.line(line,fill='black')

    #Editted Polys
    p0 = (85, H - 431)
    p1 = (162, H - 483)
    p2 = (209, H - 486)
    p3 = (222, H - 479)
    p4 = (236, H - 434)
    p5 = (170, H - 365)
    poly = [p0, p1, p2, p3, p4, p5]
    p0 = (188, H - 496)
    p1 = (188, H - 484.5)
    p2 = (162, H - 483)
    poly2 = [p0, p1, p2]

    canvas.polygon(poly, fill='white')
    canvas.polygon(poly2, fill='white')

    #Ridge
    a = (87, H - 431)
    b = (80, H - 414)
    c = (95, H - 385)
    ab = [a, b]
    bc = [b, c]
    d = (131, H - 437)
    e = (149, H - 428)
    f = (180, H - 363)
    de = [d, e]
    ef = [e, f]
    ad = [a, d]
    bruh = [a,b,c,f,e,d]


    canvas.line( bc,fill='black' )
    canvas.line( ab,fill='black' )
    canvas.line( ef,fill='black' )
    canvas.line( de,fill='black' )
    canvas.line( ad,fill='black' )
    canvas.polygon(bruh, fill='white', outline='black')

    #Inner Ridge
    p0 = (160, H - 365)
    p1 = (156, H - 391)
    p2 = (148, H - 401)
    p3 = (133, H - 419)
    p4 = (92, H - 414)
    p5 = (118, H - 365)
    poly = [p0, p1, p2, p3, p4, p5]

    canvas.polygon( poly, fill='black')

    #Front Notch
    p0 = (148, H - 401)
    p1 = (156, H - 391)
    p2 = (170, H - 364)
    p3 = (122, H - 311)
    p4 = (73, H - 280)
    p5 = (60, H - 283)
    p6 = (58, H - 291)
    p7 = (32, H - 313)
    p8 = (41, H - 342)
    p9 = (110, H - 395)
    # inner line, p6, p10, p1
    p10 = (98, H - 335)
    poly = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]
    line = [p7, p10, p1]

    canvas.polygon(poly, fill='black')
    canvas.line(line)

    #Outer Ridge
    p0 = (85, H - 431)
    np = (162, H - 483)
    p1 = (340, H - 538)
    p2 = (490, H - 506)
    p3 = (568, H - 390)
    # line between these two
    p4 = (518, H - 363)
    p5 = (459, H - 437)
    # separate arcs
    p6 = (396, H - 459)
    p7 = (297, H - 463)
    arc1 = [p0,np, p1]
    arc2 = [p1, p2]
    arc3 = [p2, p3]
    line = [p3, p4]
    arc4 = [p4, p5]
    arc5 = [p6, p7]

    canvas.line(arc1, fill='black')
    canvas.line(arc2, fill='black')
    canvas.line(arc3, fill='black')
    canvas.line(line, fill='black')
    canvas.line(arc4, fill='black')
    canvas.line(arc5,fill='black')

    #Second Spike
    p0 = (122, H - 311)
    p1 = (366, H - 566)
    p2 = (247, H - 388)
    poly = [p0, p1, p2]

    canvas.polygon(poly, fill='orange',outline='black')

    #Third Spike
    p0 = (122, H - 311)
    p1 = (155, H - 347)
    p2 = (558, H - 536)
    p3 = (315, H - 366)
    p4 = (269, H - 359)
    poly = [p0, p1, p2, p3, p4]
    #this line is in the wrong spike
    p0 = (366, H - 566)
    p1 = (160, H - 336)
    l1 = [p0,p1]
    #two more lines
    p0 = (122, H - 311)
    p1 = (558, H - 536)
    l2 = [p0,p1]
    p0 = (495, H - 505)
    p1 = (274, H - 360)
    l3 = [p0, p1]

    canvas.line(l1, fill='black')
    canvas.polygon( poly, fill='orange',outline='black')
    canvas.line(l3)
    canvas.line(l2, fill='black')


    #Ridge Lines
    p0 = (236, H - 434)
    p1 = (162, H - 483)
    p2 = (209, H - 486)
    p3 = (222, H - 479)
        #other line
    p4 = (140, H - 440)
    np = (209, H - 486)
    p5 = (317, H - 522)
    line = [ p0, p3, p2, p1]
    other_line = [ p4, np, p5]

    canvas.line( line, fill='black' )
    canvas.line( other_line, fill='black' )

    #Bolts (circles)
    c1_1 = (216, H - 473)
    c1_2 = (219, H - 471)
    c2_2 = (230, H - 477)
    c2_1 = (227, H - 479)
    c3_1 = (229, H - 436)
    c3_2 = (232, H - 433)
    c4_2 = (240, H - 440)
    c4_1 = (237, H - 443)
    c5_2 = (290, H - 348)
    c5_1 = (286, H - 351)
    c6_2 = (294, H - 351)
    c6_1 = (291, H - 354)
    c7_1 = (295, H - 357)
    c7_2 = (300, H - 354)
    c8_1 = (307, H - 315)
    c8_2 = (311, H - 312)
    c9_2 = (380, H - 323)
    c9_1 = (377, H - 325)
    c10_2 = (419, H - 351)
    c10_1 = (416, H - 354)
    circ_1 = [c1_1, c1_2]
    circ_2 = [c2_1, c2_2]
    circ_3 = [c3_1, c3_2]
    circ_4 = [c4_1, c4_2]
    circ_5 = [c5_1, c5_2]
    circ_6 = [c6_1, c6_2]
    circ_7 = [c7_1, c7_2]
    circ_8 = [c8_1, c8_2]
    circ_9 = [c9_1, c9_2]
    circ_10 = [c10_1, c10_2]

    canvas.ellipse( circ_1, outline="black")
    canvas.ellipse( circ_2, outline="black" )
    canvas.ellipse( circ_3, outline="black" )
    canvas.ellipse( circ_4, outline="black")
    canvas.ellipse( circ_5, outline="black" )
    canvas.ellipse( circ_6, outline="black" )
    canvas.ellipse( circ_7, outline="black" )
    canvas.ellipse( circ_8, outline="black" )
    canvas.ellipse( circ_9, outline="black" )
    canvas.ellipse( circ_10, outline="black" )

    #Marks (lines)(made in pairs ex: p0, p1)
    p0 = (220, H - 434)
    p1 = (224.5, H - 426)
    p2 = (217.5, H - 431.5)
    p3 = (222,H - 424)
    p4 = (215, H - 429)
    p5 = (219, H - 422)
    p6 = (212.5, H - 426.5)
    p7 = (216, H - 419)
    p8 = (227, H - 325)
    p9 = (220, H - 319)
    p10 = (223, H - 327)
    p11 = (216, H - 322)
    l1 = [p0, p1]
    l2 = [p2, p3]
    l3 = [p4, p5]
    l4 = [p6, p7]
    l5 = [p8, p9]
    l6 = [p10, p11]

    canvas.line(l1, fill='black')
    canvas.line(l2, fill='black')
    canvas.line(l3, fill='black')
    canvas.line(l4, fill='black')
    canvas.line(l5, fill='black')
    canvas.line(l6, fill='black')

    #Top Lower Curves (arcs?)
    p0 = (454, H - 460)
    np = (455, H - 399.3)
    np1 = (424.1, H - 350.2)
    p1 = (390, H - 323)
    np2 = (325, H - 303.7)
    p2 = (261, H - 304)
    p3 = (155, H - 280)
    p4 = (74.5, H - 247)
        #line stuff, dont forget p4^
    p5 = (74, H - 279)

    p6 = (74, H - 250)
    p7 = (69, H - 251)
    p8 = (66, H - 249)
    p9 = (65, H -279)
    p10 = (66, H - 249)
    p11 = (54.5, H - 292)
    np3 = (281, H - 333.5)
    np4 = (296, H - 305)
    np5 = (370, H - 400)
    np6 = (423, H - 353)
    c1 = [p0, np, np1, p1]
    c2 = [p1, np2, p2]
    c3 = [p2, p3]
    c4 = [p3, p4]
    l1 = [p4, p5]
    l2 = [p6, p7]
    l3 = [p7, p8]
    l4 = [p8, p9]
    c5 = [p10, p11]
    l5 = [np3,np4]
    l6 = [np5,np6]

    canvas.line(c1, fill='black')
    canvas.line(c2, fill='black')
    canvas.line(c3, fill='black')
    canvas.line(c4, fill='black')
    canvas.line(l1, fill='black')
    canvas.line(l2, fill='black')
    canvas.line(l3, fill='black')
    canvas.line(l4, fill='black')
    canvas.line(c5, fill='black')
    canvas.line(l5, fill='black')
    canvas.line(l6, fill='black')

    #Weird Module Part
    p0 = (239.6, H - 326)
    p1 = (215, H - 299)
    p2 = (218, H - 297)
    p3 = (256.1, H - 316.2)
    poly = [p0,p1,p2,p3]
    p0 = (240.7, H - 332.2)
    p1 = (239.6, H - 326)
    p2 = (256.1, H - 316.2)
    p3 = (271.4, H - 327.2)
    p4 = (246.6, H - 342.2)
    poly2 = [p0,p1,p2,p3,p4]
    p0 = (271.4, H - 327.2)
    p1 = (314.7, H - 361)
    l1 = [p0,p1]
    p0 = (246.6, H - 342.2)
    p1 = (270.8, H - 359)
    l2 = [p0,p1]
    p0 = (248, H - 328)
    p1 = (252, H - 324)
    c1 = [p0,p1]

    canvas.polygon(poly, fill='grey', outline='black')
    canvas.polygon(poly2, fill='grey', outline='black')
    canvas.line(l1, fill='black')
    canvas.line(l2, fill='black')
    canvas.ellipse(c1, fill='black')

    #Eyes
    p0 = (128.5, H - 263)
    p1 = (96, H - 250)
    p2 = (76, H - 218)
    p3 = (105, H - 219)
    p4 = (154.2, H - 238.8)
    p5 = (192.5, H - 247)
    p6 = (225.5, H - 267.7)
    p7 = (232, H - 288.4)
    p8 = (187.5, H - 258.8)
    p9 = (148, H - 252)
    poly = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9]

    canvas.polygon(poly, fill="grey")

    p0 = (128.5, H - 263)
    p1 = (105, H - 219)
    l1 = [p0,p1]
    #line
    p2 = (154.2, H - 238.8)
    p3 = (148, H - 252)
    l2 = [p2,p3]
    #line
    p4 = (232, H - 288.4)
    p5 = (187.5, H - 258.8)
    l3 = [p4, p5]
    #line
    p6 = (210, H - 258)
    p7 = (207, H - 262.5)
    l4 = [p6, p7]
    #line
    p8 = (105, H - 219)
    p9 = (198, H - 241.5)
    p10 = (237, H - 268.5)
    p11 = (244, H - 294)
    l5 = [p8, p9, p10, p11]

    canvas.line(l1, fill='black')
    canvas.line(l2, fill='black')
    canvas.line(l3, fill='black')
    canvas.line(l4, fill='black')
    canvas.line(l5, fill='black')

    #Inner Mouth (poly)
    p0 = (205, H - 195)
    p1 = (328, H - 227)
    p2 = (345, H - 200)
    p3 = (292, H - 150)
    p4 = (180, H - 79)
    p5 = (155, H - 120)
    p6 = (154.9, H - 140.2)
    p7 = (159.6, H - 147.6)
    p8 = (165, H - 145.2)
    p9 = (168.8, H - 142.8)
    p10 = (175.3, H - 145.8)
    p11 = (174.9, H - 153.7)
    p12 = (177.7, H - 158.3)
    p13 = (178.2, H - 161.5)
    p14 = (181.8, H - 162.6)
    p15 = (190.5, H - 162.6)
    p16 = (192.9, H - 166)
    p17 = (204.9, H - 167.5)
    p18 = (213.7, H - 172.3)
    p19 = (208.5, H - 183.3)
    poly = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19]

    canvas.polygon(poly,fill='black',outline='black')

    #Nose part
    p0 = (87, H - 246)
    p1 = (87, H - 242)
    p2 = (82, H - 239)
    p3 = (69, H - 217)
    p4 = (100, H - 184)
    p5 = (135, H - 184)
    p6 = (160, H - 192)
    p7 = (163, H - 192)
    p8 = (163, H - 189)
    p9 = (171, H - 192)
    p10 = (175, H - 191)
    p11 = (191, H - 199)
    p12 = (204, H - 206)
    p13 = (210, H - 205)
    p14 = (214, H - 208)
    p15 = (220, H - 210)
    l1 = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]

    canvas.line(l1, fill='black')

    #polygons
    p0 = (80, H - 205)
    p1 = (83, H - 202)
    p2 = (124, H - 202.5)
    p3 = (124, H - 205.4)
    poly1 = [p0,p1,p2,p3]
    p0 = (89, H - 195.9)
    p1 = (91, H - 193.5)
    p2 = (124, H - 193.4)
    p3 = (124, H - 196)
    poly2 = [p0,p1,p2,p3]
    p0 = (328, H - 342.5)
    p1 = (333.3, H - 340.1)
    p2 = (359.1, H - 355)
    p3 = (357.5, H - 358.8)
    poly3 = [p0,p1,p2,p3]
    p0 = (337, H - 338.7)
    p1 = (342, H - 337)
    p2 = (361.5, H - 347.5)
    p3 = (360, H - 351)
    poly4 = [p0,p1,p2,p3]
    p0 = (346.6, H - 335)
    p1 = (351.5, H - 333)
    p2 = (364, H - 340)
    p3 = (363, H - 344)
    poly5 = [p0,p1,p2,p3]

    canvas.polygon(poly1, fill='black')
    canvas.polygon(poly2, fill='black')
    canvas.polygon(poly3, fill='black')
    canvas.polygon(poly4, fill='black')
    canvas.polygon(poly5, fill='black')

    #Top Teeth (poly)
    p0 = (106.5, H - 183)
    p1 = (113.5, H - 171.4)
    p2 = (125.5, H - 171.3)
    p3 = (128.9, H - 182.7)
    poly = [p0,p1,p2,p3]
    p0 = (135, H - 184)
    p1 = (139.6, H - 175.4)
    p2 = (144.6, H - 173.4)
    p3 = (151.6, H - 177)
    p4 = (154.2, H - 185.6)
    p5 = (165, H - 177.8)
    p6 = (168.5, H - 174.7)
    p7 = (175.2, H - 175.3)
    p8 = (174.9, H - 191.9)
    p9 = (160, H - 191.9)
    poly1 = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9]
    p0 = (179.2, H - 193)
    p1 = (191.4, H - 190.6)
    p2 = (196.1, H - 188.6)
    p3 = (199, H - 184.1)
    p4 = (204.5, H - 184.3)
    p5 = (209.86, H - 187.1)
    p6 = (209.85, H - 204.6)
    p7 = (204.3, H - 206.8)
    poly2 = [p0,p1,p2,p3,p4,p5,p6,p7]
    p0 = (210, H - 201)
    p1 = (216.9, H - 198.3)
    p2 = (222.5, H - 198.66)
    p3 = (225.14, H - 203.34)
    p4 = (221, H - 209.7)
    p5 = (217.8, H - 208.16)
    p6 = (213.8, H - 208.1)
    p7 = (210.05, H - 205.56)
    poly3 = [p0,p1,p2,p3,p4,p5,p6,p7]

    canvas.polygon(poly, fill='grey', outline='black')
    canvas.polygon(poly1, fill='grey', outline='black')
    canvas.polygon(poly2, fill='grey', outline='black')
    canvas.polygon(poly3, fill='grey', outline='black')

    # Triangle
    p0 = (281, H - 228)
    p1 = (293.9, H - 204.3)
    p2 = (291.8, H - 195)
    p3 = (322, H - 223.4)
    poly = [p0, p1, p2, p3]

    canvas.polygon(poly, fill='white')

    #Right of face
    p0 = (261, H - 304)
    p1 = (256, H - 280)
    p2 = (215, H - 236)
    l1 = [p0,p1,p2]
    p0 = (303, H - 301.5)
    p1 = (302.2, H - 282.3)
    p2 = (266.3, H - 236.7)
    l2 = [p0,p1,p2]
    p0 = (302.2, H - 282.2)
    p1 = (318.4, H - 270)
    l3 = [p0,p1]
    p0 = (388.2, H - 322.4)
    p1 = (318.7, H - 270)
    p2 = (280.8, H - 227.6)
    l4 = [p0,p1,p2]
    p0 = (343.2, H - 242.2)
    p1 = (289.8, H - 192.4)
    l5 = [p0,p1]

    canvas.line(l1, fill='black')
    canvas.line(l2, fill='black')
    canvas.line(l3, fill='black')
    canvas.line(l4, fill='black')
    canvas.line(l5, fill='black')

    #polygons
    p0 = (215, H - 236)
    p1 = (266.3, H - 236.7)
    p2 = (280.8, H - 227.6)
    p3 = (293, H - 203)
    p4 = (290, H - 192.5)
    p5 = (264.5, H - 178.2)
    p6 = (245.6, H - 178.3)
    p7 = (235, H - 186)
    p8 = (213, H - 224.2)
    poly1 = [p0,p1,p2,p3,p4,p5,p6,p7,p8]
    p0 = (225, H - 227)
    p1 = (267, H - 226)
    p2 = (279, H - 203)
    p3 = (253, H - 188.5)
    p4 = (245, H - 191)
    poly2 = [p0,p1,p2,p3,p4]

    canvas.polygon(poly1,fill='white',outline='black')
    canvas.polygon(poly2,fill="grey",outline='black')

    #lines
    p0 = (235.5, H - 227)
    p1 = (253.2, H - 196.4)
    p2 = (246, H - 190.3)
    p3 = (278, H - 203)
    l1 = [p0,p1,p3]
    l2 = [p1,p2]
    p0 = (247.4, H - 227)
    p1 = (252, H - 217.2)
    p2 = (270.3, H - 218)
    l3 = [p0,p1,p2]
    p0 = (250.8, H - 227.3)
    p1 = (254, H - 220)
    p2 = (269.2, H - 221)
    l4 = [p0,p1,p2]
    p0 = (257.2, H - 212.4)
    p1 = (271.8, H - 204.6)
    c1 = [p0,p1]

    canvas.line(l1, fill='black')
    canvas.line(l2, fill='black')
    canvas.line(l3, fill='white')
    canvas.line(l4, fill='white')
    canvas.ellipse(c1, outline='black')

    #Bottom Teeth (poly)
    p0 = (175, H - 78)
    p1 = (164, H - 88.5)
    p2 = (156.5, H - 97.9)
    p3 = (148, H - 113.7)
    p4 = (150.1, H - 124.9)
    p5 = (153.3, H - 126.5)
    p6 = (156.5, H - 113.9)
    p7 = (159.7, H - 109.2)
    p8 = (163.8, H - 110.3)
    p9 = (161.5, H - 114.4)
    p10 = (161.7, H - 124.3)
    p11 = (162.4, H - 127.2)
    p12 = (166.5, H - 129.3)
    p13 = (172, H - 115.3)
    p14 = (175, H - 116.7)
    p15 = (180, H - 112.6)
    p16 = (185, H - 113.9)
    p17 = (188, H - 116)
    p18 = (189.3, H - 147.5)
    p19 = (191.7, H - 150)
    p20 = (198, H - 149)
    p21 = (200.6, H - 143.4)
    p22 = (201.5, H - 133.2)
    p23 = (203, H - 124.4)
    p24 = (206.2, H - 122.3)
    p25 = (213.1, H - 122)
    p26 = (219, H - 121.2)
    p27 = (232.2, H - 114.6)
    p28 = (236.5, H - 122)
    p29 = (241.2, H - 122.7)
    p30 = (241.3, H - 125.5)
    p31 = (244.3, H - 127.5)
    p32 = (243.8, H - 133)
    p33 = (248, H - 140.4)
    p34 = (247.6, H - 149.7)
    p35 = (246.3, H - 153.8)
    p36 = (254.9, H - 155.6)
    p37 = (259.9, H - 153.5)
    p38 = (261.1, H - 148)
    p39 = (266.3, H - 141.7)
    p40 = (272.5, H - 143.1)
    p41 = (275.2, H - 152.3)
    p42 = (275, H - 157.2)
    p43 = (281.8, H - 157.4)
    p44 = (285.2, H - 155.3)
    p45 = (302.1, H - 159.6)
    p46 = (302.4, H - 167.1)
    p47 = (305.2, H - 169.8)
    p48 = (309.8, H - 170)
    p49 = (316.4, H - 170.5)
    p50 = (321.9, H - 176.1)
    p51 = (321.5, H - 187.4)
    p52 = (319.4, H - 192.6)
    p53 = (324.6, H - 195.1)
    p54 = (329.3, H - 194.4)
    p55 = (335, H - 189.1)
    p56 = (339, H - 186.6)
    p57 = (341.9, H - 190.8)
    p58 = (348.4, H - 189.3)
    p59 = (358, H - 156.7)
    p60 = (239.7, H - 47.7)
    p61 = (223.2, H - 74.2)
    p62 = (215.8, H - 81.5)
    p63 = (208.2, H - 83)
    poly = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50,p51,p52,p53,p54,p55,p56,p57,p58,p59,p60,p61,p62,p63]

    canvas.polygon(poly, fill='grey', outline='black')

    #Crimson Chin
    p0 = (175, H - 64)
    p1 = (165, H - 43)
    p2 = (170, H - 34)
    p3 = (175, H - 36)
    poly = [p0,p1,p2,p3]
    p0 = (167, H - 46)
    p1 = (175, H - 36)
    l1 = [p0,p1]
    p0 = (175, H - 77)
    p1 = (175, H - 5)
    p2 = (179, H - 3)
    p3 = (197, H - 3)
    p4 = (201, H - 5)
    p5 = (237, H - 49)
    p6 = (222.9, H - 75.5)
    p7 = (215.9, H - 81.3)
    p8 = (207, H - 82.6)
    poly2 = [p0,p1,p2,p3,p4,p5,p6,p7,p8]
    p0 = (175, H - 5)
    p1 = (181, H - 25)
    p2 = (201, H - 5)
    l2 = [p0,p1,p2]
    p0 = (181, H - 25)
    p1 = (188, H - 45)
    p2 = (188, H - 60)
    p3 = (180, H - 79)
    l3 = [p0,p1,p2,p3]
    p0 = (237, H - 49)
    p1 = (242, H - 45)
    l4 = [p0,p1]
    p0 = (237, H - 35)
    p1 = (238.9, H - 26.1)
    p2 = (243.4, H - 26.8)
    p3 = (267.6, H - 51.7)
    p4 = (272, H - 95.8)
    poly3 = [p0,p1,p2,p3,p4]
    p0 = (240, H - 40)
    p1 = (243.4, H - 26.8)
    l5 = [p0,p1]

    canvas.polygon(poly,fill='orange',outline='black')
    canvas.line(l1, fill='black')
    canvas.polygon(poly2,fill=(139,26,26))
    canvas.line(l2, fill='black')
    canvas.line(l3, fill='black')
    canvas.line(l4, fill='black')
    canvas.polygon(poly3,fill='orange',outline='black')
    canvas.line(l5, fill='black')

    #Jaw Part (poly)
    p0 = (275, H - 125)
    p1 = (269.2, H - 50.2)
    p2 = (267.6, H - 51.7)
    p3 = (282, H - 48.7)
    p4 = (362.2, H - 111.4)
    p6 = (388, H - 193.2)
    p7 = (356.7, H - 203.8)
    p8 = (348.7, H - 185.4)
    p9 = (323, H - 160)
    p10 = (293.4, H - 138.3)
    poly = [p0,p1,p2,p3,p4,p6,p7,p8,p9,p10]

    canvas.polygon(poly,fill='white',outline='black')

    #Back Jaw (poly,lines, and possibly circles)
    p0 = (284, H - 124)
    p1 = (284.7, H - 75.6)
    p2 = (282.1, H - 62.9)
    p3 = (290.2, H - 72.6)
    p4 = (295.5, H - 81.7)
    p5 = (300, H - 94.5)
    p6 = (301.3, H - 100)
    p7 = (302.6, H - 132.4)
    poly = [p0,p1,p2,p3,p4,p5,p6,p7]
    p0 = (334, H - 90)
    p1 = (336.4, H - 117.7)
    p2 = (373, H - 144.3)
    l1 = [p0,p1,p2]

    canvas.polygon(poly, fill='grey', outline='black')
    canvas.line(l1,fill='black')



    #Final Part
    p0 = (330, H - 273)
    p1 = (324.7, H - 269.6)
    p2 = (324.3, H - 263.5)
    p3 = (331.6, H - 261.4)
    p4 = (361.8, H - 203.3)
    p5 = (365, H - 194)
    p6 = (370.2, H - 190.7)
    p7 = (425, H - 203.4)
    p8 = (427.2, H - 210)
    p9 = (439.6, H - 216.2)
    p10 = (455.5, H - 218.2)
    p11 = (500, H - 268.6)
    p12 = (520, H - 319.4)
    p13 = (516.6, H - 363.4)
    p14 = (459.6, H - 437.3)
    p15 = (424.6, H - 351.6)
    p16 = (386.6, H - 322)
    p17 = (344.7, H - 289.7)
    poly = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17]

    #inner poly
    p0 = (345, H - 265)
    p1 = (401, H - 275.3)
    p2 = (408, H - 276.8)
    p3 = (414.4, H - 269.8)
    p4 = (415, H - 210.4)
    p5 = (396.5, H - 200.3)
    p6 = (373.3, H - 201)
    poly1 = [p0,p1,p2,p3,p4,p5,p6]

    #inner inner poly
    p0 = (358, H - 251)
    p1 = (360.2, H - 244.2)
    p2 = (414.6, H - 254.9)
    p3 = (414.6, H - 263)
    np = (385, H - 270)
    poly2 = [p0,p1,p2,p3]
    l1 = [p0,np]
    p0 = (360.6, H - 230.1)
    p1 = (363.2, H - 223.8)
    p2 = (416.5, H - 234.5)
    p3 = (415.7, H - 242.7)
    np = (385, H - 248.5)
    poly3 = [p0,p1,p2,p3]
    l2 = [p0,np]
    p0 = (368.5, H - 211.2)
    p1 = (371.7, H - 205.3)
    p2 = (414.8, H - 211.7)
    p3 = (416, H - 222)
    np = (394, H - 230)
    poly4 = [p0,p1,p2,p3]
    l3 = [p0,np]


    canvas.polygon(poly, fill='white',outline='black')
    canvas.polygon(poly1, fill='grey',outline='black')
    canvas.polygon(poly2, fill='white',outline='black')
    canvas.polygon(poly3,  fill='white',outline='black')
    canvas.polygon(poly4,  fill='white',outline='black')
    canvas.line(l1, fill='black')
    canvas.line(l2, fill='black')
    canvas.line(l3, fill='black')

    #bruhhhhhhhhhhhhhhhhhhh
    p0 = (156, H - 100)
    p1 = (173.1, H - 97)
    p2 = (191.5, H - 99.7)
    p3 = (192.9, H - 97.8)
    p4 = (173.5, H - 94.8)
    p5 = (159.8, H - 95.9)
    poly = [p0,p1,p2,p3,p4,p5]
    p0 = (163, H - 90.3)
    p1 = (179.5, H - 88.5)
    p2 = (196, H - 92.9)
    p3 = (198.1, H - 90.8)
    p4 = (180.7, H - 85.9)
    p5 = (166.2, H - 86.9)
    poly2 = [p0,p1,p2,p3,p4,p5]

    canvas.polygon(poly, fill='black')
    canvas.polygon(poly2, fill='black')

    # return the art
    return im

# no changes to the below
# -----------------------

if ( __name__ == "__main__" ) :

    im = picture()

    im.show()

    im.save( 'my-artistry.jpg' )
