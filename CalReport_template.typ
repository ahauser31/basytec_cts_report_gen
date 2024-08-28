/* VARIABLE EXAMPLES

// The following values have to be set for the report to be generated correctly

#let signer_name = [Andreas Hauser]
#let signer_title = [Manager - A*STAR Battery Test Facility]

#let calibrated_by = [Dexter Ong]
#let calibrated_by_title = [Lab Technician]

#let report_number = [C202408001]

#let submitter_company = [Sample Pte Ltd]
#let submitter_company_address = [1 Sample Road\ \#01-01 Sample building\ Singapore 999999]

#let tester_model = [CTS 32 channel]
#let tester_serial = [CTS.X.15.00.0724]
#let tester_id = [724]

#let date_received = [03/08/2024]
#let date_calibrated = [03/08/2024]
#let date_recommended = [03/08/2025]

#let calibration_sop = [Calibrating BaSyTec Battery Test System]
#let calibration_sop_date = [5/6/2024]
#let software_version = [6.0.16.0]

#let multimeter_due = [20/8/2025]
#let multimeter_report = [XZY]
#let calibrator_due = [02/07/2025]
#let calibrator_report = [XYZ]

#let condition_received_tolerance = [Yes]
#let condition_received_remark = [N/A]
#let condition_shipped_tolerance = [Yes]
#let condition_shipped_remark = [N/A]
*/

/* CHANNEL ARRAY EXAMPLE

// The following array is an example of the parameter required to call the channel table creation function
#let array1 = (
  "af I1 -90 av", 
  "af I1 -90 mv",
  "af I1 -90 dv",
  "al I1 -90 av",
  "al I1 -90 mv",
  "al I1 -90 dv",
  "I1 -90 uc",

  "af I1 -10 av", 
  "af I1 -10 mv",
  "af I1 -10 dv",
  "al I1 -10 av",
  "al I1 -10 mv",
  "al I1 -10 dv",
  "I1 -10 uc",

  "af I1 10 av", 
  "af I1 10 mv",
  "af I1 10 dv",
  "al I1 10 av",
  "al I1 10 mv",
  "al I1 10 dv",
  "I1 10 uc",

  "af I1 90 av", 
  "af I1 90 mv",
  "af I1 90 dv",
  "al I1 90 av",
  "al I1 90 mv",
  "al I1 90 dv",
  "I1 90 uc",

  "af I2 -90 av", 
  "af I2 -90 mv",
  "af I2 -90 dv",
  "al I2 -90 av",
  "al I2 -90 mv",
  "al I2 -90 dv",
  "I2 -90 uc",

  "af I2 -10 av", 
  "af I2 -10 mv",
  "af I2 -10 dv",
  "al I2 -10 av",
  "al I2 -10 mv",
  "al I2 -10 dv",
  "I2 -10 uc",

  "af I2 10 av", 
  "af I2 10 mv",
  "af I2 10 dv",
  "al I2 10 av",
  "al I2 10 mv",
  "al I2 10 dv",
  "I2 10 uc",

  "af I2 90 av", 
  "af I2 90 mv",
  "af I2 90 dv",
  "al I2 90 av",
  "al I2 90 mv",
  "al I2 90 dv",
  "I2 90 uc",

  "af I3 -90 av", 
  "af I3 -90 mv",
  "af I3 -90 dv",
  "al I3 -90 av",
  "al I3 -90 mv",
  "al I3 -90 dv",
  "I3 -90 uc",

  "af I3 -10 av", 
  "af I3 -10 mv",
  "af I3 -10 dv",
  "al I3 -10 av",
  "al I3 -10 mv",
  "al I3 -10 dv",
  "I3 -10 uc",

  "af I3 10 av", 
  "af I3 10 mv",
  "af I3 10 dv",
  "al I3 10 av",
  "al I3 10 mv",
  "al I3 10 dv",
  "I3 10 uc",

  "af I3 90 av", 
  "af I3 90 mv",
  "af I3 90 dv",
  "al I3 90 av",
  "al I3 90 mv",
  "al I3 90 dv",
  "I3 90 uc",

  "af I4 -90 av", 
  "af I4 -90 mv",
  "af I4 -90 dv",
  "al I4 -90 av",
  "al I4 -90 mv",
  "al I4 -90 dv",
  "I4 -90 uc",

  "af I4 -10 av", 
  "af I4 -10 mv",
  "af I4 -10 dv",
  "al I4 -10 av",
  "al I4 -10 mv",
  "al I4 -10 dv",
  "I4 -10 uc",

  "af I4 10 av", 
  "af I4 10 mv",
  "af I4 10 dv",
  "al I4 10 av",
  "al I4 10 mv",
  "al I4 10 dv",
  "I4 10 uc",

  "af I4 90 av", 
  "af I4 90 mv",
  "af I4 90 dv",
  "al I4 90 av",
  "al I4 90 mv",
  "al I4 90 dv",
  "I4 90 uc",

  "af U 10 av", 
  "af U 10 mv",
  "af U 10 dv",
  "al U 10 av",
  "al U 10 mv",
  "al U 10 dv",
  "U 10 uc",

  "af U 50 av", 
  "af U 50 mv",
  "af U 50 dv",
  "al U 50 av",
  "al U 50 mv",
  "al U 50 dv",
  "U 50 uc",

  "af U 90 av", 
  "af U 90 mv",
  "af U 90 dv",
  "al U 90 av",
  "al U 90 mv",
  "al U 90 dv",
  "U 90 uc",

  "af T r1 av", 
  "af T r1 mv",
  "af T r1 dv",
  "al T r1 av",
  "al T r1 mv",
  "al T r1 dv",
  "T r1 uc",

  "af T r2 av", 
  "af T r2 mv",
  "af T r2 dv",
  "al T r2 av",
  "al T r2 mv",
  "al T r2 dv",
  "T r2 uc",

  "I1 factor", "I1 offset",
  "I2 factor", "I2 offset",
  "I3 factor", "I3 offset",
  "I4 factor", "I4 offset",
  "U factor", "U offset",
  "T factor", "T offset"
)
*/

// END OF VARIABLES

// START OF TEMPLATE

#let astar_blue = color.rgb("#003087")

#let makechannel(number, array, lastChannel: false) = {
  [
    #v(18pt)
    = #tester_id CTS CH#if number < 10 [0#number] else [#number]

    #set text(size: 8pt)
    #v(6pt)
    #table(
      columns: (auto, auto, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
      align: (center, center, right, right, right, right, right, right, right),
      stroke: 0.5pt,
      table.cell(rowspan: 2, [*Value*]), table.cell(rowspan: 2, [*Range*]), table.cell(colspan: 3, align: center, [*As Found*]), table.cell(colspan: 3, align: center, [*As Left*]), table.cell(rowspan: 2, align: center, [*Uncertainty \ (95%, k ≈ 2)*]),table.cell(align: center, [*Applied Value*]), table.cell(align: center, [*Measured Value*]), table.cell(align: center, [*Deviation*]), table.cell(align: center, [*Applied Value*]), table.cell(align: center, [*Measured Value*]), table.cell(align: center, [*Deviation*]),

      [I1], [-1 mA (90%)], [#array.at(0)], [#array.at(1)], [#array.at(2)], [#array.at(3)], [#array.at(4)], [#array.at(5)], [#array.at(6)],
      [I1], [-1 mA (10%)], [#array.at(7)], [#array.at(8)], [#array.at(9)], [#array.at(10)], [#array.at(11)], [#array.at(12)], [#array.at(13)],
      [I1], [1 mA (10%)], [#array.at(14)], [#array.at(15)], [#array.at(16)], [#array.at(17)], [#array.at(18)], [#array.at(19)], [#array.at(20)],
      [I1], [1 mA (90%)], [#array.at(21)], [#array.at(22)], [#array.at(23)], [#array.at(24)], [#array.at(25)], [#array.at(26)], [#array.at(27)],

      [I2], [-15 mA (90%)], [#array.at(28)], [#array.at(29)], [#array.at(30)], [#array.at(31)], [#array.at(32)], [#array.at(33)], [#array.at(34)],
      [I2], [-15 mA (10%)], [#array.at(35)], [#array.at(36)], [#array.at(37)], [#array.at(38)], [#array.at(39)], [#array.at(40)], [#array.at(41)],
      [I2], [15 mA (10%)], [#array.at(42)], [#array.at(43)], [#array.at(44)], [#array.at(45)], [#array.at(46)], [#array.at(47)], [#array.at(48)],
      [I2], [15 mA (90%)], [#array.at(49)], [#array.at(50)], [#array.at(51)], [#array.at(52)], [#array.at(53)], [#array.at(54)], [#array.at(55)],

      [I3], [-300 mA (90%)], [#array.at(56)], [#array.at(57)], [#array.at(58)], [#array.at(59)], [#array.at(60)], [#array.at(61)], [#array.at(62)],
      [I3], [-300 mA (10%)], [#array.at(63)], [#array.at(64)], [#array.at(65)], [#array.at(66)], [#array.at(67)], [#array.at(68)], [#array.at(69)],
      [I3], [300 mA (10%)], [#array.at(70)], [#array.at(71)], [#array.at(72)], [#array.at(73)], [#array.at(74)], [#array.at(75)], [#array.at(76)],
      [I3], [300 mA (90%)], [#array.at(77)], [#array.at(78)], [#array.at(79)], [#array.at(80)], [#array.at(81)], [#array.at(82)], [#array.at(83)],

      [I4], [-5 A (90%)], [#array.at(84)], [#array.at(85)], [#array.at(86)], [#array.at(87)], [#array.at(88)], [#array.at(89)], [#array.at(90)],
      [I4], [-5 A (10%)], [#array.at(91)], [#array.at(92)], [#array.at(93)], [#array.at(94)], [#array.at(95)], [#array.at(96)], [#array.at(97)],
      [I4], [5 A (10%)], [#array.at(98)], [#array.at(99)], [#array.at(100)], [#array.at(101)], [#array.at(102)], [#array.at(103)], [#array.at(104)],
      [I4], [5 A (90%)], [#array.at(105)], [#array.at(106)], [#array.at(107)], [#array.at(108)], [#array.at(109)], [#array.at(110)], [#array.at(111)],

      [U], [5 V (10%)], [#array.at(112)], [#array.at(113)], [#array.at(114)], [#array.at(115)], [#array.at(116)], [#array.at(117)], [#array.at(118)],
      [U], [5 V (50%)], [#array.at(119)], [#array.at(120)], [#array.at(121)], [#array.at(122)], [#array.at(123)], [#array.at(124)], [#array.at(125)],
      [U], [5 V (90%)], [#array.at(126)], [#array.at(127)], [#array.at(128)], [#array.at(129)], [#array.at(130)], [#array.at(131)], [#array.at(132)],

      [T], [Temp Ref1], [#array.at(133)], [#array.at(134)], [#array.at(135)], [#array.at(136)], [#array.at(137)], [#array.at(138)], [#array.at(139)],
      [T], [Temp Ref2], [#array.at(140)], [#array.at(141)], [#array.at(142)], [#array.at(143)], [#array.at(144)], [#array.at(145)], [#array.at(146)]
    )
    #v(18pt)
    #text(size: 10pt, [*Calibration settings*])
    #table(
      columns: (auto, auto, 20%, 20%),
      align: (center, center, right, right),
      stroke: 0.5pt,
      table.cell(align: center, [*Value*]), table.cell(align: center, [*Range*]), table.cell(align: center, [*Factor*]), table.cell(align: center, [*Offset*]),
      [I1], [±1 mA], [#array.at(147)], [#array.at(148)],
      [I2], [±15 mA], [#array.at(149)], [#array.at(150)],
      [I3], [±300 mA], [#array.at(151)], [#array.at(152)],
      [I4], [±5 A], [#array.at(153)], [#array.at(154)],
      [U], [0 - 6 V], [#array.at(155)], [#array.at(156)],
      [T], [-30°C to 100°C], [#array.at(157)], [#array.at(158)]
    )
    #if lastChannel == false [#pagebreak()] else [
      #v(50pt)
      #text(size: 11pt, [#align(center, [*----- END OF REPORT -----*])])
    ]
  ]
}

#set document(
  author: "Andreas Hauser",
  title: "Calibration Report",
  date: datetime.today()
)

#set page(
  paper: "a4",
  margin: (top: 3.5cm, bottom: 1.1cm, left: 1.7cm, right: 1.7cm),
  footer: [
    #grid(
      columns: (1fr, auto, 1fr),
      stroke: none,
      [],
      [
        #set align(center)
        #text(size: 8pt, fill: astar_blue, font: "Open Sauce One", [A member of A*STAR Research Entities (Co. Reg. No. 199702110H)])
      ],
      [
        #set text(size: 9pt)
        #set align(right)
        #context[Page #here().page() / #counter(page).display()]
      ]
    )
    
  ],
  header-ascent: 0%,
  footer-descent: 0%,
  header: [
    #set text(size: 8pt)
    #grid(
      stroke: none,
      columns: (auto, 1fr, auto),
      align: (left + top, left),
      image("artc_small.png", width: 6.4cm),
      [],
      box[
        #set text(fill: astar_blue)
        *Advanced Remanufacturing\ and Technology Centre (ARTC)*\
        #v(3pt)
        3 CleanTech Loop\
        \#01-01 CleanTeach Two\
        Singapore 637143\
        Tel: (+65) 6908 7900\
        www.a-star.edu.sg/artc
        ]
    )
  ]
)

#set par(justify: true, leading: 0.5em)
#set heading(numbering: "1.", supplement: "Clause")
#set enum(numbering: "(a).(i)")
#set list(marker: "-", indent: 1.2em)

#set text(
  font: "Linux Libertine",
  size: 10pt,
  lang: "en",
  hyphenate: false
)

#show heading: it => [
  #set align(center)
  #set text(size: 14pt, font: "Linux Libertine")
  #strong[#upper(it.body)]
]

#v(16pt)
#align(
  end + top,
  [Report number: #report_number]
)

= Calibration Report
#v(6pt)

#grid(
  columns: (auto, 60pt, auto),
  align: (left, right, left),
  gutter: (6pt, 6pt),
  [*Submitted By*],
  [:#h(10pt)],
  [*#submitter_company* \
  #submitter_company_address],
  [],[],[],
  [*Unit Under Test (UUT)*],
  [:#h(10pt)],
  [Battery Tester],
  [*Manufacturer*],
  [:#h(10pt)],
  [BaSyTec],
  [*Model*],
  [:#h(10pt)],
  [#tester_model],
  [*Serial Number*],
  [:#h(10pt)],
  [#tester_serial],
  [],[],[],
  [*Ambient Temperature*],
  [:#h(10pt)],
  [23 °C ± 3 °C],
  [*Relative Humidity*],
  [:#h(10pt)],
  [(40 to 70)% RH],
  [*Software Version*],
  [:#h(10pt)],
  [#software_version],
  [],[],[],
  [*Date Received*],
  [:#h(10pt)],
  [#date_received],
  [*Date Calibrated*],
  [:#h(10pt)],
  [#date_calibrated],
  [*Recommended Due Date*],
  [:#h(10pt)],
  [#date_recommended]
)

#v(10pt)
//#set text(size: 10pt)
The Advanced Remanufacturing and Technology Centre confirms the UUT has been calibrated under the environmental conditions as stated above. The expanded measurement uncertainties are estimated at a level of confidence of approximately 95% with a coverage factor of k ≈ 2. Calibration is performed with equipment directly traceable to the Singapore national standards. Principles and methods of calibration correspond with ISO/IEC 17025. This calibration certificate shall not be reproduced in part or in full without the written approval of the Advanced Remanufacturing and Technology Centre. Calibration reports without signatures are not valid. The user is advised to have the object recalibrated at appropriate intervals.

#v(10pt)
//#set text(size: 10pt)

#show heading: it => [
  #set align(left)
  #set text(size: 11pt)
  #strong(it.body)
]

= Method of Calibration
#v(4pt)
Calibration is based on the procedure "#calibration_sop", dated #calibration_sop_date

#v(10pt)

= Calibration Equipment Used
#v(2pt)
#table(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  stroke: none,
  align: (left, left, left, left, left),
  table.header([*Description*],[*Model*],[*Serial No.*],[*Cal. report*],[*Cal. Due Date*]),
  table.hline(),
  [Multimeter],
  [HM 8112-3],
  [022844646],
  [#multimeter_report],
  [#multimeter_due],
  [Calibrator],
  [CTS Calibrator],
  [1285.0],
  [#calibrator_report],
  [#calibrator_due]
)

#v(5pt)

= Result of Calibration
#v(4pt)
#table(
  columns: (50%, 50%),
  stroke: 0.5pt,
  table.header(table.cell(align: center)[*As Received Condition*], table.cell(align: center)[*As Shipped Condition*]),
  [Within Tolerance: *#condition_received_tolerance*\
  Remarks: #condition_received_remark],
  [Within Tolerance: *#condition_shipped_tolerance*\
  Remark: #condition_shipped_remark]
)

#v(18pt)
#grid(
  columns: (1fr, 23%, 1fr),
  column-gutter: 20pt,
  grid.cell(align: bottom)[#line(length: 100%)],
  grid.cell(align: center)[Singapore, #datetime.today().display("[day]/[month]/[year]") #line(length: 100%)],
  grid.cell(align: bottom)[#line(length: 100%)],
  grid.cell(inset: (y: 6pt))[Calibrated by:\
  #calibrated_by\
  #text(size: 10pt, style: "italic",[(#calibrated_by_title)])],
  grid.cell(align: center, inset: (y: 6pt))[Place and Date],
  grid.cell(inset: (y: 6pt))[Approved by:\
  #signer_name\
  #text(size: 9.5pt, style: "italic",[(#signer_title)])],
)#pagebreak()

#set page(
  margin: (top: 2.2cm, bottom: 1.1cm, left: 1.0cm, right: 1.0cm),
  header: [
    #set text(size: 8pt)
    #grid(
      stroke: none,
      columns: (auto, 1fr, auto),
      align: (left + top, left),
      image("artc_small.png", width: 4.5cm),
      [],
      [
        #set text(fill: astar_blue)
        *Advanced Remanufacturing\ and Technology Centre (ARTC)*\
        #v(3pt)
        #text(fill: black, size: 10pt, [Report number: #report_number])
      ]
    )
  ],
  footer: [
    #set align(center)
    #set text(size: 9pt)
    #context[Page #here().page() / #counter(page).display()]
  ],
)

/* EXAMPLE OF CHANNEL TABLE GENERATION FUNCTION CALL

#makechannel(0, array1)
#makechannel(1, array1, lastChannel: true)

*/

// Channel tables start here

