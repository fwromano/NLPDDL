```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on-table a)
         (on-table b)
         (on c a)
         (clear b)
         (clear c))
  (:goal (and (on a c)
              (on b a))))
```