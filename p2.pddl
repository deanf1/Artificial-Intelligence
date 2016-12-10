;; Block A is on the table, block B on A and there is nothing on B.  A
;; water bucket, a brush, a A blue sprayer and a red paint can are on
;; the table and clear.  The goal is to for A to be colored red and B
;; blue and the brush be clean.

(define (problem 2)
  (:domain hw5)
  (:objects blockA blockB waterbucket brush1 blueSprayer redPaintCan)
  (:init (arm-empty)
          ;; block A is on the table
          (block blockA)
          (on-table blockA)
	       ;; block B is on block A and there's nothing on B
         (block blockB)
         (on blockB blockA)
         (clear blockB)
         ;; there is a blue sprayer on the table and nothing is on it 
         (sprayer blueSprayer blue)
         (on-table blueSprayer)
         (clear blueSprayer)
	       ;; there is a red paint can on the table and noting is on it
         (paint-can redPaintCan red)
         (on-table redPaintCan)
         (clear redPaintCan)
	       ;; there is a clean brush on the table and nothing is on it 
         (brush brush1)
         (on-table brush1)
         (clear brush1)
         (clean brush1)
	       ;; there is a water bucket on the table and nothing is on it
         (water-bucket waterbucket)
         (on-table waterbucket)
         (clear waterbucket)
      )
  (:goal (and (arm-empty)
              ;; A is red
              (color blockA red)
              ;; B is blue
              (color blockB blue)
              ;; the brush is clean
              (clean brush1)

              (clear waterbucket)
              (clear brush1)
              (clear blueSprayer)
              (clear redPaintCan)              
           )))