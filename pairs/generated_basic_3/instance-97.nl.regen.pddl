```pddl
(define (problem blocksworld-4ops-problem)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (hand-empty)
         (on a table)
         (on b a)
         (on c b)
         (clear c))
  (:goal (on c a))
)
```