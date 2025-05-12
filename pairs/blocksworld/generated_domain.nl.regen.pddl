```pddl
(define (problem blocksworld-problem)
  (:domain blocksworld-4ops)
  (:objects block1 block2 block3 block4)
  (:init 
    (on block1 block2)
    (on block2 block3)
    (on block3 table)
    (clear block1)
    (clear block4)
    (handempty)
  )
  (:goal 
    (and 
      (on block1 block3)
      (on block2 block4)
      (clear block2)
      (clear block1)
      (handempty)
    )
  )
)
```