```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on a b)
         (on b c)
         (on-table c)
         (clear a))
  (:goal (on b a)))
```