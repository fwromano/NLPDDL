```pddl
(define (problem blocksworld-4ops-problem)
  (:domain blocksworld-4ops)
  (:objects
    a b c - block
  )
  (:init
    (empty-hand)
    (on a c)
    (on b a)
    (on-table c)
    (clear b)
  )
  (:goal
    (on a b)
  )
)
```