
taskplan:
- braille module
  - BrailleTranslator(text)
    - as-grade-1 -> braillestring
    - as-grade-2 -> braillestring
  - BrailleString
    - as unicode
    - as cells
  - BrailleCell
    - as unicode
    - dot[n]
- motioner:
 - make a plan
   - give it shape (bottle)
   - give it home?
   - render-braille-into-it.

Or is it the reverse? A planner-base that from braille that the more master think talks to?
but that thing probably still needs knowledge of its space. Think smart line-breaks.
Lets go with a pure-planner that groks braille for now. We can refactor later if needed.
Mmmm. no. It should be able to spit out a set of movements (even gcode for now), but those should
exist out-of-space. IT should make a list of movements, ONLY.

Not real readme yet... just my working notes :)

Need:
- braillie patterns
- braillie contraints (note: according to https://www.compliancesigns.com/media/resource-bulletins/CRB-ADA-Braille.pdf, distance between dots is measure center-to-center. The dot size really doesn't change spacing between rows/characters)
  - Dot base diameter: 1.5mm to 1.6mm
  - Distance between two dots in the same cell: 2.3mm to 2.5mm (California->2.5mm)
  - Distance between correstponding dots in adjacent cell: 6.1mm to 7.6mm (ca=7.6mm)
  - Doit height = 0.6mm to 0.9mm
  - Distance between correstponding dot one cell directly below: 10mm to 10.2mm
  - Drill depth
  - Drill width
- grbl mm ratio
- shape of target
- home location ON target.
- string!

Motion-planning-thoughts:
- mind-simple:
  - translate to grade-2
  - move to sp_x, sp_y.
  - walk through characters:
    - walk through dots-in-character:
      - start upper-left.
      - if dot, do drill-step.
      - move down by inter_dot_distance
      - if dot, do drill-step.
      - move down by inter_dot_distance
      - if dot, do drill-step.
      - move over by inter_dot_distance
      - if dot, do drill-step
      - move up by inter_dot_distance
      - if dot, do drill-step
      - move up by inter-dot-distance
      - if dot, do drill-step
    - move over by inter_cell_dot_distance - inter-dot-distance
  - comments:
    - single line, though if one tracks hz-distance, a 'newline' could zip-back and down.
    - we move through the entire cell, even on a space.
- slightly-smarter
  - translate
  - set mv_x, mv_y to sp_x, sp_y
  - walk through characters
    - walk through dots-in-character
      - if dot, do mv_x, mv_y, drill, mv_x, mv_y = 0
      - mv_y += inter_dot_distance
      - if dot, do mv_x, mv_y, drill, mv_x, mv_y = 0
      - mv_y += inter_dot_distance
      - if dot, do mv_x, mv_y, drill, mv_x, mv_y = 0
      - mv_x += inter_dot_distance
      - if dot, do mv_x, mv_y, drill, mv_x, mv_y = 0
      - mv_y -= inter_dot_distance
      - if dot, do mv_x, mv_y, drill, mv_x, mv_y = 0
      - mv_y += inter_dot_distance
      - if dot, do mv_x, mv_y, drill, mv_x, mv_y = 0
    - mv_y += inter_cell_dot_distance  - inter-dot-distance
  - comments:
    - still single line, but same applies
    - we are way smarter on move steps. 
      
      
Calulation-process?
- starting-points:
  - sp_x = sp_y = dot_base_diameter / 2   ... everything is relative to that
- 
- 