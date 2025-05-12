```pddl
(define (problem blocksworld-4ops)
  (:domain blocksworld)
  (:objects a b c - block)
  (:init (empty-hand)
         (on a c)
         (on b table)
         (on c table)
         (clear a)
         (clear b))
  (:goal (and (on a b)
              (on c a))))
```