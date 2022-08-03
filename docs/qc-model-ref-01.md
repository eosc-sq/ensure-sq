# QM Reference 01: (include ISO/IEC 9126): 11, 46, 58, 99, 108, 124, 147

Reviewer:  ER (Elisabetta Ronchieri)

ISO/IEC 25010:2011 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models: https://www.iso.org/standard/35733.html

(paper ID = 46) Standardized code quality benchmarking for improving software maintainability

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Characteristics | Comment |
| :------: | :---: | :--------: | :-----------------: | :-------------: | :-----: |
|          | Volume | size of the software application | aut | Maintainability | the larger a system, the more effort it takes to maintain since there
is more information to be taken into account. |
|          | Redundancy | level of redundancy in code | aut | Maintainability | duplicated code has to be maintained in all places where it
occurs |
|          | Unit Size | lowest-level piece of functionality that should be maintained | aut | Maintainability | lines of code per unit (unit is the smallest piece of invokable code) code |
|          | Complexity | level of complexity that should be comprehended | aut | Maintainability | no specific metric is reported |
|          | Interface Size | number of parameters in interface | aut | Maintainability |  units with many parameters can be a symptom of bad
encapsulation |
|          | Coupling | number of coupled components | aut | Maintainability | tightly coupled components are more resistant to change |
