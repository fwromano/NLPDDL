```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on a c)
         (on b table)
         (on c table)
         (clear a)
         (clear b))
  (:goal (and (on a c)
              (on b a)))
)
```