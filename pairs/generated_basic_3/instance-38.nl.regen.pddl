```pddl
(define (problem blocksworld-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (hand-empty)
         (on a b)
         (on b table)
         (on c a)
         (clear c))
  (:goal (on b a))
)
```