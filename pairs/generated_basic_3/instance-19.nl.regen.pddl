```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on a b)
         (on-table b)
         (on-table c)
         (clear a)
         (clear c))
  (:goal (and (on a c)
              (on b a))))
```