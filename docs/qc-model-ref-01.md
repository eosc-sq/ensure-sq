# QM Reference 01: (include ISO/IEC 9126): 11, 46, 58, 99, 108, 124, 147

Reviewer:  ER (Elisabetta Ronchieri)

ISO/IEC 25010:2011 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models: https://www.iso.org/standard/35733.html

(paper ID = 46) Standardized code quality benchmarking for improving software maintainability

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Characteristics | Comment |
| :------: | :---: | :--------: | :-----------------: | :-------------: | :-----: |
|          | Estimated rebuild value | Evaluate the volume property | aut | Maintainability, Analysability | The larger a system, the more effort it takes to maintain since there is more information to be taken into account. The metric is estimated from the number of lines of code. The value is calculated in man-years. |  
|          | Percentage of Redundant code | evaluate the duplication property | aut | Maintainability, Analysability, Changeability | Duplicated code has to be maintained in all places where it occurs. A line of code is considered redundant if it is part of a code fragment (larger than 6 lines of code) that is repeated literally in at least one other location in the source code. |
|          | Lines of code per unit | the number of lines of code in each unit, evaluating the unit size property | aut | Maintainability, Analysability, Testability | lines of code per unit (unit is the smallest piece of  invokable code) code |
|          | Cyclomatic Complexity per unit (McCabe) | Evaluate the unit complexity property | aut | Maintainability, Changeability, Testability |  |
|          | Number of parameters per unit | number of parameters declared in the interface of each unit | aut | Maintainability, Stability |  units with many parameters can be a symptom of bad encapsulation |
|          | Number of incoming calls per module | number of incoming invocations for each module, evaluating the module coupling property | aut | Maintainability, Changeability, Stability | The notion of module is defined as a delimited group of units (e.g. a class or a file) |
