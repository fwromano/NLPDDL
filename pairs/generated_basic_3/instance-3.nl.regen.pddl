```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on-table a)
         (on b c)
         (on c a)
         (clear b))
  (:goal (and (on b a)
              (on c b))))
```