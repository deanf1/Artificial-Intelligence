;; There is only one block, A, which is on the table.  A can with red
;; paint is on the table.  There is a clean brush on the table.  Our
;; goal is to have A be red, and the arm empty.

(define (problem 1)
  (:domain hw5)
  (:objects blockA redPaintCan brush1)
  (:init (arm-empty)
  		(block blockA)
  		(clear blockA)
        (on-table blockA)
    	(paint-can redPaintCan red)
    	(clear redPaintCan)
    	(on-table redPaintCan)
    	(brush brush1)
    	(clear brush1)
    	(clean brush1)
    	(on-table brush1)
	 )
  (:goal (and (arm-empty) (color blockA red) (clear blockA) (clear redPaintCan)))
