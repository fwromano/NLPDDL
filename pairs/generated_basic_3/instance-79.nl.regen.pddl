```pddl
(define (problem blocksworld-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (hand-empty)
         (on a table)
         (on b c)
         (on c a)
         (clear b))
  (:goal (on a c))
)
```