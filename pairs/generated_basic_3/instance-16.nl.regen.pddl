```pddl
(define (problem blocksworld-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (hand-empty)
         (on-table a)
         (on b c)
         (on c a)
         (clear b))
  (:goal (and (on a c)
              (on b a)))
)
```